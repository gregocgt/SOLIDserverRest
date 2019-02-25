# Method - ip_site_list
## Description

	This service returns a list of IP address Spaces matching optional condition(s).

## Available Input Parameters :

	* where - Can be used to filter the result using any output field in an SQL fashion.
	* orderby - Can be used to order the result using any output field in an SQL fashion.
	* offset
	* limit

## Available Output Fields :

	* site_is_template - Space is a template
	* site_id - Space ID
	* tree_level
	* tree_path
	* tree_id_path
	* site_is_default
	* site_name - Space name
	* site_description - Space description
	* parent_site_id - Space parent ID
	* parent_site_name - Space parent name
	* site_class_name - Space class name
	* parent_site_class_name
	* row_enabled
	* multistatus
	* site_class_parameters - Space class parameters
	* site_class_parameters_properties - Class parameters properties
	* site_class_parameters_inheritance_source
	* parent_site_class_parameters
	* parent_site_class_parameters_properties
