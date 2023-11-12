from django.db import models

from userlogin.models import *
from products.models import *
from cart.models import *
import uuid

# Define the Orders model


# Model for the Combined order from the cart
class Orders(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    expected_delivery_date = models.DateField(null=True, blank=True)
    delivered_date = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.user.fullname}'s Order | ID : {self.order_id}"
    

# Define the OrdersItem model
# Model for the Each items in the Orders Model
class OrdersItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    variant = models.ForeignKey(ColorVarient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="Order confirmed")


    def total_price(self): # To Calculate the price * Quantity and provide the total price
        return self.quantity * self.price


    def __str__(self) :
        return f"{self.variant.product.name}'s {self.variant.color} order - {self.quantity} item(s) | ID : {self.order.order_id}"

