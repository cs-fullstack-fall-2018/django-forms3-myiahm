from django.shortcuts import render, redirect, get_object_or_404
from .forms import Forms
from .models import NonProfit

def index(request):
    form_list = NonProfit.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context)


def add(request):
    if(request.method == 'POST'):
        form = Forms(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("index")
    else:
        form = Forms()
    return render(request, 'forms_app/add.html', {'form': form})


def edit(request, pk):
    theModel = get_object_or_404(NonProfit, pk=pk)

    if(request.method == 'POST'):
        form = Forms(request.POST, instance=theModel)
        if(form.is_valid()):
            form.save()
            return redirect("index")
        else:
            print("Hey buddy. It looks like your form was invalid. Sorry about that...")
            return redirect("edit", pk=pk)
    else:
        form = Forms(instance=theModel)
    return render(request, 'forms_app/add.html', {'form': form})