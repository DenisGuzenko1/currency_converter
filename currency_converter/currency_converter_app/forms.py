from django import forms

class CurrencyConverterForm(forms.Form):
    amount_in_usd = forms.DecimalField(label='Сумма в долларах', max_digits=10, decimal_places=2)
