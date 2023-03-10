from django.contrib import admin
from django.contrib.auth.models import (
    Group,
    User
)
from django.utils.safestring import mark_safe

from .forms import ProductColorAdminForm
from .models import *


admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "parent_category",
        "slug"
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent_category":
            kwargs["queryset"] = Category.objects.filter(parent_category__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "product_category",
        "slug"
    )

    @admin.display
    def product_category(self, obj):
        return ", ".join(str(category) for category in obj.category.all())

    product_category.short_description = "Категории"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(parent_category__isnull=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "product_image"
    )

    @admin.display
    def product_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' style='height: 50px;'>")

    product_image.short_description = "Фото"

@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "product_color"
    )

    form = ProductColorAdminForm

    @admin.display
    def product_color(self, obj):
        return mark_safe(f"<div style='width: 20px; height: 20px; background-color: {obj.color};'></div>")

    product_color.short_description = "Цвет"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone_number",
        "type",
        "order"
    )

    def has_add_permission(self, request, obj=None) -> bool:
        return False
    
    def has_change_permission(self, request, obj=None) -> bool:
        return False

admin.site.register(News)
admin.site.register(LogoLayOn)
