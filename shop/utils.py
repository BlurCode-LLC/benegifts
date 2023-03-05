from .models import Category


def get_context_data():
    categories = Category.objects.filter(parent_category__isnull=True).order_by("id")
    sub_categories_dict = { category.slug: category.sub_categories.order_by("id") for category in categories }
    return {
        'categories': categories,
        'sub_categories_dict': sub_categories_dict
    }
