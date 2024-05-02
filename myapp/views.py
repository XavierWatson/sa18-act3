from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

def get_products(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products':products})
def show_product(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request, 'myapp/show.html', {'product':product})
# Create your views here.
