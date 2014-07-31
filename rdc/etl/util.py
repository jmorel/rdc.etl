# -*- coding: utf-8 -*-
#
# Copyright 2012-2014 Romain Dorgueil
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cgi
import time
from datetime import datetime

import requests
from blessings import Terminal as _Terminal
from lxml import etree
from webapp2 import cached_property






class Timer(object):
    """
    Context manager used to time execution of stuff.
    """

    def __enter__(self):
        self.__start = time.time()

    def __exit__(self, type, value, traceback):
        # Error handling here
        self.__finish = time.time()

    @property
    def duration(self):
        return self.__finish - self.__start

    def __str__(self):
        return str(int(self.duration * 1000) / 1000.0) + 's'


def create_http_reader(url):
    """
    Simple reader for an HTTP resource.
    """

    def http_reader():
        return requests.get(url).content

    return http_reader


def create_file_reader(path):
    """
    Simple reader for a local filesystem resource.
    """

    def file_reader():
        with open(path, 'rU') as f:
            return f.read()

    return file_reader

def sfloat(mixed, default=None):
    """Safe float cast."""
    try:
        return float(mixed)
    except:
        return default

def sint(mixed, default=None):
    """Safe int cast."""
    try:
        return int(mixed)
    except:
        return default

def sbool(mixed, default=None):
    """Safe boolean cast."""
    try:
        return bool(mixed)
    except:
        return default

# Exports
terminal = _Terminal()
html_escape = cgi.escape

now = datetime.now
cached_property = cached_property
etree = etree

