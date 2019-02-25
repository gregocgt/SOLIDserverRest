# Method - ip_address_add
## Description

	This service allows to add an IPv4 Address.

## Mandatory Parameters

	(hostaddr + (site_id | site_name))

## Available Input Parameters :

	* site_id - Space ID
	* site_name - Space name
	* ip_id - IP address ID
	* name - IP address name
	* ip_name - IP address name
	* mac_addr - IP address MAC address
	* ip_addr - IP address
	* hostaddr - IP address
	* ip_class_name - IP address class name
	* ip_class_parameters - IP address class parameters
	* hostdev_id - Device ID
	* hostiface_id - Interface ID
	* iplport_id - NetChange port ID
	* last_info - Information about the last call of the service
	* dhcphost_id - DHCP Static ID
	* dhcplease_id - DHCP Lease ID
	* check - Launch service in read only
	* check_is_dhcp_ip - Check if the IP is valid for DHCP
	* keep_previous_param - Params to not overwrite for update
	* add_flag - new_edit/new_only/edit_only flag
	* class_parameters_to_delete - Class parameters to delete
	* ip_class_parameters_properties - Class parameters properties
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
