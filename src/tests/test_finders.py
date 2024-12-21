#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations
import pytest
from jpaye import get_jcpy_path, get_libpython, get_jcpy_loader, get_jcpy_engine


def test_jcpy_path():
    pth = get_jcpy_path()
    print(pth)
    assert "jpaye/jcpy" in pth


def test_libpython():
    pth = get_libpython()
    print(pth)
    assert "libpython3" in pth


def test_loader():
    pth = get_jcpy_loader()
    print(pth)
    assert "loader.so" in pth


def test_engine():
    pth = get_jcpy_engine()
    print(pth)
    assert "engine.so" in pth
