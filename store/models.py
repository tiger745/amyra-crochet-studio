from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('dolls', '🧸 Dolls & Toys'),
        ('purses', '👛 Purses & Bags'),
        ('flowers', '🌸 Flowers & Decor'),
        ('accessories', '🎀 Keychains & Accessories'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='dolls')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    whatsapp_number = models.CharField(max_length=15, default='919999999999')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"
