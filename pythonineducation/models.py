from django.db import models
from django_amber.models import ModelWithContent


class Page(ModelWithContent):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    language = models.CharField(max_length=255)

    dump_path_template =  'content/[language]/[slug].[content_format]'

    key_field_names = ['language', 'slug']

    def __str__(self):
        return '{}/{}'.format(self.language, self.slug)
