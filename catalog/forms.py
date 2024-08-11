from django.forms import ModelForm, forms

from catalog.models import Product, Version

ban_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name,  field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("__all__")

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]

        if cleaned_data in ban_list:
            for word in ban_list:
                if word in cleaned_data.lower():
                    raise forms.ValidationError(f"В названии продукта нельзя использовать запрещенные слово {word}.")

        return cleaned_data


    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]

        if cleaned_data in ban_list:
            for word in ban_list:
                if word in cleaned_data.lower():
                    raise forms.ValidationError(
                        f"В описании продукта нельзя использовать запрещенные слово {word}.")

        return cleaned_data

class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = ("__all__")


