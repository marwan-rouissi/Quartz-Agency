from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    prompt      = models.TextField(blank=True, null=True)
    image_generator  = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"