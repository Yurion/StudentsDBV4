from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from datetime import datetime
from django.contrib import messages
from ..models.students import Student
from ..models.groups import Group


def students_list(request):
    students = Student.objects.all().order_by('last_name')

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # deliver first page
        students = paginator.page(1)
    except EmptyPage:
        # deliver last page
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students, 'request': request})


def students_add(request):
    if request.method == 'POST':
        if request.POST.get('add_button') is not None:
            errors = {}

            data = {'middle_name': request.POST.get('middle_name'),
                    'notes': request.POST.get('notes')}

            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = "Ім'я є обов'язковим"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = "Прізвище є обов'язковим"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = "Дата народження є обов'язковою"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = 'Не вірний формат дати (YYYY-MM-DD)'
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = "Номер білета є обов'язковим"
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = "Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = 'Помилка вибору групи'
                else:
                    data['student_group'] = groups[0]

            # TODO 'make validation for photo'
            photo = request.FILES.get('photo')
            if photo:
                # print('Size: ', os.stat(photo).st_size)
                data['photo'] = photo

            if not errors:
                student = Student(**data)
                # student.save()
                # return render(request, 'students/students_add.html',
                #               {'groups': Group.objects.all().order_by('title'),
                #                'errors': errors})

                messages.info(request, 'Студента успішно додано')
                # return HttpResponseRedirect('{0}?status_message=Студента успішно додано'.format(reverse('home')))
                return HttpResponseRedirect(reverse('home'))
            else:
                # messages.add_message(request, messages.ERROR, 'Заповніть форму правильно')
                messages.warning(request, 'Заповніть форму правильно')
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'),
                               'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            messages.info(request, 'Додавання студента скасовано!')
            return HttpResponseRedirect(reverse('home'))

    else:
        return render(request, 'students/students_add.html',
                      {'groups': Group.objects.all().order_by('title')})


def students_edit(request, sid):
    return HttpResponse('Edit Student %s' % sid)


def students_delete(request, sid):
    return HttpResponse('Delete Student %s' % sid)