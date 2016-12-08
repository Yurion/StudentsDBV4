from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student

preview_order = 'last_name'
preview_reverse = ''


def students_list(request):
    students = Student.objects.all().order_by('last_name')

    global preview_order
    global preview_reverse

    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        preview_order = order_by
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            preview_reverse = '1'
            students = students.reverse()
        else:
            preview_reverse = ''

    if order_by == 'numb':
        if request.GET.get('reverse', '') == '1':
            if preview_reverse == '1':
                students = students.order_by(preview_order)
            else:
                students = students.order_by(preview_order).reverse()
        else:
            if preview_reverse == '1':
                students = students.order_by(preview_order).reverse()
            else:
                students = students.order_by(preview_order)

    return render(request, 'students/students_list.html', {'students': students, 'request': request})


def students_add(request):
    return HttpResponse('Student Add Form')


def students_edit(request, sid):
    return HttpResponse('Edit Student %s' % sid)


def students_delete(request, sid):
    return HttpResponse('Delete Student %s' % sid)