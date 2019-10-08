# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument

import json


def create_peering_asn(cmd, client,
                       name,
                       peer_asn=None,
                       peer_contact_info=None,
                       peer_name=None,
                       validation_state=None):
    return client.create_or_update(peer_asn_name=name, peer_asn=peer_asn)


def update_peering_asn(cmd, client, body,
                       name,
                       peer_asn=None,
                       peer_contact_info=None,
                       peer_name=None,
                       validation_state=None):
    return client.create_or_update(peer_asn_name=name, peer_asn=peer_asn)


def list_peering_asn(cmd, client):
    return client.list_by_subscription()


def create_peering(cmd, client,
                   resource_group,
                   name,
                   kind,
                   location,
                   sku_name=None,
                   sku_tier=None,
                   sku_family=None,
                   sku_size=None,
                   direct=None,
                   exchange=None,
                   peering_location=None,
                   tags=None):
    return client.create_or_update(resource_group_name=resource_group, peering_name=name)


def update_peering(cmd, client, body,
                   resource_group,
                   name,
                   kind,
                   location,
                   sku_name=None,
                   sku_tier=None,
                   sku_family=None,
                   sku_size=None,
                   direct=None,
                   exchange=None,
                   peering_location=None,
                   tags=None):
    return client.create_or_update(resource_group_name=resource_group, peering_name=name)


def list_peering(cmd, client,
                 resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()


def create_peering_prefix(cmd, client,
                          resource_group,
                          peering_service_name,
                          name,
                          prefix=None):
    return client.create_or_update(resource_group_name=resource_group, peering_service_name=peering_service_name, prefix_name=name)


def update_peering_prefix(cmd, client, body,
                          resource_group,
                          peering_service_name,
                          name,
                          prefix=None):
    return client.create_or_update(resource_group_name=resource_group, peering_service_name=peering_service_name, prefix_name=name)


def list_peering_prefix(cmd, client,
                        resource_group,
                        peering_service_name):
    return client.list_by_peering_service(resource_group_name=resource_group, peering_service_name=peering_service_name)


def create_peering_service(cmd, client,
                           resource_group,
                           name,
                           location,
                           peering_service_location=None,
                           peering_service_provider=None,
                           tags=None):
    return client.create_or_update(resource_group_name=resource_group, peering_service_name=name)


def update_peering_service(cmd, client, body,
                           resource_group,
                           name,
                           location,
                           peering_service_location=None,
                           peering_service_provider=None,
                           tags=None):
    return client.create_or_update(resource_group_name=resource_group, peering_service_name=name)


def list_peering_service(cmd, client,
                         resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list_by_subscription()
