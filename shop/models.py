from django.db import models


class Category(models.Model):

    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, related_name="sub_categories", blank=True, null=True, verbose_name="Категория")
    name = models.CharField(verbose_name="Имя категории", max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(verbose_name="Фото", upload_to="categories/", blank=True, null=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.parent_category} ({self.name})" if self.parent_category is not None else self.name


class Product(models.Model):

    name = models.CharField(max_length=200, verbose_name="Имя товара")
    category = models.ManyToManyField(Category, related_name="products", verbose_name="Категория")
    image = models.ImageField(verbose_name="Фото", upload_to='products/')
    slug = models.SlugField(max_length=200, unique=True)
    size = models.CharField(verbose_name="Размеры", max_length=150)
    material = models.CharField(verbose_name="Материал", max_length=150)
    weight = models.CharField(verbose_name="Вес", max_length=20)
    price = models.CharField(verbose_name="Цена", max_length=20)
    description = models.TextField(verbose_name="Описание")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты" 

    def __str__(self):
        return f"{', '.join(str(cat_ry) for cat_ry in self.category.all())} - {self.name}"


class ProductImage(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images', verbose_name="Продукт")
    image = models.ImageField(verbose_name="Фото", upload_to="products_images/")

    class Meta:
        db_table = "shop_product_image"
        ordering = ("product__name",)
        verbose_name = "Фото продукта"
        verbose_name_plural = "Фото продуктов" 

    def __str__(self):
        return self.product


class ProductColor(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_colors", verbose_name="Продукт")
    color = models.CharField(verbose_name="Цвет", max_length=50)

    class Meta:
        db_table = "shop_product_color"
        ordering = ("product__name",)
        verbose_name = "Цвет продукта"
        verbose_name_plural = "Цвета продуктов" 

    def __str__(self):
        return self.product


class News(models.Model):

    name = models.CharField(verbose_name="Имя новости", max_length=200)
    description = models.CharField(verbose_name="Описание", max_length=500)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(verbose_name="Фото", upload_to="news/")
    content = models.TextField(verbose_name="Текст новости")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-id",)
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    
    def __str__(self) -> str:
        return self.name
