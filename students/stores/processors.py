# from django.conf import settings
from django.http import HttpRequest


def students_proc(request):
    return {'PORTAL_URL': HttpRequest.get_raw_uri(request)}