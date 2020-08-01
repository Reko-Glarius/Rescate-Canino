from django.db import models

# Create your models here.
class Dog(models.Model):
    STATE=[
        ("0", "Disponible"),
        ("1", "Adoptada")
    ]
    AGES=[
        ("Cachorro","Cachoro"),
        ("Jpven", "Joven"),
        ("Adulto", "Adulto"),
        ("Anciano", "Anciano")
    ]
    id=models.AutoField(primary_key=True, unique=True )
    name=models.CharField("Nombre", max_length=50)
    description=models.TextField("Descripcion", max_length=200)
    race=models.CharField("Raza", max_length=50)
    age=models.CharField("Edad", choices=AGES, max_length=8)
    state=models.CharField("Estado", choices=STATE, max_length=2)
    photo=models.ImageField("Fotografia", upload_to="Dogs")
    date=models.DateField("Fecha de Registro", auto_now_add=True)

    class Meta:
        verbose_name="Perro"
        verbose_name_plural="Perros"
        ordering=["-date"]

    def __str__(self):
        return self.name