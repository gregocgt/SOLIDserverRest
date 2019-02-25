# Method - ip_pool6_add
## Description

	This service allows to add an IPv6 Address Pool.

## Mandatory Parameters

	(start_addr + end_addr + (subnet6_id | site_id | site_name))

## Available Input Parameters :

	* site_id - Space ID
	* site_name - Space name
	* subnet6_id - Subnet6 ID
	* pool6_id - Pool6 ID
	* pool6_name - Pool6 name
	* start_addr - Pool6 start IP address
	* end_addr - Pool6 end IP address
	* pool6_class_name - Pool6 class name
	* pool6_class_parameters - Pool6 class parameters
	* pool6_read_only - Pool6 is in read only mode
	* keep_previous_param - Params to not overwrite for update
	* add_flag - new_edit/new_only/edit_only flag
	* class_parameters_to_delete - Class parameters to delete
	* pool6_class_parameters_properties - Class parameters properties
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
