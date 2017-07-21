from django.db import models
from django.template.defaultfilters import slugify


class Todo(models.Model):

    title = models.CharField(max_length=128, unique=True)
    body = models.TextField()
    # done = models.BooleanField(default=False)

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Todos'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Todo, self).save(*args, **kwargs)


class Comment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, unique=True)
    body = models.TextField()

    class Meta:
        verbose_name_plural = 'Comments'

        def __str__(self):
            return self.name
