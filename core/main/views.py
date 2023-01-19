from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import HomeMenu, SingleImage, RightImage

# Create your views here.


class HomeListView(ListView):
    template_name = 'index.html'

    def get(self,request):
        homemenu = HomeMenu.objects.all()
        singleimage = SingleImage.objects.all()
        rightimage = RightImage.objects.all()
        return render(request, self.template_name, {'homemenu':homemenu, 'singleimage':singleimage, 'rightimage':rightimage})
