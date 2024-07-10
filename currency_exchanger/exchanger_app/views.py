from django.shortcuts import render
import requests
from currency_exchanger.settings import API_KEY
# from .models


def exchanger(request):
    url = 'http://data.fixer.io/api/latest?access_key=' + API_KEY
    currencies = requests.get(url).json().get('rates')

    if request.method == 'POST':
        amount = request.POST.get('amount')
        from_value = request.POST.get('from_value')
        to_value = request.POST.get('to_value')
        result = round((currencies[to_value] / currencies[from_value]) * float(amount), 2)
        context = {
            'currencies': currencies,
            'result': result,
            'from_value': from_value,
            'to_value': to_value,
            'amount': amount,
        }
        return render(request, 'exchanger_app/index.html', context)
    else:
        context = {
            'currencies': currencies,
        }
        return render(request, 'exchanger_app/index.html', context)
