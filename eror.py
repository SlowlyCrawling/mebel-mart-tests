import pytest

def test_will_fail(driver, base_url):
    """Тест который специально падает"""
    driver.get(base_url)
    assert False, "Этот тест упал специально для проверки скриншота"