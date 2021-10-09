from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.core.mail import EmailMessage

from threading import Thread




# Create your views here.



def contacto(request):

    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)

        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")


            email=EmailMessage("Mensaje enviado desde IZZI PARKING",
            "El usuario con nombre {}  con la direccion {} escribe  lo sieguiente :\n\n{}".format(nombre,email,contenido),
            "",["fikuss2000@gmail.com"],reply_to=[email])
            try: 
                email.send()
                return redirect("/contacto/?valido")

            except:
                
                return redirect("/contacto/?novalido")


    return render(request, "contacto/contacto.html" , {'miformulario':formulario_contacto})