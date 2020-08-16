from tests.conftest import browser


def test_youtube_site_load(driver, browser):
    browser.open("http://www.youtube.com")
    assert driver.title == "YouTube"
