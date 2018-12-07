from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

from .models import Grocery, PiggyTopUp
from groceries.forms import GroceryForm, PiggyForm

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
    groceries = Grocery.objects.filter(person_id=person_id).order_by('-paid_date')
    person = groceries[0].person
    outstanding_groceries = Grocery.objects.filter(person=person).filter(paid_date__isnull=True).order_by('-bought_date')
    total = 0
    for grocery in outstanding_groceries:
        total += grocery.cost
    stuff_for_front_end = {'groceries': groceries, 'person': person, 'total': total}
    return render(request, 'groceries/purchaser.html', stuff_for_front_end)


# shows a list of all groceries bought by a person when their username is clicked
@ login_required
def user_purchaser_list(request):
    groceries = Grocery.objects.filter(person=request.user).order_by('-bought_date')
    person = 'you'
    outstanding_groceries = Grocery.objects.filter(person=request.user).filter(paid_date__isnull=True).order_by('-bought_date')
    total = 0
    for grocery in outstanding_groceries:
        total += grocery.cost
    stuff_for_front_end = {'groceries': groceries, 'person': person, 'total': total}
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
            if grocery.cost == 0.00:
                grocery.paid_date = timezone.now()
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
    length_list = len(groceries)
    total = 0
    for grocery in groceries:
        total += grocery.cost
    stuff_for_front_end = {'groceries': groceries, 'total': total, 'length_list': length_list}
    return render(request, 'groceries/piggy_page.html', stuff_for_front_end)


@ login_required
def piggy_top_up(request):
    if request.method == 'POST':
        # updating an existing form
        form = PiggyForm(request.POST)
        if form.is_valid():
            piggytopup = form.save(commit=False)
            piggytopup.person = request.user
            piggytopup.save()
            return redirect('piggy_top_up_list')

    else:
        form = PiggyForm()
        stuff_for_front_end = {'form': form}
        return render(request, 'groceries/piggy_top_up.html', stuff_for_front_end)


@login_required
def piggy_top_up_list(request):
    piggy_top_ups = PiggyTopUp.objects.all().order_by('-added_date')
    piggy_total = 0
    for piggy_top_up in piggy_top_ups:
        piggy_total += piggy_top_up.amount
    stuff_for_front_end = {'piggy_top_ups': piggy_top_ups, 'piggy_total': piggy_total}
    return render(request, 'groceries/piggy_top_up_list.html', stuff_for_front_end)


# shows a list of all of the groceries bought on a specific date
@ login_required
def bought_date_list(request, bought_date):
    groceries = Grocery.objects.filter(bought_date=bought_date).order_by('person')
    stuff_for_front_end ={'groceries': groceries, 'bought_date': bought_date}
    return render(request, 'groceries/bought_date_list.html', stuff_for_front_end)


# allows the user to edit an item that they bought
@ login_required
def edit_item(request, pk):
    grocery = get_object_or_404(Grocery, pk=pk)
    item = grocery.item
    if grocery.person == request.user:
        if request.method == 'POST':

            # updating an existing form
            form = GroceryForm(request.POST, instance=grocery)
            if form.is_valid():
                grocery = form.save(commit=False)
                if grocery.cost == 0.00:
                    grocery.paid_date = timezone.now()
                grocery.save()
                return redirect('grocery_list')

        else:
            form = GroceryForm(instance=grocery)
            stuff_for_frontend = {'form': form, 'grocery': grocery}
        return render(request, 'groceries/edit_item.html', stuff_for_frontend)

    else:
        message = "Oops!  It doesn't look like you bought " + item.upper() + "..."
        stuff_for_frontend = {'message': message, 'grocery': grocery}
        return render(request, 'groceries/edit_item.html', stuff_for_frontend)

# allows a user to delete an item
@login_required
def delete_item(request, pk):
    grocery = get_object_or_404(Grocery, pk=pk)
    grocery.delete()
    return redirect('/', pk=grocery.pk)


# allows the user to edit an item that they bought
@ login_required
def edit_reason(request, pk):
    piggy_top_up = get_object_or_404(PiggyTopUp, pk=pk)
    reason = piggy_top_up.reason
    if piggy_top_up.person == request.user:
        if request.method == 'POST':

            # updating an existing form
            form = PiggyForm(request.POST, instance=piggy_top_up)
            if form.is_valid():
                piggy_top_up = form.save(commit=False)
                piggy_top_up.save()
                return redirect('piggy_top_up_list')

        else:
            form = PiggyForm(instance=piggy_top_up)
            stuff_for_frontend = {'form': form, 'piggy_top_up': piggy_top_up}
        return render(request, 'groceries/edit_reason.html', stuff_for_frontend)

    else:
        message = "Whoa there amigo/amiga   !  It doesn't look like you added this one to the piggy bank..."
        stuff_for_frontend = {'message': message}
        return render(request, 'groceries/edit_reason.html', stuff_for_frontend)

# allows a user to delete an item
@login_required
def delete_reason(request, pk):
    piggy_top_up = get_object_or_404(PiggyTopUp, pk=pk)
    piggy_top_up.delete()
    return redirect('/groceries/piggy_top_up_list', pk=piggy_top_up.pk)

@login_required
def item_claim(request, pk):
    grocery = get_object_or_404(Grocery, pk=pk)
    grocery.paid()
    return redirect('piggy_page')