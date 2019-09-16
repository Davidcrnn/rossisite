from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='images/', default=True)

    def __str__(self):
        return self.name

    def get_products(self):
     return Product.objects.filter(project__name=self.name)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name= 'products')
    date_creation = models.DateTimeField(auto_now_add=False, blank=True)
    image = models.FileField(upload_to='images/', default=False)
    image2 = models.FileField(upload_to='images/', default=False)
    image3 = models.FileField(upload_to='images/', default=False)
    visible_home = models.BooleanField(default=False)

    def __str__(self):
        return self.name

