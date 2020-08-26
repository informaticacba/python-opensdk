# Copyright 2020 TestProject (https://testproject.io)
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

import os
import pytest

from src.testproject.sdk.drivers import webdriver
from tests.pageobjects.web import LoginPage, ProfilePage


@pytest.fixture
def driver():

    emulator_id = os.environ.get("TP_ANDROID_DUT_UDID", None)

    if emulator_id is None:
        raise KeyError("TP_ANDROID_DUT_UDID variable was not set")

    desired_capabilities = {
        "udid": emulator_id,
        "browserName": "chrome",
        "platformName": "Android",
        "unicodeKeyboard": "true",
        "resetKeyboard": "true"
    }

    driver = webdriver.Remote(desired_capabilities=desired_capabilities)
    yield driver
    driver.quit()


def test_example_on_chrome_on_android(driver):

    LoginPage(driver).open().login_as("John Smith", "12345")

    profile_page = ProfilePage(driver)

    profile_page.update_profile(
        "United States",
        "Street name and number",
        "john.smith@somewhere.tld",
        "+1 555 555 55",
    )

    assert profile_page.saved_message_is_displayed() is True
