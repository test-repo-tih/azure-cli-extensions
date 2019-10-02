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
        self.cmd('managed-network create  --resource-group "myResourceGroup" --name "myManagedNetwork" --location "eastus"', checks=[
        ])

        self.cmd('managed-network create  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

        self.cmd('managed-network create  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

# create_or_update -- update
        self.cmd('managed-network update  --resource-group "myResourceGroup" --name "myManagedNetwork" --location "eastus"', checks=[
        ])

        self.cmd('managed-network update  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

        self.cmd('managed-network update  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

# delete -- delete
        self.cmd('managed-network delete  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

        self.cmd('managed-network delete  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

        self.cmd('managed-network delete  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

# list_by_resource_group -- list
        self.cmd('managed-network list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('managed-network list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('managed-network list  --resource-group "myResourceGroup"', checks=[
        ])

# list_by_subscription -- list
        self.cmd('managed-network list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('managed-network list  --resource-group "myResourceGroup"', checks=[
        ])

        self.cmd('managed-network list  --resource-group "myResourceGroup"', checks=[
        ])

# get -- show
        self.cmd('managed-network show  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

        self.cmd('managed-network show  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

        self.cmd('managed-network show  --resource-group "myResourceGroup" --name "myManagedNetwork"', checks=[
        ])

# create_or_update -- create
        self.cmd('managed-network create  --scope "subscriptions/subscriptionC" --name "subscriptionCAssignment" --assigned-managed-network "subscriptions/subscriptionA/resourceGroups/myResourceGroup/providers/Microsoft.ManagedNetwork/managedNetworks/myManagedNetwork"', checks=[
        ])

        self.cmd('managed-network create  --scope "subscriptions/subscriptionC" --name "subscriptionCAssignment"', checks=[
        ])

# create_or_update -- update
        self.cmd('managed-network update  --scope "subscriptions/subscriptionC" --name "subscriptionCAssignment" --assigned-managed-network "subscriptions/subscriptionA/resourceGroups/myResourceGroup/providers/Microsoft.ManagedNetwork/managedNetworks/myManagedNetwork"', checks=[
        ])

        self.cmd('managed-network update  --scope "subscriptions/subscriptionC" --name "subscriptionCAssignment"', checks=[
        ])

# delete -- delete
        self.cmd('managed-network delete  --scope "subscriptions/subscriptionC" --name "subscriptionCAssignment"', checks=[
        ])

        self.cmd('managed-network delete  --scope "subscriptions/subscriptionC" --name "subscriptionCAssignment"', checks=[
        ])

# list -- list
        self.cmd('managed-network list  --scope "subscriptions/subscriptionC"', checks=[
        ])

        self.cmd('managed-network list  --scope "subscriptions/subscriptionC"', checks=[
        ])

# get -- show
        self.cmd('managed-network show  --scope "subscriptions/subscriptionC" --name "subscriptionCAssignment"', checks=[
        ])

        self.cmd('managed-network show  --scope "subscriptions/subscriptionC" --name "subscriptionCAssignment"', checks=[
        ])

# create_or_update -- create
        self.cmd('managed-network managed-network-group create  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

        self.cmd('managed-network managed-network-group create  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

# create_or_update -- update
        self.cmd('managed-network managed-network-group update  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

        self.cmd('managed-network managed-network-group update  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

# delete -- delete
        self.cmd('managed-network managed-network-group delete  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

        self.cmd('managed-network managed-network-group delete  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

# list_by_managed_network -- list
        self.cmd('managed-network managed-network-group list  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork"', checks=[
        ])

        self.cmd('managed-network managed-network-group list  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork"', checks=[
        ])

# get -- show
        self.cmd('managed-network managed-network-group show  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

        self.cmd('managed-network managed-network-group show  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myManagedNetworkGroup1"', checks=[
        ])

# create_or_update -- create
        self.cmd('managed-network managed-network-peering-policy create  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke" --type "HubAndSpokeTopology"', checks=[
        ])

        self.cmd('managed-network managed-network-peering-policy create  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])

# create_or_update -- update
        self.cmd('managed-network managed-network-peering-policy update  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke" --type "HubAndSpokeTopology"', checks=[
        ])

        self.cmd('managed-network managed-network-peering-policy update  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])

# delete -- delete
        self.cmd('managed-network managed-network-peering-policy delete  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])

        self.cmd('managed-network managed-network-peering-policy delete  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])

# list_by_managed_network -- list
        self.cmd('managed-network managed-network-peering-policy list  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork"', checks=[
        ])

        self.cmd('managed-network managed-network-peering-policy list  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork"', checks=[
        ])

# get -- show
        self.cmd('managed-network managed-network-peering-policy show  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])

        self.cmd('managed-network managed-network-peering-policy show  --resource-group "myResourceGroup" --managed-network-name "myManagedNetwork" --name "myHubAndSpoke"', checks=[
        ])
