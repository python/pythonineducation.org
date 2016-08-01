from django.shortcuts import get_object_or_404, render

from .models import Page


def page_view(request, key):
    if not key:
        key = 'en'

    page = get_object_or_404(Page, key=key)

    assert page.content_format in ['html', 'md'], 'Page content must use HTML or Markdown'

    language = key.split('/')[0]

    template = 'page_{}.html'.format(language)

    context = {
        'content': page.content,
        'content_format': page.content_format,
        'title': page.title,
        'language': language,
    }

    return render(request, template, context)
