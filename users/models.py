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
    alley = models.CharField('Alley', max_length=50, null=True)
    number = models.CharField('No', max_length=50, null=True)
    floor = models.CharField('Floor', max_length=50, null=True)
    unit = models.CharField('Unit', max_length=50, null=True)


class User(models.Model):
    f_name = models.CharField('First Name', max_length=100)
    l_name = models.CharField('Last Name', max_length=100)
    email = models.EmailField('Email', max_length=100)
    id_number = models.CharField('National Number', max_length=10, validators=[MinLengthValidator(10)],
                                 help_text='10 digit number')
    mobile = models.CharField('Mobile', max_length=10, validators=[MinLengthValidator(10)],
                              help_text='10 digit number without 0 at first')
    phone = models.CharField('Phone', max_length=10, validators=[MinLengthValidator(10)], help_text='10 digit number')
    image = models.ImageField('Profile Image', upload_to='images/users', default='images/users/default.jpg')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Apartment(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='a_owner')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='a_tenant')
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
    price = models.FloatField('Price', null=True)
    Mortgage_price = models.FloatField('Mortgage Price', null=True)
    rent_price = models.FloatField('Rent Price', null=True)


class House(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='h_owner')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='h_tenant')
    num_room = models.IntegerField('Number of Rooms')
    area = models.FloatField('Area(m2)')
    phone = models.BooleanField('Phone')
    parking = models.BooleanField('Parking')
    pool = models.BooleanField('Pool')
    contract_type = models.CharField('Contract Type', max_length=1,
                                     choices=[('m', 'Mortgage'), ('r', 'Rent'), ('s', 'Sale')])
    price = models.FloatField('Price', null=True)
    Mortgage_price = models.FloatField('Mortgage Price', null=True)
    rent_price = models.FloatField('Rent Price', null=True)


class Shop(models.Model):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sh_owner')
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sh_tenant')
    area = models.FloatField('Area(m2)')
    phone = models.BooleanField('Phone')
    parking = models.BooleanField('Parking')
    contract_type = models.CharField('Contract Type', max_length=1,
                                     choices=[('m', 'Mortgage'), ('r', 'Rent'), ('s', 'Sale')])
    price = models.FloatField('Price', null=True)
    Mortgage_price = models.FloatField('Mortgage Price', null=True)
    rent_price = models.FloatField('Rent Price', null=True)
