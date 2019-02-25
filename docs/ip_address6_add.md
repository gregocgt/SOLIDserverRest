# Method - ip_address6_add
## Description

	This service allows to add an IPv6 Address

## Mandatory Parameters

	(hostaddr + (site_id | site_name))

## Available Input Parameters :

	* site_id - Space ID
	* site_name - Space name
	* ip6_id - IP6 address ID
	* ip6_name - IP6 address name
	* ip6_mac_addr - IP6 address MAC address
	* ip6_addr - IP6 address
	* hostaddr - IP6 address
	* ip6_class_name - IP6 address class name
	* ip6_class_parameters - IP6 address class parameters
	* last_info - Information about the last call of the service
	* hostdev_id - Device ID
	* hostiface_id - Interface ID
	* iplport_id - NetChange port ID
	* keep_previous_param - Params to not overwrite for update
	* add_flag - new_edit/new_only/edit_only flag
	* class_parameters_to_delete - Class parameters to delete
	* ip6_class_parameters_properties - Class parameters properties
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
