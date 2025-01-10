from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Product,Order,Client,Review
from .forms import ProductForm,OrderForm,ClientForm,ReviewForm




class ProductListView(View):
    def get(self, request):
        products=Product.objects.filter(supplier=request.user)
        return render(request,'product_list.html',{'products':products})




class ProductCreateView(View):
    def get(self,request):
        form=ProductForm()
        return render(request,'product_form.html',{'form':form})
    
    def Post(self,request):
        form=ProductForm(request.POST)
        if form.is_valid():
            product=form.save(commits=False)
            product.supplier=request.user
            product.save()
            return JsonResponse({'sucess':True,'product_id':product.id})
        return JsonResponse({'scuess':False,'errors':form.errors})


class OrderListView(View):
    def get(self, request):
        orders=Order.objects.filter(product__supplier=reques.user)
        return render(request,'order_list.html',{'orders':orders})
    

class OrderUpdateView(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return JsonResponse({'sucess':True,'order_id':order.id})
        return JsonResponse({'sucess':False,'errors':form.errors})

    def post(self,request,pk):
        order=get_object_or_404(Order,pk=pk)
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return JsonResponse({'sucess':True,'order_id':order.id})
        return JsonResponse({'sucess':False,'errors':form.errors})


class ClientListView(View):
    def get(self, request):
        clients = Client.objects.filter(sales_representative=request.user)
        return render(request, 'clients/client_list.html', {'clients': clients})

class ClientCreateView(View):
    def get(self, request):
        form = ClientForm()
        return render(request, 'clients/client_form.html', {'form': form})

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.sales_representative = request.user
            client.save()
            return JsonResponse({'success': True, 'client_id': client.id})
        return JsonResponse({'success': False, 'errors': form.errors})

class ClientOrderView(View):
    def get(self, request):
        clients = Client.objects.filter(sales_representative=request.user)
        orders = Order.objects.filter(product__supplier=request.user)
        return render(request, 'clients/client_orders.html', {'clients': clients, 'orders': orders})



class ReviewListView(View):
    def get(self,request,product_id):
        product=get_object_or_404(Product,id=product_id)
        reviews=product.reviews.all()
        return render(request,'review_list.html',{'reviews':reviews,'product_id':product_id})


class ReviewCreateView(View):
    def get(self, request, product_id):
        form=ReviewForm()
        return render(request,'review.html',{'form':form,'product_id':product_id})
    


    def post(self,request,product_id):
        product=get_object_or_404(Product,id=product_id)
        form=ReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.product=product
            review.client=request.user.clients.first()
            review.save()
            return JsonResponse({'sucess':True,'review_id':review.id})
        return JsonResponse({'sucess':False,'errors':form.errors})


