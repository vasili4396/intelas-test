from collections import defaultdict
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urljoin

DISMISSED_HREFS = ['#', 'tel:', 'mailto:', 'javascript:']


def find_urls(input_url, max_nesting_level=1, _cur_nesting_level=1, _processed_urls=None):
    if _processed_urls is None:
        _processed_urls = set()

    if _cur_nesting_level > max_nesting_level or input_url in _processed_urls:
        return {}


    try:
        html_content = urllib.request.urlopen(input_url, timeout=10)
    except Exception as e:
        print(f'{input_url} ended with error')
        return {}

    _processed_urls.add(input_url)

    soup = BeautifulSoup(html_content, 'html.parser')
    links = defaultdict(dict)

    for tag in soup.find_all('a', href=True):
        href = tag.get('href')
        # dismiss anchors, tel's and mailto's
        if not href or any([href.startswith(dismissed) for dismissed in DISMISSED_HREFS]):
            continue
        href = urljoin(input_url, href)
        if href.endswith('/'):
            href = href[:-1]
        if href not in _processed_urls:
            links[href].update(
                find_urls(href, max_nesting_level, _cur_nesting_level + 1, _processed_urls)
            )

    return links
