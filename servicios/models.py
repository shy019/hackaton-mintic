from django.db import models

# Create your models here.


class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=500)
    direccion = models.CharField(null = True,max_length=500)
    fecha=models.DateTimeField(null=True, max_length=400)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo



ciudad =[(1,"Bogota"),
               (2,"Medellín"),
               (3,"	Cali"),
               (4,"Barranquilla"),
               (5,"	Cartagena de Indias"),
               (6,"Soacha"),
               (7,"Cúcuta"),
               (8,"	Soledad"),
               (9,"	Bucaramanga"),
               (10,"Bello"),
               (11,"Villavicencio"),
               (12,"Ibagué"),
               (13,"Santa Marta"),
               (14,"Valledupar"),
               (15,"Manizales"),
               (16,"Pereira"),
               (17,"Montería"),
               (18,"Neiva"),
               (19,"Pasto"),
               (20,"Armenia"),
               ]





class Registro(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    cedula = models.CharField(max_length=20)
    edad= models.IntegerField(max_length=3)
    ciudad= models.IntegerField(null = False, blank = False,choices=ciudad,verbose_name="Ciudad")
    elegir_evento = models.ForeignKey(Servicio,  null=True ,blank = True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='Registro'
        verbose_name_plural='Registros'

    def __str__(self):
        return self.nombre