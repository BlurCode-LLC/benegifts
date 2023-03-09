from django.contrib.admin.widgets import AdminTextInputWidget
from django.forms import (
    CharField,
    ModelForm,
    TextInput
)

from .models import (
    Contact,
    ProductColor
)


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        exclude = (
            "type",
            "datetime"
        )
        widget = {
            'name': TextInput(attrs={'placeholder': "Ваше имя"})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = TextInput(attrs={'placeholder': "Ваше имя"})
        self.fields['phone_number'].widget = TextInput(attrs={'placeholder': "Номер телефона"})


class ProductColorAdminForm(ModelForm):

    class Meta:
        model = ProductColor
        fields = "__all__"
        widgets = {
            'color': AdminTextInputWidget(attrs={'type': "color"})
        }
