# Method - ip_pool_list
## Description

	This service returns a list of IPv4 Address Pools matching optional condition(s).

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
	* pool_id - Pool ID
	* pool_name - Pool name
	* pool_class_name - Pool class name
	* pool_read_only - Pool is in read only mode
	* start_ip_addr
	* end_ip_addr
	* pool_start_ip_addr
	* pool_end_ip_addr
	* pool_size - Pool size
	* parent_subnet_name
	* parent_subnet_id - Parent Subnet ID
	* parent_subnet_size
	* vlsm_subnet_id
	* parent_subnet_class_name
	* subnet_name - Subnet name
	* vlsm_block_id
	* subnet_id - Subnet ID
	* subnet_start_ip_addr
	* subnet_end_ip_addr
	* subnet_size - Subnet size
	* subnet_class_name - Subnet class name
	* multistatus
	* pool_class_parameters - Pool class parameters
	* pool_class_parameters_properties - Class parameters properties
	* pool_class_parameters_inheritance_source
	* site_class_parameters - Space class parameters
	* site_class_parameters_properties - Class parameters properties
	* subnet_class_parameters - Subnet class parameters
	* subnet_class_parameters_properties - Subnet class parameters properties
