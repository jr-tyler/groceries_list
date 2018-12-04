from django.contrib import admin
from .models import Grocery, PiggyTopUp, PiggyPaid

# Register your models here.
admin.site.register(Grocery)
admin.site.register(PiggyTopUp)
admin.site.register(PiggyPaid)