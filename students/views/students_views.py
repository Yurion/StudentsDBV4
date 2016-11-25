from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    students = (
        {'id': 1,
         'first_name': 'Віталій',
         'last_name': 'Подоба',
         'ticket': 235,
         'image': 'img/me.jpeg'},
        {'id': 2,
         'first_name': 'Корост',
         'last_name': 'Андрій',
         'ticket': 2123,
         'image': 'img/piv.png'},
        {'id': 3,
         'first_name': 'Притула',
         'last_name': 'Тарас',
         'ticket': 5332,
         'image': 'img/podoba3.jpg'}
    )
    return render(request, 'students/students_list.html', {'students': students, 'request': request})


def students_add(request):
    return HttpResponse('Student Add Form')


def students_edit(request, sid):
    return HttpResponse('Edit Student %s' % sid)


def students_delete(request, sid):
    return HttpResponse('Delete Student %s' % sid)