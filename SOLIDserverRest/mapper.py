#!/usr/bin/python
# -*-coding:Utf-8 -*
##############################################

"""
set of values used to map calls from names to API endpoints
and method to use in REST calls
"""
__all__ = ["SERVICE_MAPPER", "METHOD_MAPPER"]

SERVICE_MAPPER = {
    'ip_site_add': 'ip_site_add',
    'ip_site_create': 'ip_site_add',
    'ip_site_update': 'ip_site_add',
    'ip_site_count': 'ip_site_count',
    'ip_site_list': 'ip_site_list',
    'ip_site_info': 'ip_site_info',
    'ip_site_delete': 'ip_site_delete',

    'ip_subnet_add': 'ip_subnet_add',
    'ip_subnet_update': 'ip_subnet_add',
    'ip_subnet_count': 'ip_block_subnet_count',
    'ip_subnet_list': 'ip_block_subnet_list',
    'ip_subnet_info': 'ip_block_subnet_info',
    'ip_subnet_delete': 'ip_subnet_delete',
    'ip_subnet_find_free': 'ip_find_free_subnet',

    'ip_subnet6_add': 'ip6_subnet6_add',
    'ip_subnet6_update': 'ip6_subnet6_add',
    'ip_subnet6_count': 'ip6_block6_subnet6_count',
    'ip_subnet6_list': 'ip6_block6_subnet6_list',
    'ip_subnet6_info': 'ip6_block6_subnet6_info',
    'ip_subnet6_delete': 'ip6_subnet6_delete',
    'ip_subnet6_find_free': 'ip6_find_free_subnet6',

    'ip_pool_add': 'ip_pool_add',
    'ip_pool_update': 'ip_pool_add',
    'ip_pool_count': 'ip_pool_count',
    'ip_pool_list': 'ip_pool_list',
    'ip_pool_info': 'ip_pool_info',
    'ip_pool_delete': 'ip_pool_delete',

    'ip_pool6_add': 'ip6_pool6_add',
    'ip_pool6_update': 'ip6_pool6_add',
    'ip_pool6_count': 'ip6_pool6_count',
    'ip_pool6_list': 'ip6_pool6_list',
    'ip_pool6_info': 'ip6_pool6_info',
    'ip_pool6_delete': 'ip6_pool6_delete',

    'ip_address_add': 'ip_add',
    'ip_address_update': 'ip_add',
    'ip_address_count': 'ip_address_count',
    'ip_address_list': 'ip_address_list',
    'ip_address_info': 'ip_address_info',
    'ip_address_delete': 'ip_delete',
    'ip_address_find_free': 'ip_find_free_address',

    'ip_address6_add': 'ip6_address6_add',
    'ip_address6_update': 'ip6_address6_add',
    'ip_address6_count': 'ip6_address6_count',
    'ip_address6_list': 'ip6_address6_list',
    'ip_address6_info': 'ip6_address6_info',
    'ip_address6_delete': 'ip6_address6_delete',
    'ip_address6_find_free': 'ip6_find_free_address6',

    'ip_alias_add': 'ip_alias_add',
    'ip_alias_list': 'ip_alias_list',
    'ip_alias_delete': 'ip_alias_delete',

    'ip_alias6_add': 'ip6_alias_add',
    'ip_alias6_list': 'ip6_alias_list',
    'ip_alias6_delete': 'ip6_alias_delete',

    'dns_rr_list': 'dns_rr_list',
    'dns_rr_add': 'dns_rr_add',
    'dns_rr_delete': 'dns_rr_delete',

    'dns_server_list': 'dns_server_list',

    'app_application_list': 'app_application_list',
    'app_application_add': 'app_application_add',
    'app_application_delete': 'app_application_delete',
    'app_application_count': 'app_application_count',
    'app_application_info': 'app_application_info',
    'app_application_delete': 'app_application_delete',

    'app_pool_add': 'app_pool_add',
    'app_pool_update': 'app_pool_add',
    'app_pool_list': 'app_pool_list',
    'app_pool_count': 'app_pool_count',
    'app_pool_info': 'app_pool_info',
    'app_pool_delete': 'app_pool_delete',

    'app_node_add': 'app_node_add',
    'app_node_update': 'app_node_add',
    'app_node_info': 'app_node_info',
    'app_node_count': 'app_node_count',
    'app_node_list': 'app_node_list',
    'app_node_delete': 'app_node_delete',

    'app_healthcheck_count': 'app_healthcheck_count',
    'app_healthcheck_info': 'app_healthcheck_info',
    'app_healthcheck_list': 'app_healthcheck_list',

}

METHOD_MAPPER = {
    'add': 'POST',
    'update': 'PUT',
    'count': 'GET',
    'list': 'GET',
    'info': 'GET',
    'find_free': "OPTIONS",
    'create': 'POST',
    'delete': "DELETE",

}
