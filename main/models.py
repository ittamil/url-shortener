from django.db import models
import random ,string

class Shortener(models.Model):
    name = models.CharField(max_length = 500,blank = True)
    slug = models.SlugField(blank = True)
    url = models.URLField(blank = True)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True,null = True)

    def save(self, *args, **kwargs):
        slug = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k = 7))
        if Shortener.objects.filter(slug = slug).exists():
            self.slug = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k = 7))
        else:
            self.slug = slug 
        super(Shortener, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
