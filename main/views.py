from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import models


def handle_index(request: HttpRequest) -> HttpResponse:

    preview_images = models.PreviewImage.objects.all()
    context = {'preview_images': preview_images}

    return render(request, 'home/home.html', context)


def handle_contacts(request: HttpRequest) -> HttpResponse:
    contacts = models.Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'contacts/index.html', context)


def handle_about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about/index.html')
