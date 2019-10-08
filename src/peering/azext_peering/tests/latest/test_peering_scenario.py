# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class ApimgmtScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='cli_test_apimgmt')
    def test_apimgmt(self, resource_group):

        self.kwargs.update({
            'name': 'test1'
        })

# create_or_update -- create
        self.cmd('peering create  --name "peerAsnName" --peer-asn "65000" --peer-name "Contoso"', checks=[
        ])

        self.cmd('peering create  --name "peerAsnName"', checks=[
        ])

# create_or_update -- update
        self.cmd('peering update  --name "peerAsnName" --peer-asn "65000" --peer-name "Contoso"', checks=[
        ])

        self.cmd('peering update  --name "peerAsnName"', checks=[
        ])

# delete -- delete
        self.cmd('peering delete  --name "peerAsnName"', checks=[
        ])

        self.cmd('peering delete  --name "peerAsnName"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('peering list ', checks=[
        ])

        self.cmd('peering list ', checks=[
        ])

# get -- show
        self.cmd('peering show  --name "peerAsnName"', checks=[
        ])

        self.cmd('peering show  --name "peerAsnName"', checks=[
        ])

# create_or_update -- create
        self.cmd('peering create  --resource-group "rgName" --name "peeringName" --sku-name "Basic_Direct_Free" --kind "Direct" --peering-location "peeringLocation0" --location "eastus"', checks=[
        ])

        self.cmd('peering create  --resource-group "rgName" --name "peeringName" --sku-name "Basic_Exchange_Free" --kind "Exchange" --peering-location "peeringLocation0" --location "eastus"', checks=[
        ])

        self.cmd('peering create  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering create  --resource-group "rgName" --name "peeringName"', checks=[
        ])

# create_or_update -- update
        self.cmd('peering update  --resource-group "rgName" --name "peeringName" --sku-name "Basic_Direct_Free" --kind "Direct" --peering-location "peeringLocation0" --location "eastus"', checks=[
        ])

        self.cmd('peering update  --resource-group "rgName" --name "peeringName" --sku-name "Basic_Exchange_Free" --kind "Exchange" --peering-location "peeringLocation0" --location "eastus"', checks=[
        ])

        self.cmd('peering update  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering update  --resource-group "rgName" --name "peeringName"', checks=[
        ])

# delete -- delete
        self.cmd('peering delete  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering delete  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering delete  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering delete  --resource-group "rgName" --name "peeringName"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

# get -- show
        self.cmd('peering show  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering show  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering show  --resource-group "rgName" --name "peeringName"', checks=[
        ])

        self.cmd('peering show  --resource-group "rgName" --name "peeringName"', checks=[
        ])

# create_or_update -- create
        self.cmd('peering prefixe create  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName" --prefix "192.168.1.0/24"', checks=[
        ])

        self.cmd('peering prefixe create  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName"', checks=[
        ])

# create_or_update -- update
        self.cmd('peering prefixe update  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName" --prefix "192.168.1.0/24"', checks=[
        ])

        self.cmd('peering prefixe update  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName"', checks=[
        ])

# delete -- delete
        self.cmd('peering prefixe delete  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName"', checks=[
        ])

        self.cmd('peering prefixe delete  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName"', checks=[
        ])

# list_by_peering_service -- list
        self.cmd('peering prefixe list  --resource-group "rgName" --peering-service-name "peeringServiceName"', checks=[
        ])

        self.cmd('peering prefixe list  --resource-group "rgName" --peering-service-name "peeringServiceName"', checks=[
        ])

# get -- show
        self.cmd('peering prefixe show  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName"', checks=[
        ])

        self.cmd('peering prefixe show  --resource-group "rgName" --peering-service-name "peeringServiceName" --name "peeringServicePrefixName"', checks=[
        ])

# create_or_update -- create
        self.cmd('peering create  --resource-group "rgName" --name "peeringServiceName" --peering-service-location "state1" --peering-service-provider "serviceProvider1" --location "eastus"', checks=[
        ])

        self.cmd('peering create  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

        self.cmd('peering create  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

# create_or_update -- update
        self.cmd('peering update  --resource-group "rgName" --name "peeringServiceName" --peering-service-location "state1" --peering-service-provider "serviceProvider1" --location "eastus"', checks=[
        ])

        self.cmd('peering update  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

        self.cmd('peering update  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

# delete -- delete
        self.cmd('peering delete  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

        self.cmd('peering delete  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

        self.cmd('peering delete  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

        self.cmd('peering list  --resource-group "rgName"', checks=[
        ])

# get -- show
        self.cmd('peering show  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

        self.cmd('peering show  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])

        self.cmd('peering show  --resource-group "rgName" --name "peeringServiceName"', checks=[
        ])
