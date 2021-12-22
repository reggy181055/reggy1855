from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')

def volume(request):
    if request.method == 'POST':
        var1 = request.POST['pjg']
        var2 = request.POST['lbr']
        var3 = request.POST['tgi']
        var1 = float(var1)
        var2 = float(var2)
        var3 = float(var3)
        volbalok=var1*var2*var3
        context = {
            'panjang': var1,
            'lebar': var2,
            'tinggi': var3,
            'hasilvol': volbalok,
        }
        return render(request, 'main/volume.html', context)
    else:
        return render(request, 'main/volume.html', {})
