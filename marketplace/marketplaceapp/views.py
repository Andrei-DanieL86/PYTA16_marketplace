from django.http import HttpResponse
from .models import Product
from django.shortcuts import get_object_or_404, render

def index(request):
	#return HttpResponse("Hello world")
	return render(request, "marketplaceapp/home.html")

def product_list(request):
	# read all products from db
	all_products = Product.objects.all()
	context = {
		"products" : all_products
	}
	print(all_products)
	#return HttpResponse("Product list")
	return render(request, "marketplaceapp/product_list.html", context)

def product_detail(request, product_id):
	# read only one product
	# product = Product.objects.get(pk=product_id) # pk vine de la primarykey
	product = get_object_or_404(Product, pk=product_id)
	print(product)
	context = {
		"product" : product
	}
	#return HttpResponse(f"Product_detail {product_id}")
	return render(request, "marketplaceapp/product_detail.html", context)