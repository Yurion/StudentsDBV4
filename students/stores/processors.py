from StudentsDBV4.settings import PORTAL_URL  # хардкорний спосіб
# from django.conf.global_settings import PORTAL_URL # а хотілось би якось так

def students_proc(request):
    return {'PORTAL_URL': PORTAL_URL}