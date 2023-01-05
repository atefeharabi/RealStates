from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Address(models.Model):
    postal_code = models.CharField('Postal Code', max_length=10, unique=True, validators=[MinLengthValidator(10)],
                                   help_text='10 digit number')
    country = models.CharField('Country', max_length=50)
    district = models.CharField('District', max_length=50)
    city = models.CharField('City', max_length=50)
    street = models.CharField('Street', max_length=50)
    alley = models.CharField('Alley', max_length=50, null=True, blank=True)
    number = models.CharField('No', max_length=50, null=True, blank=True)
    floor = models.CharField('Floor', max_length=50, null=True, blank=True)
    unit = models.CharField('Unit', max_length=50, null=True, blank=True)


class User(models.Model):
    f_name = models.CharField('First Name', max_length=100)
    l_name = models.CharField('Last Name', max_length=100)
    email = models.EmailField('Email', max_length=100)
    id_number = models.CharField('National Number', max_length=10, validators=[MinLengthValidator(10)],
                                 help_text='10 digit number')
    mobile = models.CharField('Mobile', max_length=10, validators=[MinLengthValidator(10)],
                              help_text='10 digit number without 0 at first')
    phone = models.CharField('Phone', max_length=10, validators=[MinLengthValidator(10)], help_text='10 digit number')
    image = models.ImageField('Profile Image', upload_to='static/images/users/', default='images/users/default.jpg')
    # Adrese mahale sokonate karbar
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Apartment(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='a_owner')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='a_tenant', null=True, blank=True)
    num_room = models.IntegerField('Number of Rooms')
    area = models.FloatField('Area(m2)')

    # total floor for apartment
    story = models.IntegerField('Story')
    phone = models.BooleanField('Phone')
    parking = models.BooleanField('Parking')
    elevator = models.BooleanField('Elevator')
    pool = models.BooleanField('Pool')
    contract_type = models.CharField('Contract Type', max_length=1,
                                     choices=[('m', 'Mortgage'), ('r', 'Rent'), ('s', 'Sale')])
    price = models.FloatField('Price', null=True, blank=True)
    Mortgage_price = models.FloatField('Mortgage Price', null=True, blank=True)
    rent_price = models.FloatField('Rent Price', null=True, blank=True)
    image = models.ImageField('Apartment Image', upload_to='static/images/apartments/', default='images/apartments/default.jpg',
                              null=True, blank=True)


class House(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='h_owner')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='h_tenant', null=True, blank=True)
    num_room = models.IntegerField('Number of Rooms')
    area = models.FloatField('Area(m2)')
    phone = models.BooleanField('Phone')
    parking = models.BooleanField('Parking')
    pool = models.BooleanField('Pool')
    contract_type = models.CharField('Contract Type', max_length=1,
                                     choices=[('m', 'Mortgage'), ('r', 'Rent'), ('s', 'Sale')])
    price = models.FloatField('Price', null=True, blank=True)
    Mortgage_price = models.FloatField('Mortgage Price', null=True, blank=True)
    rent_price = models.FloatField('Rent Price', null=True, blank=True)
    image = models.ImageField('House Image', upload_to='static/images/houses/', default='images/houses/default.jpg',
                              null=True, blank=True)


class Shop(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sh_owner')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sh_tenant', blank=True, null=True)
    area = models.FloatField('Area(m2)')
    phone = models.BooleanField('Phone')
    parking = models.BooleanField('Parking')
    contract_type = models.CharField('Contract Type', max_length=1,
                                     choices=[('m', 'Mortgage'), ('r', 'Rent'), ('s', 'Sale')])
    price = models.FloatField('Price', null=True, blank=True)
    Mortgage_price = models.FloatField('Mortgage Price', null=True, blank=True)
    rent_price = models.FloatField('Rent Price', null=True, blank=True)
    image = models.ImageField('Shop Image', upload_to='static/images/shops/', default='images/shops/default.jpg',
                              null=True, blank=True)