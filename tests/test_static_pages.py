# SPDX-License-Identifier: GPL-3.0
import app

import os
import sys

import pytest
import pytest_cov.embed


def test_static_pages(app, client):
    
    for f in os.listdir('templates'):
        if f == "template.html" or f == "page.html":
            continue

        # ignore non html files like system files e.g. '.DS_Store', '.thumbsdb', ...
        if f.split('.', 1)[1] not in ['html', 'htm']:
            continue

        static_file = f.split('.', 1)[0]
        page = "/" + static_file + ".html"
        print("Checking presence of: ", page)
        res = client.get(page)
        assert res.status_code == 200
