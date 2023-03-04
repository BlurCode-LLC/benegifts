from django.urls import path
from shop import views

app_name = "shop"


urlpatterns = [
    path("", views.index, name="index"),
    path("benedict/", views.benedict, name="benedict"),
    path("benetex/", views.benetex, name="benetex"),
    path("logo-lay-on/", views.logo_lay_on, name="logo_lay_on"),
    path("category/<slug:slug>", views.category_detail, name="category"),
    path("product/<slug:slug>", views.product_detail, name="product"),
    path("news/<slug:slug>", views.news_detail, name="news"),
]
