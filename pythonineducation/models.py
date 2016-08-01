from django.db import models
from django_amber.models import ModelWithContent


class Page(ModelWithContent):
    title = models.CharField(max_length=255)

    dump_dir_path = 'content'
