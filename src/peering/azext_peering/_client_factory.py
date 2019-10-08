# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


def cf_peering(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from .vendored_sdks.peering import PeeringManagementClient
    return get_mgmt_service_client(cli_ctx, PeeringManagementClient)


def cf_peer_asns(cli_ctx, *_):
    return cf_peering(cli_ctx).peer_asns


def cf_peerings(cli_ctx, *_):
    return cf_peering(cli_ctx).peerings


def cf_prefixes(cli_ctx, *_):
    return cf_peering(cli_ctx).prefixes


def cf_peering_services(cli_ctx, *_):
    return cf_peering(cli_ctx).peering_services
