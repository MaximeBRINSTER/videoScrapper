import pytest

import scrapper


def test_init():
    link_len = len(scrapper.videos[3].get_videoId())
    assert link_len > 5


def test_get_title():
    title = scrapper.videos[2].get_title()
    assert title.__str__()


def test_get_date():
    date = scrapper.videos[0].get_date()
    assert date.__str__()


def test_get_views():
    views = scrapper.videos[6].get_views()
    assert views.isdecimal()


def test_get_desc():
    desc = len(scrapper.videos[0].get_desc())
    assert desc > 50


def test_get_links():
    links = scrapper.videos[3].get_links()
    assert links.__add__(["alpha"])


def test_get_channel_name():
    name = scrapper.videos[0].get_channel_name()
    assert 2 < len(name) < 25


def test_get_videoId():
    id = scrapper.videos[7].get_videoId()
    assert id.isprintable()


def test_get_dict():
    dict = scrapper.videos[5].get_dict()
    assert len(dict) == 7
