from django.shortcuts import render
from .forms import ExampleForm
# Create your views here.
def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))
    else:
        form = ExampleForm()

    return render(request, "form_example.html", {"method": request.method, "form": form})

