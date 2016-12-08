from django.shortcuts import render
from django.http import HttpResponse


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