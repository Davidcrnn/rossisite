from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic   import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, Project

# Create your views here.

# uniquement pour mail
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

class HomePageView(TemplateView):
    template_name= 'home.html'
    model = Product

    def get(self, request):
         series = Product.objects.all()
         visible = series.filter(visible_home=True)
         stu = {"product_name": series}
         return render(request, 'home.html', stu)


class ProjectListView(ListView):
    model = Project
    template_name = "project_index.html"
    context_object_name = 'products_list'


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project_detail.html"

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(Project, id=id_)

class ProductListView(ListView):
    model = Product
    template_name = 'product.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_object(self):
        id_= self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)



class ContactView(TemplateView):
    template_name= 'contact.html'






def error_404(request):
        data = {}
        return render(request,'pages/error_404.html', data)

def error_500(request):
        data = {}
        return render(request,'pages/error_500.html', data)