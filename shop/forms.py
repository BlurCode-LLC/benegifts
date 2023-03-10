from django.contrib.admin.widgets import AdminTextInputWidget
from django.forms import (
    ModelForm,
    NumberInput,
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = TextInput(attrs={'placeholder': "Ваше имя"})
        self.fields['phone_number'].widget = TextInput(attrs={'placeholder': "Номер телефона"})
        self.fields['order'].widget = NumberInput(attrs={'style': "display: none;"})


class ProductColorAdminForm(ModelForm):

    class Meta:
        model = ProductColor
        fields = "__all__"
        widgets = {
            'color': AdminTextInputWidget(attrs={'type': "color"})
        }
