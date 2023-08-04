from django.db import models

from users.models import User


class Diary(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Page(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.PROTECT)

    notes = models.TextField(null=True, blank=True)
    what_I_learned = models.TextField(null=True, blank=True)
    what_should_be_changed = models.TextField(null=True, blank=True)

    initial_tasks_number = models.PositiveIntegerField()
    total_tasks_number = models.PositiveIntegerField(null=True, blank=True)
    done_tasks_number = models.PositiveIntegerField(null=True, blank=True)

    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateField(null=True, blank=True)

    @property
    def done_percentage(self):
        if not self.total_tasks_number:
            return self.done_tasks_number / self.total_tasks_number

    def __str__(self):
        return f'{self.created_at}'
