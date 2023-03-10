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
    
    @property
    def sub_category_first(self):
        return self.sub_categories.order_by("id").first()


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
    
    def product_colors_by_three(self):
        product_colors = self.product_colors.all()
        return [product_colors[i : i + 3] for i in range(0, product_colors.count(), 3)]


class ProductImage(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images', verbose_name="Продукт")
    image = models.ImageField(verbose_name="Фото", upload_to="products_images/")

    class Meta:
        db_table = "shop_product_image"
        ordering = ("product__name",)
        verbose_name = "Фото продукта"
        verbose_name_plural = "Фото продуктов" 

    def __str__(self):
        return str(self.product)


class ProductColor(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_colors", verbose_name="Продукт")
    color = models.CharField(verbose_name="Цвет", max_length=50)

    class Meta:
        db_table = "shop_product_color"
        ordering = ("product__name",)
        verbose_name = "Цвет продукта"
        verbose_name_plural = "Цвета продуктов" 

    def __str__(self):
        return str(self.product)


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


class LogoLayOn(models.Model):

    name = models.CharField(verbose_name="Имя нанесения логотипа", max_length=50)
    image_1 = models.ImageField(verbose_name="Фото нанесения 1", upload_to="logo-lay-ons/")
    image_2 = models.ImageField(verbose_name="Фото нанесения 2", upload_to="logo-lay-ons/")
    image_3 = models.ImageField(verbose_name="Фото нанесения 3", upload_to="logo-lay-ons/")
    image_4 = models.ImageField(verbose_name="Фото нанесения 4", upload_to="logo-lay-ons/")
    video = models.FileField(verbose_name="Видео", upload_to="logo-lay-ons/videos/")

    class Meta:
        db_table = "shop_logo_lay_on"
        ordering = ("id",)
        verbose_name = "Нанесение логотипа"
        verbose_name_plural = "Нанесения логотипа"
    
    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    
    class ContactType(models.TextChoices):
        CALL_ORDER = "call-order", "Звонок на заказ"
        PRODUCT_ORDER = "product-order", "Заказ продукта"
        DEALER = "dealer", "Дилер"
        PROVIDER = "provider", "Поставщик"
    
    name = models.CharField(verbose_name="Имя клиента", max_length=50)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=20)
    type = models.CharField(verbose_name="Тип клиента", max_length=20, choices=ContactType.choices, default=ContactType.CALL_ORDER)
    order = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE, related_name="product_contacts", blank=True, null=True)
    datetime = models.DateTimeField(verbose_name="Дата и время", auto_now_add=True)

    class Meta:
        ordering = ("-id",)
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
    
    def __str__(self) -> str:
        return f"{self.name} ({self.phone_number})" + (f" - {str(self.order)}" if self.order else "")
