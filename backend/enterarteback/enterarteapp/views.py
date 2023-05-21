from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Eventos

def evento_lista(request):
    eventos = Eventos.objects.all()
    return render(request, 'evento_lista.html', {'eventos': eventos})

def evento_detalle(request, idEvento):
    evento = get_object_or_404(Eventos, idEvento=idEvento)
    return render(request, 'evento_detalle.html', {'evento': evento})

def evento_crear(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        idEvento = request.POST['idEvento']
        idUser = request.POST['idUser']
        idTicket = request.POST['idTicket']

        # Crear el objeto evento
        evento = Eventos(idEvento=idEvento, idUser=idUser, idTicket=idTicket)
        evento.save()
        
        return redirect('evento_lista')

    return render(request, 'evento_crear.html')

def evento_editar(request, idEvento):
    evento = get_object_or_404(Eventos, idEvento=idEvento)

    if request.method == 'POST':
        # Obtener datos del formulario
        evento.idUser = request.POST['idUser']
        evento.idTicket = request.POST['idTicket']

        # Guardar los cambios en el objeto evento
        evento.save()

        return redirect('evento_lista')

    return render(request, 'evento_editar.html', {'evento': evento})

def evento_eliminar(request, idEvento):
    evento = get_object_or_404(Eventos, idEvento=idEvento)

    if request.method == 'POST':
        # Eliminar el objeto evento
        evento.delete()
        
        return redirect('evento_lista')

    return render(request, 'evento_eliminar.html', {'evento': evento})
