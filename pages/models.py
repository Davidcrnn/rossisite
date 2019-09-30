from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.FileField(upload_to='images/', default=True)

    def __str__(self):
        return self.name

    def get_products(self):
     return Product.objects.filter(project__name=self.name)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name= 'products')
    date_creation = models.DateField(auto_now_add=False, blank=True, null=True)
    image = models.FileField(upload_to='images/')
    image2 = models.FileField(upload_to='images/', null=True, blank=True)
    image3 = models.FileField(upload_to='images/', null=True, blank=True)
    visible_home = models.BooleanField(default=True)

    def __str__(self):
        return self.name

