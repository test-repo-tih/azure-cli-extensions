# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class HealthcareApisScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_healthcareapis')
    def test_healthcareapis(self, resource_group):

        self.kwargs.update({
            'name': 'test1'
        })

        self.cmd('az healthcareapis create --resource-group {rg} --name "service1"', checks=[
        ])
