
from functools import total_ordering
from django.db import models
from datetime import date
from django.db.models.query_utils import select_related_descend

from django.utils.translation import override

# Create your models here.

tipo_vehicu = [(1,"Camioneta"),
               (2,"Motocarro"),
               (3,"Automovil"),
               (4,"Motocicleta"),
               (5,"Bus"),
               (6,"Camion"),
               ]

preci_estadar__tipo_vehiculo =[(1,"4000"),
               (2,"4000"),
               (3,"3500"),
               (4,"2000"),
               (5,"5000"),
               (6,"8000"),
               ]

class Cliente(models.Model):
    nombre=models.CharField(max_length=50,verbose_name="Nombres")
    apellido=models.CharField(max_length=50,verbose_name="Apellidos")
    telefono=models.IntegerField(verbose_name="Telefono")
    #tipo_vehiculo=models.IntegerField(null = False, blank = False,choices=tipo_vehicu,verbose_name="Tipo de vehiculo")
    email=models.EmailField(verbose_name="Email")
    #frecuente_si_no=models.BooleanField()
    
    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes" 
        
    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    hora_llegada = models.DateTimeField()
    placa = models.CharField(max_length=6)
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas" 
        
    def __str__(self):
        #texto = "({1})"
        #return texto.format(self.placa)
        return self.placa
    
    
class Vehiculo(models.Model):
    tipo_vehiculo=models.IntegerField(null = False, blank = False,choices=tipo_vehicu,verbose_name="Tipo de vehiculo")
    dueño_vehiculo = models.ForeignKey(Cliente,  null=True ,blank = True, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    cilindraje = models.CharField(max_length=40)
    placa = models.CharField(null = True,max_length=6)
    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos" 
        
    def __str__(self):
 
        return self.placa
        
    
class Factura(models.Model):
    hora_llegada = models.DateTimeField()
    hora_salida = models.DateTimeField()
    placa_vehiculo = models.ForeignKey(Vehiculo,  null=True ,blank = True, on_delete=models.CASCADE)
    nombre_administrativo = models.CharField(max_length=20)
    tipo_vehiculo=models.IntegerField(null = False, blank = False,choices=tipo_vehicu)
    dueño_vehiculo = models.ForeignKey(Cliente,  null=True ,blank = True, on_delete=models.CASCADE)
    #ubicacion_vehiculo = models.ForeignKey(Parqueadero,  null=True ,blank = True, on_delete=models.CASCADE)
    total_vehiculo = models.IntegerField(null = True, blank = False,choices=preci_estadar__tipo_vehiculo)
    frecuente_si_no=models.BooleanField()
    
    class Meta:
        verbose_name = "factura"
        verbose_name_plural = "facturas"
        
    
ubicacion = [(1,"A1"),
               (2,"A2"),
               (3,"A3"),
               (4,"A4"),
               (5,"A5"),
               (6,"A6"),
               (7,"A7"),
               (8,"A8"),
               (9,"A9"),
               (10,"A10"),
               (11,"A11"),
               (12,"A12"),
               (13,"A13"),
               (14,"A14"),
               (15,"A15"),
               (16,"A16"),
               (17,"A17"),
               (18,"A18"),
               (19,"A19"),
               (20,"A20"),
               ]

class Parqueadero(models.Model):

    nombre_administrador = models.CharField(max_length=20)
    ubicacion = models.IntegerField(null = False, blank = False,choices=ubicacion,verbose_name="Ubicacion parqueadero")
    placa_vehiculo = models.ForeignKey(Vehiculo,  null=True ,blank = True, on_delete=models.CASCADE)
    gastos_totales = models.FloatField() 
    hora_puesto = models.TimeField(null=True,verbose_name="Hora de llegada")
    hora_puesto_exit = models.TimeField(null=True,verbose_name="Hora de salida")
    
    class Meta:
        verbose_name = "parqueo"
        
        
  
class Puesto(models.Model):
    puestos_totales = models.IntegerField()
    puestos_llenos = models.IntegerField()
    puestos_vacios = models.IntegerField()
    ubicacion = models.IntegerField(null = True, blank = False,choices=ubicacion,verbose_name="Ubicacion parqueadero")

    
    class Meta:
        verbose_name = "Puesto"
 