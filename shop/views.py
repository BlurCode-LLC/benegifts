from django.shortcuts import (
    get_object_or_404,
    render
)
from os import listdir

from .models import (
    Category,
    News,
    Product
)
from .utils import get_context_data


def index(request):
    context_data = get_context_data()
    categories = context_data['categories']
    categories_for_index_page = [categories[i : i + 6] for i in range(0, len(categories), 6)]
    news = News.objects.all()[:5]
    sponsors = [f"img/sponsors/{item}" for item in listdir("static/img/sponsors")]
    brands = [f"img/brands/{item}" for item in listdir("static/img/brands")]
    return render(request, "shop/index.html", {
        **context_data,
        'categories_for_index_page': categories_for_index_page,
        'news': news,
        'sponsors': sponsors,
        'brands': brands
    })


def benedict(request):
    return render(request, "shop/benedict.html", {
        **get_context_data()
    })


def benetex(request):
    return render(request, "shop/benetex.html", {
        **get_context_data()
    })


def logo_lay_on(request):
    return render(request, "shop/logo_lay_on.html", {
        **get_context_data()
    })


def category_detail(request, slug):
    category: Category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, "shop/category.html", {
        **get_context_data(),
        'category': category,
        'products': category.products.all()
    })


def product_detail(request, slug):
    product: Product = get_object_or_404(Product, slug=slug)
    return render(request, "shop/product.html", {
        **get_context_data(),
        'product': product
    })


def news_detail(request, slug):
    new: News = get_object_or_404(News, slug=slug)
    news = News.objects.exclude(id=new.id)[:5]
    return render(request, "shop/news.html", {
        **get_context_data(),
        'new': new,
        'news': news
    })
