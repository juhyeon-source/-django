from django.shortcuts import render

def product_list(request):
    return render(request, 'product_list.html')
