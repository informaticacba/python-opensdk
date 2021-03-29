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

from selenium.webdriver import ChromeOptions

from src.testproject.enums.report_type import ReportType
from src.testproject.sdk.drivers.webdriver.base import BaseDriver


class Chrome(BaseDriver):
    """Used to create a new Chrome browser instance

    Args:
        chrome_options (ChromeOptions): Chrome automation session desired capabilities and options
        desired_capabilities (dict): Dictionary object containing desired capabilities for Chrome automation session
        token (str): The developer token used to communicate with the agent
        project_name (str): Project name to report
        job_name (str): Job name to report
        disable_reports (bool): set to True to disable all reporting (no report will be created on TestProject)
        report_type (ReportType): Type of report to produce - cloud, local or both.
    """

    def __init__(self, chrome_options: ChromeOptions = None, desired_capabilities: dict = None, token: str = None,
                 project_name: str = None, job_name: str = None, disable_reports: bool = False,
                 report_type: ReportType = ReportType.CLOUD_AND_LOCAL):

        # If no options or capabilities are specified at all, use default ChromeOptions
        if chrome_options is None and desired_capabilities is None:
            caps = ChromeOptions().to_capabilities()
        else:
            # Specified ChromeOptions take precedence over desired capabilities but either can be used
            caps = (
                chrome_options.to_capabilities()
                if chrome_options is not None
                else desired_capabilities
            )

        super().__init__(
            capabilities=caps,
            token=token,
            project_name=project_name,
            job_name=job_name,
            disable_reports=disable_reports,
            report_type=report_type
        )
