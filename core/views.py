import os
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


# Create your views here.
def get_pdf(request):
    base_path = settings.MEDIA_ROOT
    with open(os.path.join(base_path, 'sample.pdf'), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response

