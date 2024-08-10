from django.forms import ModelForm, forms

from catalog.models import Product


ban_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
class ProductForm(ModelForm):
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