from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

from .models import Grocery
from groceries.forms import GroceryForm

# Create your views here.

# shows list of all groceries bought by everyone where the piggy money has not been claimed
@ login_required
def grocery_list(request):
    groceries = Grocery.objects.filter(bought_date__lte=timezone.now()).filter(paid_date__isnull=True).order_by('-bought_date')
    total = 0
    for grocery in groceries:
        total += grocery.cost
    stuff_for_front_end = {'groceries': groceries, 'total': total}
    return render(request, 'groceries/groceries_list.html', stuff_for_front_end)

# shows a list of all groceries bought by a person when clicked in the table
@ login_required
def purchaser_list(request, person_id):
    groceries = Grocery.objects.filter(person_id=person_id).order_by('-bought_date')
    stuff_for_front_end = {'groceries': groceries}
    return render(request, 'groceries/purchaser.html', stuff_for_front_end)

# shows a list of all groceries bought by a person when their username is clicked
@ login_required
def user_purchaser_list(request):
    groceries = Grocery.objects.filter(person=request.user).order_by('-bought_date')
    stuff_for_front_end = {'groceries': groceries}
    return render(request, 'groceries/purchaser.html', stuff_for_front_end)

# allows the user to add more groceries
@ login_required
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

# shows the user what groceries they haven't yet taken money from the piggy bank for
@ login_required
def piggy_page(request):
    # filter objects based on the user and if they have been paid from piggy
    groceries = Grocery.objects.filter(person=request.user).filter(paid_date__isnull=True).order_by('-bought_date')
    total = 0
    for grocery in groceries:
        total += grocery.cost
    stuff_for_front_end = {'groceries': groceries, 'total': total}
    return render(request, 'groceries/piggy_page.html', stuff_for_front_end)

# shows a list of all of the groceries bought on a specific date
@ login_required
def bought_date_list(request, bought_date):
    groceries = Grocery.objects.filter(bought_date=bought_date).order_by('-bought_date')
    stuff_for_front_end ={'groceries': groceries}
    return render(request, 'groceries/bought_date_list.html', stuff_for_front_end)

# allows the user to edit an item that they bought
@ login_required
def edit_item(request, pk):
    grocery = get_object_or_404(Grocery, pk=pk)
    if grocery.person == request.user:
        if request.method == 'POST':

            # updating an existing form
            form = GroceryForm(request.POST, instance=grocery)
            if form.is_valid():
                grocery = form.save(commit=False)
                grocery.save()
                return redirect('grocery_list')

        else:
            form = GroceryForm(instance=grocery)
            stuff_for_frontend = {'form': form, 'grocery': grocery}
        return render(request, 'groceries/edit_item.html', stuff_for_frontend)

    else:
        message = "Oops!  It doesn't look like you bought this one!"
        stuff_for_frontend = {'message': message}
        return render(request, 'groceries/edit_item.html', stuff_for_frontend)

