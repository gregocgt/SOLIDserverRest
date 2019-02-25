# Method - ip_alias_add
## Description

	This service allows to associate an Alias of type A or CNAME to an IPv4 Address.

## Mandatory Parameters

	(ip_name + (ip_id | (hostaddr + (site_id | site_name))))

## Available Input Parameters :

	* site_id - Space ID
	* site_name - Space name
	* ip_id - IP address ID
	* ip_name_id - IP address alias ID
	* ip_name - IP address alias
	* name - IP address alias
	* ip_name_type - IP name type
	* ip_addr - IP address
	* hostaddr - IP address
	* keep_previous_param - Params to not overwrite for update
	* add_flag - new_edit/new_only/edit_only flag
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
