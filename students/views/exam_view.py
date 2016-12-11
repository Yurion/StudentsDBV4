from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models.exams import Exam


def exam_list(request):
    exams = Exam.objects.all().order_by('exam_name')

    order_by = request.GET.get('order_by', '')
    if order_by in ('id', 'exam_name', 'date', 'teacher_name', 'exam_group'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.order_by(order_by).reverse()

    # paginate students
    # paginator = Paginator(groups, 2)
    # page = request.GET.get('page')
    # try:
    #     groups = paginator.page(page)
    # except PageNotAnInteger:
    #     # deliver first page
    #     groups = paginator.page(1)
    # except EmptyPage:
    #     # deliver last page
    #     groups = paginator.page(paginator.num_pages)

    return render(request, 'students/exams.html', {'exams': exams})
