# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose

def test_foo():
    gilded_rose = GildedRose([Item("foo", 0, 0)])
    gilded_rose.update_quality()
    assert "FixMe" == gilded_rose.items[0].name
