from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import loader

# Create your views here.

# /tablesearch/
def index(request):
    all_tables = Tables.all_tables
    data_type = DataType.data_type
    template = loader.get_template('tablesearch/home.html')
    context = {
        'all_tables': all_tables,
        'data_type': data_type
    }
    return HttpResponse(template.render(context, request))