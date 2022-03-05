from django.db import models


class ObjectType(models.Model):
    name = models.CharField(max_length=12)
    verbose_name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.verbose_name


class Object(models.Model):
    cad_num = models.CharField(max_length=20)
    obj_type = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    update_date = models.DateField(max_length=10)
    created_date = models.DateField(max_length=10)
    cost = models.DecimalField(max_digits=13, decimal_places=2)
    stamp = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class ParcelObject(Object):
    utility = models.CharField(max_length=100)


class BuildingObject(Object):
    name = models.CharField(max_length=100)


class FlatObject(Object):
    area = models.IntegerField()


class ConstructionObject(Object):
    name = models.CharField(max_length=100)


