from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.groups import Group


def groups_list(request):
    groups = Group.objects.all().order_by('title')

    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.order_by(order_by).reverse()

    # paginate students
    paginator = Paginator(groups, 2)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # deliver first page
        groups = paginator.page(1)
    except EmptyPage:
        # deliver last page
        groups = paginator.page(paginator.num_pages)

    return render(request, 'students/groups.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('Group Add Form')


def groups_edit(request, sid):
    return HttpResponse('Edit Group %s' % sid)


def groups_delete(request, sid):
    return HttpResponse('Delete Groups %s' % sid)