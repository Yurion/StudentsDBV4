from django.db import models


class Group(models.Model):
    """Group Model"""

    class Meta:
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'

    title = models.CharField("Назва",
                             max_length=256,
                             blank=False)

    leader = models.OneToOneField('Student',
                                  verbose_name='Староста',
                                  null=True,
                                  blank=True,
                                  on_delete=models.SET_NULL)

    notes = models.TextField('Додаткові нотатки',
                             blank=True)

    def __str__(self):
        if self.leader:
            return "{0} ({1} {2})".format(self.title, self.leader.first_name, self.leader.last_name)
        else:
            return "{0}".format(self.title)
