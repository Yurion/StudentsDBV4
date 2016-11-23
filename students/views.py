from django.shortcuts import render
from django.http import HttpResponse


# Views for students
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
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('Student Add Form')


def students_edit(request, sid):
    return HttpResponse('Edit Student %s' % sid)


def students_delete(request, sid):
    return HttpResponse('Delete Student %s' % sid)


# View for groups
def groups_list(request):
    groups = (
        {'id': 1,
         'group_name': 'МтМ-21',
         'leader_name': 'Ячменев Олег'},
        {'id': 2,
         'group_name': 'МтМ-22',
         'leader_name': 'Віталій Подоба'},
        {'id': 3,
         'group_name': 'МтМ-23',
         'leader_name': 'Іванов Андрій'}
    )
    return render(request, 'students/groups.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('Group Add Form')


def groups_edit(request, sid):
    return HttpResponse('Edit Group %s' % sid)


def groups_delete(request, sid):
    return HttpResponse('Delete Groups %s' % sid)