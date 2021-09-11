from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from decouple import config

def sample(request):
    #API access key
    key =config('secret_key')
    params = {
        'access_key': key
            }

    
    #collect sbi etf values
    present_etf = requests.get('https://api.marketstack.com/v1/tickers/SETFNN50.XNSE/eod/latest',params)
    sbi_present_etf=present_etf.json()['close']
    
    previous_etf = requests.get('http://api.marketstack.com/v1/tickers/SETFNN50.XNSE/eod/2021-03-09',params)
    sbi_previous_etf=previous_etf.json()['close']
    
    #collect sbi nifty values
    present_nifty = requests.get('https://api.marketstack.com/v1/tickers/NN50.INDX/eod/latest',params)
    sbi_present_nifty = present_nifty.json()['close']
    
    previous_nifty = requests.get('http://api.marketstack.com/v1/tickers/NN50.INDX/eod/2021-03-09', params)
    sbi_previous_nifty = previous_nifty.json()['close']
    

    #tracking error calculation
    sbi_diff = sbi_present_etf/sbi_previous_etf-1
    nifty_diff = sbi_present_nifty/sbi_previous_nifty-1

    tracking_error = abs((sbi_diff-nifty_diff)*100)
    
    context = {
        'tracking_error':tracking_error
    }
    return render(request,"tracking.html",context)


