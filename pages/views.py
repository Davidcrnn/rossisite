from django.shortcuts import render, get_object_or_404
from django.views.generic   import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, Project
# Create your views here.

class HomePageView(TemplateView):
    template_name= 'home.html'
    model = Product

    def get(self, request):
         series = Product.objects.all()
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