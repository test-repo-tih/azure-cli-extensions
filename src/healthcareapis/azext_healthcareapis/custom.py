# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument


def create_healthcareapis(cmd, client,
                          resource_group,
                          name,
                          kind,
                          location,
                          access_policies_object_id,
                          tags=None,
                          etag=None,
                          cosmos_db_offer_throughput=None,
                          authentication_authority=None,
                          authentication_audience=None,
                          authentication_smart_proxy_enabled=None,
                          cors_origins=None,
                          cors_headers=None,
                          cors_methods=None,
                          cors_max_age=None,
                          cors_allow_credentials=None):
    body = {}
    body['kind'] = kind  # str
    body['location'] = location  # str
    body['tags'] = tags  # dictionary
    body['etag'] = etag  # str
    body.setdefault('access_policies', {})['object_id'] = access_policies_object_id  # str
    body.setdefault('cosmos_db_configuration', {})['offer_throughput'] = cosmos_db_offer_throughput  # number
    body.setdefault('authentication_configuration', {})['authority'] = authentication_authority  # str
    body.setdefault('authentication_configuration', {})['audience'] = authentication_audience  # str
    body.setdefault('authentication_configuration', {})['smart_proxy_enabled'] = authentication_smart_proxy_enabled  # boolean
    body.setdefault('cors_configuration', {})['origins'] = None if cors_origins is None else cors_origins.split(',')
    body.setdefault('cors_configuration', {})['headers'] = None if cors_headers is None else cors_headers.split(',')
    body.setdefault('cors_configuration', {})['methods'] = None if cors_methods is None else cors_methods.split(',')
    body.setdefault('cors_configuration', {})['max_age'] = cors_max_age  # number
    body.setdefault('cors_configuration', {})['allow_credentials'] = cors_allow_credentials  # boolean
    return client.create_or_update(resource_group_name=resource_group, resource_name=name, service_description=body)


def update_healthcareapis(cmd, client,
                          resource_group,
                          name,
                          kind=None,
                          location=None,
                          tags=None,
                          etag=None,
                          access_policies_object_id=None,
                          cosmos_db_offer_throughput=None,
                          authentication_authority=None,
                          authentication_audience=None,
                          authentication_smart_proxy_enabled=None,
                          cors_origins=None,
                          cors_headers=None,
                          cors_methods=None,
                          cors_max_age=None,
                          cors_allow_credentials=None):
    body = client.get(resource_group_name=resource_group, resource_name=name).as_dict()
    body.kind = kind  # str
    body.location = location  # str
    body.tags = tags  # dictionary
    body.etag = etag  # str
    body.access_policies.object_id = access_policies_object_id  # str
    body.cosmos_db_configuration.offer_throughput = cosmos_db_offer_throughput  # number
    body.authentication_configuration.authority = authentication_authority  # str
    body.authentication_configuration.audience = authentication_audience  # str
    body.authentication_configuration.smart_proxy_enabled = authentication_smart_proxy_enabled  # boolean
    body.cors_configuration.origins = None if cors_origins is None else cors_origins.split(',')
    body.cors_configuration.headers = None if cors_headers is None else cors_headers.split(',')
    body.cors_configuration.methods = None if cors_methods is None else cors_methods.split(',')
    body.cors_configuration.max_age = cors_max_age  # number
    body.cors_configuration.allow_credentials = cors_allow_credentials  # boolean
    return client.create_or_update(resource_group_name=resource_group, resource_name=name, service_description=body)


def delete_healthcareapis(cmd, client,
                          resource_group,
                          name):
    return client.delete(resource_group_name=resource_group, resource_name=name)


def list_healthcareapis(cmd, client,
                        resource_group):
    if resource_group is not None:
        return client.list_by_resource_group(resource_group_name=resource_group)
    return client.list()


def list_healthcareapis(cmd, client):
    return client.list()
