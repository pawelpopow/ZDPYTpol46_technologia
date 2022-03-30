# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Census(models.Model):
    id = models.AutoField(blank=True, primary_key=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    pop2000 = models.IntegerField(blank=True, null=True)
    pop2008 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'census'

    def __str__(self):
        return f"{self.state} {self.age} {self.sex} {self.pop2008}"


class StateFact(models.Model):
    id = models.AutoField(blank=True, primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    abbreviation = models.CharField(max_length=128, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    type = models.CharField(max_length=128, blank=True, null=True)
    sort = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=128, blank=True, null=True)
    occupied = models.CharField(max_length=128, blank=True, null=True)
    notes = models.CharField(max_length=128, blank=True, null=True)
    fips_state = models.CharField(max_length=128, blank=True, null=True)
    assoc_press = models.CharField(max_length=128, blank=True, null=True)
    standard_federal_region = models.CharField(max_length=128, blank=True, null=True)
    census_region = models.CharField(max_length=128, blank=True, null=True)
    census_region_name = models.CharField(max_length=128, blank=True, null=True)
    census_division = models.CharField(max_length=128, blank=True, null=True)
    census_division_name = models.CharField(max_length=128, blank=True, null=True)
    circuit_court = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_fact'
