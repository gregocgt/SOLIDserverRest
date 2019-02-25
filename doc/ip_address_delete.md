# Method - ip_address_delete
## Description

	This service allows to delete a specific IPv4 Address.

## Mandatory Parameters

	(ip_id | (hostaddr + (site_id | site_name)))

## Available Input Parameters :

	* site_id - Space ID
	* site_name - Space name
	* ip_id - IP address ID
	* name - IP address name
	* ip_name - IP address name
	* ip_addr - IP address
	* hostaddr - IP address
	* ip_class_name - IP address class name
	* ip_class_parameters - IP address class parameters
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
