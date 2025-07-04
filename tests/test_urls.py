import os
import re
import time
from os import environ
from pathlib import Path

import pytest
import requests

re_url = re.compile(r'[<"](https://github|https://raw.githubusercontent[^>"]*)[>"]')


def get_urls(glob_path):
    files = Path(".").glob(glob_path)
    for f in files:
        for url in re_url.findall(f.read_text()):
            if environ.get("PYTEST_ONLY", "") in url:
                yield f.as_posix(), url.strip('<">')


def request_rl(method, url):
    for i in range(1, 4):
        ret = method(url)
        if ret.status_code != 429:
            break

        backoff = int(ret.headers["Retry-After"])
        if backoff > 100:
            backoff = 100
        time.sleep(i * backoff)
    return ret


@pytest.mark.parametrize("fpath,url", get_urls("VocabolariControllati/**/*.ttl"))
def test_vocab_url(fpath, url):
    # raise NotImplementedError
    if "deprecated" in fpath.lower():
        return
    if "github.com/italia/dati-semantic-assets/issues" in url:
        return

    SKIP_URLS = [
        (
            ("cities.json", "cities.rdf"),
            "https://github.com/italia/dati-semantic-assets/issues/190",
        )
    ]
    for skip_urls, issue_url in SKIP_URLS:
        if any(x in url for x in skip_urls):
            pytest.skip(f"See {issue_url}")

    ret = request_rl(requests.head, url)

    # The file exists locally, so it will exist when a PR is merged
    url_filename = url.replace("https://raw.githubusercontent.com/italia/dati-semantic-assets/master/", "")
    if ret.status_code == 404 and os.path.exists(url_filename):
        return

    assert ret.status_code in (200, 301, 302)


@pytest.mark.parametrize("fpath,url", get_urls("Ontologie/**/latest/*.ttl"))
def test_onto_url(fpath, url):
    if "deprecated" in fpath.lower():
        return
    if "github.com/italia/dati-semantic-assets/issues" in url:
        return
    if url.endswith((".png", ".jpg", ".gif", ".svg")):
        return

    SKIP_URLS = [
        (
            ("AC-AP_IT",),
            "https://github.com/italia/dati-semantic-assets/issues/193",
        )
    ]
    for skip_urls, issue_url in SKIP_URLS:
        if any(x in url for x in skip_urls):
            pytest.skip(f"See {issue_url}")

    ret = request_rl(requests.head, url)

    # The file exists locally, so it will exist when a PR is merged
    url_filename = url.replace("https://raw.githubusercontent.com/italia/dati-semantic-assets/master/", "")
    if ret.status_code == 404 and os.path.exists(url_filename):
        return

    assert ret.status_code in (200, 301, 302)
