from django.db import models
from .utils import unique_code
from django.forms.widgets import TextInput


class Shorting(models.Model):
    url_in = models.URLField()
    code = models.CharField(max_length=10, unique=True, blank=True)

    def short_url(self):
        return f"http://127.0.0.1:8000/{self.code}"

    def save(self, *args, **kwargs):
        if self.code == '':
            self.code = unique_code(self)
        super(Shorting, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url_in)
