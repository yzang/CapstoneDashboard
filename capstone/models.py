from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Crash(models.Model):
    # CRN
    crn=models.CharField(max_length=20)
    # CRASH_YEAR
    year=models.IntegerField()
    # CRASH_MONTH
    month=models.IntegerField()
    # DAY_OF_WEEK
    day=models.IntegerField()
    # HOUR_OF_DAY
    hour=models.IntegerField()
    # INTERSECT_TYPE
    intersect_type=models.CharField(max_length=30)
    # COLLISION_TYPE
    collision_type=models.CharField(max_length=30)
    # FATAL_COUNT
    fatal_count=models.IntegerField()
    # INJURY_COUNT
    injury_count=models.IntegerField()
    # SEV_INJ_COUNT
    sev_inj_count=models.IntegerField()
    # MAJ_INJ_COUNT
    maj_inj_count=models.IntegerField()
    # MCYCLE_DEATH_COUNT
    mcycle_death_count=models.IntegerField()
    # MCYCLE_SEV_INJ_COUNT
    mcycle_sev_inj_count=models.IntegerField()
    # BICYCLE_DEATH_COUNT
    bicycle_death_count=models.IntegerField()
    # BICYCLE_SEV_INJ_COUNT
    bicycle_sev_inj_count=models.IntegerField()
    # PED_DEATH_COUNT
    ped_death_count=models.IntegerField()

    # MAX_SEVERITY_LEVEL
    max_severity_level=models.CharField(max_length=30)
    # LATITUDE
    lat=models.FloatField()
    # LONGITUDE
    lng=models.FloatField()

    def __str__(self):
        return self.crn

class Person(models.Model):
    # CRN
    crn=models.CharField(max_length=20)
    # CRASH_YEAR
    year=models.IntegerField()
    # SEX
    sex=models.CharField(max_length=10)
    # AGE
    age=models.IntegerField()
    # PERSON_TYPE
    person_type=models.CharField(max_length=30)
    # RESTRAINT_HELMET
    restraint_helmet=models.CharField(max_length=30)

##Added by Phoebe
class Vehicle(models.Model):
    # CRN
    crn=models.CharField(max_length=20)
    # CRASH_YEAR
    year=models.IntegerField()
    # VEHICLE TYPE
    type=models.CharField(max_length=30)

class crashFile(models.Model):
    docfile = models.FileField(upload_to='crash/')

class vehicleFile(models.Model):
     docfile = models.FileField(upload_to='vehicle/')

class personFiles(models.Model):
    docfile = models.FileField(upload_to='person/')
    
    def __str__(self):
        return self.crn
