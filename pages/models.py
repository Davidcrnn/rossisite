from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_products(self):
     return Product.objects.filter(project__name=self.name)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name= 'products')
    image = models.FileField(upload_to='images/', default=False)
    def __str__(self):
        return self.name