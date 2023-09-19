import requests
from django.shortcuts import render

from .forms import CurrencyConverterForm


def convert_currency(request):
    if request.method == 'POST':
        form = CurrencyConverterForm(request.POST)
        if form.is_valid():
            amount_in_usd = float(form.cleaned_data['amount_in_usd'])

            api_url = f'https://openexchangerates.org/api/latest.json?app_id=b2fe78ad3a544496adc31b52bd50d6c9'
            response = requests.get(api_url)

            if response.status_code == 200:
                data = response.json()
                exchange_rates = data['rates']

                converted_currencies = {
                    'RUB': amount_in_usd * exchange_rates['RUB'],
                    'BYN': amount_in_usd * exchange_rates['BYN'],
                    'UAH': amount_in_usd * exchange_rates['UAH'],
                    'PLN': amount_in_usd * exchange_rates['PLN'],
                    'JPY': amount_in_usd * exchange_rates['JPY'],
                }
            else:
                converted_currencies = None
    else:
        form = CurrencyConverterForm()
        converted_currencies = None

    context = {'form': form, 'converted_currencies': converted_currencies}
    return render(request, 'convert_currency.html', context)

# https://api.exchangeratesapi.io/v1/latest?base=USD?access_key = b2fe78ad3a544496adc31b52bd50d6c9
# https://openexchangerates.org/api/latest.json&base=USD?app_id=b2fe78ad3a544496adc31b52bd50d6c9
# http://api.exchangeratesapi.io/latest.json?base=RUB?app_id=b2fe78ad3a544496adc31b52bd50d6c9
# https://openexchangerates.org/api/latest.json?app_id=b2fe78ad3a544496adc31b52bd50d6c9 рабочая ссылка
# https://openexchangerates.org/api/latest.json?app_id=b2fe78ad3a544496adc31b52bd50d6c9&base=RUB
