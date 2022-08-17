from django.contrib import admin
from .models import Product, Offer


# Django using info in this class (note naming convention) to determine how to display the list of products
class ProductAdmin(admin.ModelAdmin):
    # Columns that will be displayed for this table
    list_display = ('name', 'price', 'stock', 'image_url')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)

# <class 'products.admin.OfferAdmin'>: (admin.E108) The value of 'list_display[0]' refers to 'class', which is not
#  a callable, an attribute of 'OfferAdmin', or an attribute or method on 'products.Offer'.

