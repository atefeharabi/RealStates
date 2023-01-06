from django.db import models
from users.models import User, House, Apartment, Shop


# Create your models here.
class Contract(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contract_owner',
                              verbose_name='Owner')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contract_tenant',
                               verbose_name='Tenant/Buyer')
    contract_date = models.DateField('Contract Date', auto_now=True)
    expire = models.DateField('Expire Date', default=None)
    h_fk = models.ForeignKey(House, on_delete=models.CASCADE, null=True, verbose_name='House ID')
    A_fk = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True, verbose_name='Apartment ID')
    s_fk = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, verbose_name='Shop ID')

