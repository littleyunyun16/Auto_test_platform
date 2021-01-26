# Create your views here.
from django.shortcuts import render
from apps.Module.models import Product
def product_manage(request):
    username=request.session.get('user','')
    prduct_list=Product.objects.all()
    return render(request, "product_manage.html", {"user":username, "products":prduct_list})
