from django.contrib import admin
from django.contrib.auth.models import (
    Group,
    User
)

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


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductColor)
admin.site.register(News)
admin.site.register(LogoLayOn)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone_number",
        "type"
    )

    def has_add_permission(self, request, obj=None) -> bool:
        return False
    
    def has_change_permission(self, request, obj=None) -> bool:
        return False
