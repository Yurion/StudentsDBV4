from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student

previews_order = 'last_name'
previews_reverse = ''
# students = Student.objects.all().order_by(previews_order)


def students_list(request):
    students = Student.objects.all().order_by('last_name')

    # global students
    global previews_order
    global previews_reverse

    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        previews_order = order_by
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            previews_reverse = '1'
            students = students.reverse()
        else:
            previews_reverse = ''

    if order_by == 'numb':
        if request.GET.get('reverse', '') == '1':
            print('numb reverse')
            if previews_reverse == '1':
                students = students.order_by(previews_order)
            else:
                students = students.order_by(previews_order).reverse()
        else:
            print('numb')
            if previews_reverse != '1':
                students = students.order_by(previews_order)
            else:
                students = students.order_by(previews_order).reverse()

    return render(request, 'students/students_list.html', {'students': students, 'request': request})


def students_add(request):
    return HttpResponse('Student Add Form')


def students_edit(request, sid):
    return HttpResponse('Edit Student %s' % sid)


def students_delete(request, sid):
    return HttpResponse('Delete Student %s' % sid)