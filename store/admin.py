from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('category', 'price')

admin.site.site_header = "Amyra's Crochet Studio Admin"
admin.site.site_title = "Amyra's Crochet Studio"
admin.site.index_title = "Inventory & Product Management"
