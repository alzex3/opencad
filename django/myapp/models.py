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
    obj_type = models.ForeignKey(ObjectType, on_delete=models.CASCADE, related_name='facility')
    address = models.CharField(max_length=250)
    update_date = models.DateField(max_length=10)
    full_address = models.CharField(max_length=450)
    created_date = models.DateField(max_length=10)
    cost = models.DecimalField(max_digits=13, decimal_places=2)
    stamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return self.cad_num


# Future
class List(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    user = models.CharField(max_length=15, verbose_name='Пользователь')
    facility = models.ManyToManyField(Object, related_name='list')

    class Meta:
        verbose_name = 'Списки'
        verbose_name_plural = 'Списки'

    def __str__(self):
        return self.title
