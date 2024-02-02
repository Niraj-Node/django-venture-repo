from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST) # Create an instance of the RegistrationForm with the POST data
        if form.is_valid():
            data = form.cleaned_data # Get the cleaned data from the form (validated and converted data)
            return render(request, 'register_form/details.html', {'data': data})
    else:
        form = RegistrationForm()
    return render(request, 'register_form/registration_form.html', {'form': form})