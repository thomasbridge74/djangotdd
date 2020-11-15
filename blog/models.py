from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    slug = models.SlugField(default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'year': self.created_at.year,
            'month': self.created_at.month,
            'day': self.created_at.day,
            'slug': self.slug,
            'pk': self.pk,
        }
        return reverse('entry_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "entries"


class Comment(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.body


