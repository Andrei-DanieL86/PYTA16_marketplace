from django.http import HttpResponse
from .models import Product
from django.shortcuts import get_object_or_404

def index(request):
	return HttpResponse("Hello world")

def product_list(request):
	# read all products from db
	all_products = Product.objects.all()
	print(all_products)
	return HttpResponse("Product list")

def product_detail(request, product_id):
	# read only one product
	# product = Product.objects.get(pk=product_id) # pk vine de la primarykey
	product = get_object_or_404(Product, pk=product_id)
	print(product)
	return HttpResponse(f"Product_detail {product_id}")