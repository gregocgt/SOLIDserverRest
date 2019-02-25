# Method - ip_pool6_list
## Description

	This service returns a list of IPv6 Address Pools matching optional condition(s).

## Available Input Parameters :

	* where - Can be used to filter the result using any output field in an SQL fashion.
	* orderby - Can be used to order the result using any output field in an SQL fashion.
	* offset
	* limit

## Available Output Fields :

	* site_name - Space name
	* site_id - Space ID
	* site_description - Space description
	* site_class_name - Space class name
	* site_is_template - Space is a template
	* tree_path
	* pool6_id - Pool6 ID
	* pool6_name - Pool6 name
	* pool6_class_name - Pool6 class name
	* pool6_read_only - Pool6 is in read only mode
	* start_ip6_addr
	* end_ip6_addr
	* pool6_start_ip6_addr
	* pool6_end_ip6_addr
	* pool6_size
	* parent_subnet6_name
	* parent_subnet6_id - Parent Subnet6 ID
	* vlsm_subnet6_id
	* parent_subnet6_prefix
	* parent_subnet6_class_name
	* subnet6_name - Subnet6 name
	* vlsm_block6_id
	* subnet6_id - Subnet6 ID
	* subnet6_start_ip6_addr
	* subnet6_end_ip6_addr
	* subnet6_class_name - Subnet class name
	* subnet6_prefix - Subnet6 prefix
	* multistatus
	* pool6_class_parameters - Pool6 class parameters
	* pool6_class_parameters_properties - Class parameters properties
	* pool6_class_parameters_inheritance_source
	* site_class_parameters - Space class parameters
	* site_class_parameters_properties - Class parameters properties
	* subnet6_class_parameters - Subnet class parameters
	* subnet6_class_parameters_properties - Subnet class parameters properties
