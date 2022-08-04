from django.db import models


class Price(models.Model):
    price_id = models.AutoField(primary_key=True)
    market = models.CharField(max_length=100, blank=True, null=True)
    name_coin = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    # created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'price'
        unique_together = (('market', 'name_coin'),)
