from tests.conftest import browser


def test_youtube_site_load(browser):
    browser.open("http://www.youtube.com")
