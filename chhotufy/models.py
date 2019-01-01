from django.db import models
from django.conf import settings
# Create your models here.
from .utils import create_code

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class shortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(shortURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_codes(self, items=None):
        qs = shortURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.code = create_code(q)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)

class shortURL(models.Model):
    url = models.CharField(max_length=200)
    code = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = shortURLManager()

    def save(self, *args, **kwargs):
        if self.code is None or self.code == "":
            self.code = create_code(self)
        super(shortURL,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
