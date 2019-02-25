# Method - ip_alias_delete
## Description

	This service allows to remove an Alias associated to an IPv4 Address.

## Mandatory Parameters

	(ip_name_id | (ip_name + (ip_id | (hostaddr + (site_id | site_name)))))

## Available Input Parameters :

	* site_id - Space ID
	* site_name - Space name
	* ip_id - IP address ID
	* ip_name_id - IP address alias ID
	* ip_name - IP address alias
	* ip_name_type - IP name type
	* ip_addr - IP address
	* hostaddr - IP address
	* old_ip - Old IP address name
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
