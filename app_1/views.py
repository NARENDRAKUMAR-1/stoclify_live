from django.shortcuts import render

from yahoo_fin.stock_info import *

# Create your views here.

def stockPicker(request):

    stock_picker = tickers_nifty50()
    print(stock_picker)
    return render(request, 'stockPicker.html', {'stock_picker':stock_picker} )

def stocktracker(request):

    stockpicker1 = request.GET.getlist('stockpicker1')
    # now we got selected stocks

    print(stockpicker1)

    data = {}

    available_stocks = tickers_nifty50()

    for i in stockpicker1:
        if i in available_stocks:
            pass
        else:
            return HttpResponse("Error")
        
    for i in stockpicker1:
        details = get_quote_table(i)
        data.update({i: details})

    print(data)


    return render(request, 'stocktracker.html', {'data':data})