from django.shortcuts import render
from django.http import HttpResponse


def visiting_list(request):
    return render(request, 'students/visiting.html', {})