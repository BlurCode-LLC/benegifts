from django.shortcuts import (
    get_object_or_404,
    redirect,
    render
)
from math import ceil
from os import listdir

from .forms import ContactForm
from .models import (
    Category,
    LogoLayOn,
    News,
    Product
)
from .utils import get_context_data


def index(request):
    context_data = get_context_data()
    categories = context_data['categories']
    categories_for_index_page = [categories[i : i + 6] for i in range(0, len(categories), 6)]
    news = News.objects.all()[:3]
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
    logo_lay_ons = LogoLayOn.objects.all()
    length = logo_lay_ons.count()
    logo_lay_ons = [logo_lay_ons[0 : ceil(length / 2)], logo_lay_ons[ceil(length / 2) : length]]
    return render(request, "shop/logo_lay_on.html", {
        **get_context_data(),
        'logo_lay_ons': logo_lay_ons
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
        'product': product,
        'order_form': ContactForm(initial={'order': product.id})
    })


def news_detail(request, slug):
    new: News = get_object_or_404(News, slug=slug)
    news = News.objects.exclude(id=new.id)[:3]
    return render(request, "shop/news.html", {
        **get_context_data(),
        'new': new,
        'news': news
    })


def form(request, type):
    form = ContactForm(request.POST)
    contact = form.save(commit=False)
    contact.type = type
    contact.save()
    return redirect(request.META.get('HTTP_REFERER') or "shop:index")
