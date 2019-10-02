from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.detail import DetailView
from .views import ProjectListView, ProjectDetailView, ProductListView, ProductDetailView, HomePageView, ContactView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("about/", TemplateView.as_view(template_name= "about.html"), name="about"),
    path("mentions/", TemplateView.as_view(template_name= "mentions.html"), name="mentions"),
    path("projects/", ProjectListView.as_view(), name='projects'),
    path("projects/<int:id>/", ProjectDetailView.as_view(), name='project-detail'),
    path('products/', ProductListView.as_view(), name = 'products'),
    path('products/<int:id>', ProductDetailView.as_view(), name='product-detail'),
    path('contact/', ContactView.as_view(), name='contact'),

]





urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)