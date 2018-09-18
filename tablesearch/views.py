from django.shortcuts import render
from django.http import HttpResponse
from .models import Tables
from django.template import loader

# Create your views here.

# /tablesearch/
def index(request):
    all_tables = Tables.rows
    template = loader.get_template('tablesearch/home.html')
    context = {
        'all_tables': all_tables
    }
    return HttpResponse(template.render(context, request))