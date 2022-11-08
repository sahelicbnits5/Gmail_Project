import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass:
    def element_wait_clickable(self, path):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.element_to_be_clickable(path))

    def element_wait_presence(self, path):
        wait = WebDriverWait(self.driver, 10)
        send_to = None
        #breakpoint()
        for _ in range(10):
            send_to = wait.until(expected_conditions.presence_of_element_located(path))
            if send_to is not None:
                break
            else:
                continue
        return send_to
