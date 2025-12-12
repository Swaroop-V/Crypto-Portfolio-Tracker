from django.db import models

# Create your models here.

class Asset(models.Model):
    symbol = models.CharField(max_length=10) # e.g., 'bitcoin'
    quantity = models.FloatField() # e.g., 0.5
    purchase_price = models.FloatField() # Price you bought it at
    
    
    def __str__(self):
        return f"{self.symbol} - {self.quantity}"