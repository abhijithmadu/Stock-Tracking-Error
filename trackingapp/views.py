from django.http.response import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

def sample(request):
    key = 'd2f6235ac39c5e90926f6c12ac5d9209'
    params = {
        'access_key': key
            }

    present_etf = requests.get('https://api.marketstack.com/v1/tickers/SETFNN50.XNSE/eod/latest',params)
    sbi_present_etf=present_etf.json()['close']
    print(sbi_present_etf)

    previous_etf = requests.get('http://api.marketstack.com/v1/tickers/SETFNN50.XNSE/eod/2021-03-09',params)
    sbi_previous_etf=previous_etf.json()['close']
    print(sbi_previous_etf)

    present_nifty = requests.get('https://api.marketstack.com/v1/tickers/NN50.INDX/eod/latest',params)
    sbi_present_nifty = present_nifty.json()['close']
    print(sbi_present_nifty)
    
    previous_nifty = requests.get('http://api.marketstack.com/v1/tickers/NN50.INDX/eod/2021-03-09', params)
    sbi_previous_nifty = previous_nifty.json()['close']
    print(sbi_previous_nifty)


    sbi_diff = sbi_present_etf/sbi_previous_etf-1
    nifty_diff = sbi_present_nifty/sbi_previous_nifty-1

    tracking_error = abs((sbi_diff-nifty_diff)*100)
    print(tracking_error)
    context = {
        'tracking_error':tracking_error
    }
    return render(request,"tracking.html",context)


