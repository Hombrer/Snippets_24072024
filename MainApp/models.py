from django.db import models
from django.contrib.auth.models import User


LANGS = (
    ('py', 'Python'),
    ('js', 'JavaScript'),
    ('cpp', 'C++'),
    ('html', 'HTML')
)


class Snippet(models.Model):
    class Meta:
        ordering = ['name', 'lang']

    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANGS, verbose_name="Язык")
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    public = models.BooleanField(default=True) # True = public, False = private

    def __repr__(self) -> str:
        return f'Snippet({self.name}, {self.lang})'
    
    def __str__(self) -> str:
        return f'{self.name}'

