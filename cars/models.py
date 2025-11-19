from django.db import models

class TBCars(models.Model):
    carname = models.TextField()
    carbrand = models.TextField()
    carmodel = models.TextField()
    carprice = models.TextField()

    class Meta:
        db_table = 'TBCars'

    def __str__(self):
        return self.carname
