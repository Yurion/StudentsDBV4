from django.db import models


class Exam(models.Model):
    """Exam Model"""

    class Meta:
        verbose_name = 'Екзамен'
        verbose_name_plural = 'Екзамени'

    exam_name = models.CharField("Назва предмету",
                                 max_length=256,
                                 blank=False)

    date = models.DateField("Дата проведення",
                            blank=False)

    teacher_name = models.CharField("Викладач",
                                    max_length=256,
                                    blank=False)

    exam_group = models.ForeignKey('Group',
                                   verbose_name='Група',
                                   blank=False,
                                   null=True,
                                   on_delete=models.PROTECT)

    notes = models.TextField('Додаткові нотатки',
                             blank=True)

    def __str__(self):
        return "{0} ({1} {2})".format(self.exam_name, self.exam_group, self.teacher_name)
