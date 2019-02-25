# Method - ip_subnet6_delete
## Description

	This service allows to delete a specific IPv6 Network.

## Mandatory Parameters

	(subnet6_id | (subnet6_addr + (subnet6_end_addr | subnet6_prefix) + (parent_subnet6_id | subnet_level | relative_position) + (site_id | site_name)))

## Available Input Parameters :

	* site_id - Space ID
	* site_name - Space name
	* subnet6_id - Subnet6 ID
	* parent_subnet6_id - Parent Subnet6 ID
	* subnet6_name - Subnet6 name
	* subnet6_addr - Subnet6 start IP address
	* subnet6_end_addr - Subnet6 end IP address
	* subnet6_prefix - Subnet6 prefix
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
