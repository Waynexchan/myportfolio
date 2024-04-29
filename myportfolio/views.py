from django.shortcuts import render
from django.views.generic import FormView
from .forms import Contactform
from django.urls import reverse_lazy

# Create your views here.
class Homeview(FormView):
    template_name ='myportfolio/index.html'
    form_class = Contactform
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
