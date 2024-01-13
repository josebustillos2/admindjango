from django.db import models

from apps.utils import UpperCharField
from apps.validator.utils import NumberPhone, TypeDocument


# Create your models here.

class Category(models.Model):
    name = UpperCharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = UpperCharField(max_length=200, verbose_name="Nombre")
    ruc = models.BigIntegerField(
        unique=True,
        validators=[TypeDocument.valide_ruc],
        verbose_name="RUC"
    )
    email = models.EmailField(max_length=200, verbose_name="Correo electrónico")
    phone = models.CharField(max_length=200,validators=[NumberPhone.valide_cellphone], verbose_name="Teléfono/Celular")
    address = UpperCharField(max_length=256, verbose_name="Dirección y número de casa", )

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        unique_together = ["ruc",]

    def __str__(self):
        return self.name.upper()


class Product(models.Model):
    code = UpperCharField(max_length=25, verbose_name="Código")
    provider_code = UpperCharField(
        max_length=25, verbose_name="Cód. Proveedor", blank=True, null=True
    )
    name = UpperCharField(max_length=128, verbose_name="Nombre")
    cost = models.FloatField(verbose_name="Precio de costo", default=0)
    price1 = models.FloatField(verbose_name="Precio 1")
    price2 = models.FloatField(verbose_name="Precio 2", default=0)
    price3 = models.FloatField(verbose_name="Precio 3", default=0)
    discount = models.FloatField(verbose_name="Descuentos", default=0)
    stock = models.IntegerField(default=0)
    unit_size = models.ForeignKey(
        "UnitSizeProduct", on_delete=models.PROTECT, verbose_name="Unidad de Medida"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        verbose_name="Categoría",
        blank=True,
        null=True,
    )
    provider = models.ForeignKey(
        "Provider", on_delete=models.PROTECT, verbose_name="Proveedor"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        unique_together = ["code", "provider_code",]


class UnitSizeProduct(models.Model):
    name = UpperCharField(max_length=50, verbose_name="Nombre")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Ud. Medida"
