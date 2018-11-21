from django.shortcuts import render
from django.utils import timezone
from .models import Grocery

# Create your views here.
def grocery_list(request):
    groceries = Grocery.objects.filter(bought_date__lte=timezone.now()).order_by('-bought_date')
    stuff_for_front_end = {'groceries': groceries}
    return render(request, 'groceries/groceries_list.html', stuff_for_front_end)