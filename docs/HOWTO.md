When calling API endpoint for any [method](METHODS.md), you need to provide information Mandatory
could get back results. The way information are encoded is express in this document.

# Mandatory Parameters
Some methods require specific parameters combination. These parameters are listed in the method list below in the following format :

```
	(<required parameter #1> + (<required parameter #2>) | <required parameter #3>)
```

This means that you need to provide :
```
	<required parameter #1> and <required parameter #2>
```
or
```
	<required parameter #1> and <required parameter #3>
```

This parameters must be provided through a hash :

```
	puts sdsapi.ip_site_list(limit: 128, offset: 0, where: "site_name like '%test%'").body
```

# Filtering the result
Some methods allow to filter their output result using a WHERE or other parameters.

This clause can be applied on any output field combination using an SQL ANSI style clause.

## WHERE
```
	{"WHERE":"name LIKE 'eip-%' and time_to_expire<=3600"}
```

## ORDER BY
```
	{"ORDERBY":"alias_name, ip_name_type"}
```

## LIMIT / OFFSET
```
	{"LIMIT" : "100", "OFFSET" : "10"}
```
