from django.contrib import admin
from .models import Reservation_Rest,Drinks_Item,FastFood_Item,Food_Item,Order_secondary,Order_main
# Register your models here.


admin.site.register(Reservation_Rest);
admin.site.register(Drinks_Item);
admin.site.register(FastFood_Item);
admin.site.register(Food_Item);
admin.site.register(Order_main);
admin.site.register(Order_secondary);