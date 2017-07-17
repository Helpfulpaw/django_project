from django.db import models

# Create your models here.
class SHIELDS (models.Model):
    SHIELD_ID = models.IntegerField( max_length=22)
    SHIELD_NAME = models.CharField( max_length=30)
 
class ENERGY_LINK (models.Model): 
    SECURITY_CODE = models.CharField( max_length=20)
    SYSTEM_ELEMENT_ID_INPUT = models.IntegerField( max_length=22)
    SYSTEM_ELEMENT_ID_OUTPUT = models.IntegerField( max_length=22)
 
class BASE_SECTORS (models.Model): 
    LATITUDE = models.IntegerField( max_length=22)
    LONGITUDE = models.IntegerField( max_length=22)
    X = models.IntegerField( max_length=22)
    Y = models.CharField( max_length=2)
 
class ENERGY_GENERATORS (models.Model): 
    GENERATOR_ID = models.IntegerField( max_length=22)
    GENERATOR_NAME = models.CharField( max_length=30)
    MAX_POWER = models.IntegerField( max_length=22)
    POWER = models.IntegerField( max_length=22)
 
class SECTOR_SHIELDS (models.Model): 
    LATITUDE = models.IntegerField( max_length=22)
    LONGITUDE = models.IntegerField( max_length=22)
    SHIELD_ID = models.IntegerField( max_length=22)
    X = models.IntegerField( max_length=22)
    Y = models.CharField( max_length=20)
 
class SYSTEM_ELEMENTS (models.Model): 
    SYSTEM_ELEMENT_ID = models.IntegerField( max_length=22)

