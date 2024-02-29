from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db.models import Avg


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class FlowerCount(models.Model):
    name = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return str(self.name)

def field_validation(value):
    """Function to validatate rating"""

    if value == 0:
        raise ValidationError(
            ('The value should be greater than zero'),
            params={'value': value},
        )

class Product(models.Model):
    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    flower_count = models.ForeignKey(
        'FlowerCount', on_delete=models.PROTECT, related_name='count')
    has_flower_count = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def average_rating(self) -> float:
        return Rating.objects.filter(product_rating_id=self).aggregate(Avg("rating"))["rating__avg"] or 0


class Rating(models.Model):
    """
    A rating model to rate product by users
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    product_rating = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.FloatField(
        blank=False,
        default=0,
        validators=[field_validation, MaxValueValidator(5.0)])

    def __str__(self):
        return f"{self.rating}"