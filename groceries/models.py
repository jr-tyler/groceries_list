from django.db import models
from django.utils import timezone

# Create your models here.
class Grocery(models.Model):
    person = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    bought_date = models.DateTimeField(default=timezone.now)
    paid_date = models.DateTimeField(blank=True, null=True)

    def paid(self):
        self.paid_date = timezone.now()
        self.save()

    # instead of displaying the objects as numbers it returns the item label as the descriptor
    def __str__(self):
        return self.item + ' bought by ' + str(self.person)
