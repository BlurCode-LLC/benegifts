from math import ceil

from .forms import ContactForm
from .models import Category


def get_context_data():
    categories = Category.objects.filter(parent_category__isnull=True).order_by("id")
    sub_categories_dict = {}
    for category in categories:
        sub_categories = category.sub_categories.order_by("id")
        length = sub_categories.count()
        sub_categories_dict[category.slug] = [sub_categories[0 : ceil(length / 2)], sub_categories[ceil(length / 2) : length]]
    contact_form = ContactForm()
    return {
        'categories': categories,
        'sub_categories_dict': sub_categories_dict,
        'contact_form': contact_form
    }
