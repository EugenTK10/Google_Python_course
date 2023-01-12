from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import  redirect
from joburi.models import Joburi


# Create your views here.

class JoburiView(ListView):
    model = Joburi
    template_name = 'joburi/joburi_index.html'


class CreateJoburiView(CreateView):
    model = Joburi
    fields = ['url', 'title', 'type', 'description']
    template_name = 'joburi/joburi_form.html'

    def get_success_url(self):
        return reverse('joburi:lista_joburi')


class UpdateJoburiView(UpdateView):
    model = Joburi
    fields = ['url', 'title', 'type', 'description']
    template_name = 'joburi/joburi_form.html'

    def get_success_url(self):
        return reverse('joburi:lista_joburi')

def delete_joburi(request, pk):
    Joburi.objects.filter(id=pk).update(active=0)
    return redirect('joburi:lista_joburi')

def activate_joburi(request, pk):
    Joburi.objects.filter(id=pk).update(active=1)
    return redirect('joburi:lista_joburi')