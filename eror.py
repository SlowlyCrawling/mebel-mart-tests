import pytest

def test_will_fail(driver, base_url):
    driver.get(base_url)
    assert False, "Зачем ты меня уронил..."