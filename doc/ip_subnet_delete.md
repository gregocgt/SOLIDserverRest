# Method - ip_subnet_delete
## Description

	This service allows to delete a specific IPv4 Network.

## Mandatory Parameters

	(subnet_id | (subnet_addr + (subnet_end_addr | subnet_size | subnet_mask | subnet_prefix) + (parent_subnet_id | subnet_level | relative_position) + (site_id | site_name)))

## Available Input Parameters :

	* site_id - Space ID
	* site_name - Space name
	* subnet_id - Subnet ID
	* parent_subnet_id - Parent Subnet ID
	* subnet_name - Subnet name
	* subnet_addr - Subnet start IP address
	* subnet_end_addr - Subnet end IP address
	* subnet_size - Subnet size
	* subnet_mask - Subnet mask
	* subnet_prefix - Subnet prefix
	* subnet_level - Subnet level
	* relative_position - Relative position to a space
	* use_reversed_relative_position - Use the reversed relative position (start by the end)
	* keep_previous_param - Params to not overwrite for update
	* no_rule_exec - Dont execute rules
	* only_rule_exec - Only execute rules
	* additional_parameters - Additional parameters passed to rules

## Available Output Fields :

	* errno - ID of the error
	* errmsg - Error message
	* msg - Message, information about service
	* severity - severity of the error
	* parameters - Missing parameters
	* param_format - format of the incorrect parameter
	* param_value - value of the incorrect parameter
	* param_name - name of the incorrect parameter
	* ret_oid - Return oid
