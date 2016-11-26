# from django.conf import settings
from django.http import HttpRequest


def students_proc(request):
    return {'PORTAL_URL': HttpRequest._get_scheme(request) + '://' + HttpRequest._get_raw_host(request)}
