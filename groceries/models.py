from django.db import models
from django.utils import timezone

# Create your models here.
class Grocery(models.Model):
    person = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    bought_date = models.DateField(default=timezone.now)
    paid_date = models.DateField(blank=True, null=True)

    # a method to create the paid date --> to be run when the button is pressed
    def paid(self):
        self.paid_date = timezone.now()
        self.save()

    # instead of displaying the objects as numbers it returns the item label as the descriptor
    def __str__(self):
        return self.item + ' bought by ' + str(self.person)


class PiggyPaid(models.Model):
    item = models.ForeignKey('groceries.Grocery', on_delete=models.CASCADE, related_name='piggy_paid')
    paid_date = models.DateField(default=timezone.now)



class PiggyTopUp(models.Model):
    person = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='piggy_top_up')
    reason = models.CharField(max_length=300)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    added_date = models.DateField(default=timezone.now)

    # instead of displaying the objects as numbers it returns the item label as the descriptor
    def __str__(self):
        return self.reason + ' paid by ' + str(self.person)