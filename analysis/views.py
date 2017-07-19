# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404

import requests
#from models importing 2 classes
from .models import  StockPrices, StockName

# Create your views here.	
def index(request):
    # Return index page 
    return render(request, 'index.html', {})

def lists(request):
    # Return allthe fields in the StockName model 
    posts = StockName.objects.all()
    return render(request, 'lists.html', {'posts': posts})


def post_detail(request, pk):
    """ Return stockname, stockprices, toplist into post_detail.html 
        the conditions are performing inside the try exception block."""
        
        # dict declaration
    context_dict = {}
    
    try:      
        # stock have stockname class object when the name equal to pk  and it append into dict 
        stock = StockName.objects.get(pk=pk)
        context_dict['stock_name'] = stock.name

        # stock_details have the stock_prices filter when the stock_id equal to stock and append into dict
        stocks_details = StockPrices.objects.filter(stock_id=stock)
        context_dict['stocks_details'] = stocks_details

        # filtering and sorting top 5 stock_name order by its stock_volume range and append into dict
        top = StockPrices.objects.filter(stock_id=stock).order_by('-stock_volume')[:5]  
        context_dict['top'] = top
        context_dict['stock'] = stock
    except StockName.DoesNotExist:        
        pass
    return render(request, 'post_detail.html', context_dict)

def top(request):   
    # Top 5 stock volumes generally
    top = StockPrices.objects.order_by('-stock_volume')[:5]  
    return render(request, 'top.html', {'top': top}) 

def about(request):
    return render(request, 'about.html', {})
  



