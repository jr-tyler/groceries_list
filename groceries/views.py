from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

from .models import Grocery
from groceries.forms import GroceryForm

# Create your views here.
# shows list of all groceries bought by everyone where the piggy money has not been claimed
def grocery_list(request):
    groceries = Grocery.objects.filter(bought_date__lte=timezone.now()).filter(paid_date__isnull=True).order_by('-bought_date')
    total = 0
    for grocery in groceries:
        total += grocery.cost
    stuff_for_front_end = {'groceries': groceries, 'total': total}
    return render(request, 'groceries/groceries_list.html', stuff_for_front_end)

# shows a list of all groceries bought by a person
def purchaser_list(request, person_id):
    groceries = Grocery.objects.filter(person_id=person_id).order_by('-bought_date')
    stuff_for_front_end = {'groceries': groceries}
    return render(request, 'groceries/purchaser.html', stuff_for_front_end)

def groceries_new(request):
    if request.method == 'POST':
        form = GroceryForm(request.POST)
        if form.is_valid():
            grocery = form.save(commit=False)
            grocery.person = request.user
            grocery.bought_date = timezone.now()
            grocery.save()
            return redirect('/', pk=grocery.pk)
    else:
        form = GroceryForm()
        stuff_for_front_end ={'form': form}
        return render(request, 'groceries/groceries_new.html', stuff_for_front_end)


def piggy_page(request):
    # filter objects based on the user and if they have been paid from piggy
    groceries = Grocery.objects.filter(person=request.user).filter(paid_date__isnull=True).order_by('-bought_date')
    stuff_for_front_end = {'groceries': groceries}
    return render(request, 'groceries/piggy_page.html', stuff_for_front_end)
