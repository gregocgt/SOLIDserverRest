# Method - ip_site_update
## Description

	This service allows to update an IP address Space.

## Mandatory Parameters

	(site_id | site_name)

## Available Input Parameters :

	* site_id - Space ID
	* site_name - Space name
	* site_description - Space description
	* parent_site_id - Space parent ID
	* parent_site_name - Space parent name
	* site_class_name - Space class name
	* site_class_parameters - Space class parameters
	* site_is_template - Space is a template
	* keep_previous_param - Params to not overwrite for update
	* add_flag - new_edit/new_only/edit_only flag
	* class_parameters_to_delete - Class parameters to delete
	* site_class_parameters_properties - Class parameters properties
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
