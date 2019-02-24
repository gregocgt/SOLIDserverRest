# Method - ip_pool6_delete
## Description

	This service allows to delete a specific IPv6 Address Pool.

## Mandatory Parameters

	(pool6_id | (start_addr + end_addr + (subnet6_id | site_id | site_name)))

## Available Input Parameters :

	* site_id - Space ID
	* site_name - Space name
	* subnet6_id - Subnet6 ID
	* pool6_id - Pool6 ID
	* start_addr - Pool6 start IP address
	* end_addr - Pool6 end IP address
	* pool6_class_name - Pool6 class name
	* pool6_class_parameters - Pool6 class parameters
	* pool6_read_only - Pool6 is in read only mode
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
