from django.shortcuts import render, redirect
from .forms import DuplicarGastosForm
from .models import Quincena, Gasto, Ingreso
from django.contrib.auth.decorators import login_required

@login_required
def resumen_quincenal(request):
    """
    Vista que muestra ingresos y gastos organizados por quincena.
    """
    quincenas = Quincena.objects.all().order_by('fecha_inicio')
    datos = []

    for q in quincenas:
        ingresos = Ingreso.objects.filter(quincena=q)
        gastos = Gasto.objects.filter(quincena=q)

        total_ingresos = sum(i.monto for i in ingresos)
        total_gastos = sum(g.monto for g in gastos)
        disponibles = total_ingresos - total_gastos

        datos.append({
            'quincena': q,
            'ingresos': ingresos,
            'gastos': gastos,
            'total_ingresos': total_ingresos,
            'total_gastos': total_gastos,
            'disponibles': disponibles
        })

    return render(request, 'gastos/resumen.html', {'datos': datos})

@login_required
def duplicar_gastos(request):
    """
    Vista para duplicar los gastos de una quincena origen a otra destino.
    """
    if request.method == 'POST':
        form = DuplicarGastosForm(request.POST)
        if form.is_valid():
            origen = form.cleaned_data['origen']
            destino = form.cleaned_data['destino']

            # Copiar todos los gastos de la quincena origen
            gastos_origen = Gasto.objects.filter(quincena=origen)
            for gasto in gastos_origen:
                Gasto.objects.create(
                    nombre=gasto.nombre,
                    monto=gasto.monto,
                    tipo=gasto.tipo,
                    categoria=gasto.categoria,
                    quincena=destino,
                    pagado=False  # Por defecto, los gastos duplicados están sin pagar
                )
            return redirect('resumen_quincenal')  # Redirige al resumen
    else:
        form = DuplicarGastosForm()

    return render(request, 'gastos/duplicar_gastos.html', {'form': form})

@login_required
def crear_quincena(request):
    """
    Crea una nueva quincena vacía con el nombre dado desde el formulario.
    """
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if nombre:
            Quincena.objects.create(nombre=nombre)
    return redirect('duplicar_gastos')
@login_required
def profile_view(request):
    return render(request, 'account/profile.html')