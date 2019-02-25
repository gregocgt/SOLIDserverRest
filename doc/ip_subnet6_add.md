# Method - ip_subnet6_add
## Description

	This service allows to add an IPv6 Network of type Subnet or Block.

## Mandatory Parameters

	(subnet6_addr + (subnet6_end_addr | subnet6_prefix) + (site_id | site_name | parent_subnet6_id))

## Available Input Parameters :

	* site_id - Space ID
	* site_name - Space name
	* vlsm_site_id - VLSM space ID
	* vlsm_site_name - VLSM space name
	* subnet6_id - Subnet6 ID
	* subnet6_name - Subnet6 name
	* subnet6_addr - Subnet6 start IP address
	* subnet6_end_addr - Subnet6 end IP address
	* subnet6_prefix - Subnet6 prefix
	* subnet_level - Subnet level
	* parent_subnet6_id - Parent subnet6 id
	* allow_tree_reparenting - Allow Tree Reparenting
	* relative_position - Relative position to a space
	* use_reversed_relative_position - Use the reversed relative position (start by the end)
	* subnet6_class_name - Subnet class name
	* network6_class_parameters - Network class parameters
	* subnet6_class_parameters - Subnet class parameters
	* subnet6_class_parameters_properties - Subnet class parameters properties
	* permit_invalid - Permit invalid (not a real subnet6/allow overlap)
	* permit_overlap - Permit overlap (obsolete)
	* permit_no_block6 - Allow creating subnet6 without block6
	* changed_waiting_state - Changed waiting state (internal)
	* is_terminal - Subnet is terminal
	* vlmvlan_id - Subnet VLAN ID
	* enabled - Manage/Unmanage
	* check - Launch service in read only
	* lock_network_broadcast - Lock network and broadcast addresses
	* keep_previous_param - Params to not overwrite for update
	* add_flag - new_edit/new_only/edit_only flag
	* class_parameters_to_delete - Class parameters to delete
	* network6_class_parameters_properties - Class parameters properties
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
