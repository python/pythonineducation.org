from django.shortcuts import get_object_or_404, render

from .models import Page


def page_view(request, language='en', slug='home'):
    page = get_object_or_404(Page, language=language, slug=slug)

    assert page.content_format in ['html', 'md'], 'Page content must use HTML or Markdown'

    template = 'page_{}.html'.format(language)

    context = {
        'content': page.content,
        'content_format': page.content_format,
        'title': page.title,
        'language': language,
    }

    return render(request, template, context)
