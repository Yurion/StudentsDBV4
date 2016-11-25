from django.conf import settings


def students_proc(request):
    return {'PORTAL_URL': settings.PORTAL_URL}