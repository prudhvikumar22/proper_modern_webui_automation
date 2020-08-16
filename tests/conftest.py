from webui.webui import create_driver
from pytest import fixture, mark
from webui.webui import WebUI, create_driver


@fixture(scope='session')
def browser():
    driver = create_driver('CHROME')
    browser = WebUI(driver)
    yield browser
