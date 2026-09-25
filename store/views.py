from django.shortcuts import render
from .models import Product

def home(request):
    selected_category = request.GET.get('category', 'all')
    if selected_category and selected_category != 'all':
        products = Product.objects.filter(category=selected_category).order_by('-created_at')
    else:
        products = Product.objects.all().order_by('-created_at')
    
    return render(request, 'store/index.html', {
        'products': products,
        'selected_category': selected_category
    })
