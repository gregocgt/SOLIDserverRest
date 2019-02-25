# Method - ip_pool_update
## Description

	This service allows to update an IPv4 Address Pool.

## Mandatory Parameters

	(pool_id | (start_addr + (end_addr | pool_size) + (subnet_id | site_id | site_name)))

## Available Input Parameters :

	* site_id - Space ID
	* site_name - Space name
	* subnet_id - Subnet ID
	* pool_id - Pool ID
	* pool_name - Pool name
	* start_addr - Pool start IP address
	* end_addr - Pool end IP address
	* pool_size - Pool size
	* pool_class_name - Pool class name
	* pool_class_parameters - Pool class parameters
	* pool_read_only - Pool is in read only mode
	* keep_previous_param - Params to not overwrite for update
	* add_flag - new_edit/new_only/edit_only flag
	* class_parameters_to_delete - Class parameters to delete
	* pool_class_parameters_properties - Class parameters properties
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
