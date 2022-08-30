from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import RegisterProvider, RegisterBuyer
from .forms import RegisterBuyerForm, RegisterProviderForm


def home(request):
    return render(request, 'car/home.html')


def thanks(request):
    return render(request, 'car/thanks.html')


class RegisterProviderView(CreateView):
    template_name = 'car/provider.html'
    form_class = RegisterProviderForm
    success_url = reverse_lazy('thanks')


class RegisterBuyerView(CreateView):
    template_name = 'car/buyer.html'
    form_class = RegisterBuyerForm
    success_url = reverse_lazy('thanks')


