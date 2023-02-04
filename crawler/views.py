from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.views.decorators.http import require_POST

from crawler.helpers import find_urls


def index(request, **kwargs):
    return render(request, 'index.html', context=kwargs)


@require_POST
def crawl(request):
    url = request.POST.get('url')

    validate = URLValidator()
    try:
        validate(url)
    except ValidationError as e:
        return index(request, error=e.message)

    found_urls_dict = find_urls(url, max_nesting_level=3)

    return render(request, 'crawl_result.html', {
        'url': url,
        'links': found_urls_dict,
    })
