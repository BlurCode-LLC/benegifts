from django.contrib import admin
from django.contrib.auth.models import (
    Group,
    User
)

from .models import *


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductColor)
admin.site.register(News)
