[![Build status](https://travis-ci.com/gregocgt/SOLIDserverRest.svg?branch=master)](https://https://travis-ci.com/gregocgt/SOLIDserverRest)
[![License](https://img.shields.io/badge/License-BSD%202--Clause-blue.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![Updates](https://pyup.io/repos/github/gregocgt/SOLIDserverRest/shield.svg)](https://pyup.io/repos/github/gregocgt/SOLIDserverRest/)
[![Python 3](https://pyup.io/repos/github/gregocgt/SOLIDserverRest/python-3-shield.svg)](https://pyup.io/repos/github/gregocgt/SOLIDserverRest/)
[![Codecov branch](https://codecov.io/gh/gregocgt/SOLIDserverRest/branch/next-version/graph/badge.svg)](https://codecov.io/gh/gregocgt/SOLIDserverRest)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/SOLIDserverRest.svg)
[![Documentation Status](https://readthedocs.org/projects/solidserverrest/badge/?version=latest)](https://solidserverrest.readthedocs.io/en/latest/?badge=latest)

# SOLIDserverRest

This 'SOLIDserverRest' allows to easily interact with [SOLIDserver](https://www.efficientip.com/products/solidserver/)'s REST API.
It allows managing all IPAM objects through CRUD operations.

* ***Free software***: BSD2 License

This 'SOLIDserverRest' is compatible with [SOLIDserver](https://www.efficientip.com/products/solidserver/) version 6.0.1P3 and higher.

# Install
Install 'SOLIDserverRest' using pip in your virtualenv:

```
	pip install SOLIDserverRest
```

# Usage
## Using the SOLIDserverRest object

1. **Declare endpoint API point**
Set the API endpoint you want to talk with through API. Could use an IP address
(v4 or v6) or a host name
* host = IP address of the SOLIDserver server
```
con = SOLIDserverRest("fqdn_host.org")
```

2. **Specify connection method**
Only native connection is supported for this version, using SSD default method
and providing authentication through headers in the requests with information
encoded in base64

* user = user who want to use
* password = password of the user

```python
	con.use_native_ssd(user="apiuser", password="apipwd")
```

3. **Request to SOLIDserver API**

You need parameters:
* method = choose your method in the list below
* parameters = Python dico with parameters you want to use
* ssl_verify = this option permits to check your server SSL certificate.
To check the certificate, you must set ssl_verify=True
```python
	rest_answer = con.query("method", "parameters", ssl_verify=True)
```

4. **Analyze answer**

* rest_answer => object name
* rest_answer.status_code => current http answer code set in the object
* rest_answer.content => Answer core from SOLIDserver API set in the object

Example:
```python
	print(rest_answer)
	print(rest_answer.status_code)
	print(rest_answer.content)
```

# Methods that could be used
Methods are organized to match the ontology used in SOLIDServer, you will find:
* Sites - address spaces
* Subnets (v4 and v6)
* Pools (v4 and v6)
* Addresses (v4 and v6)
* Aliases (v4 and v6)

More information about supported methods in the [specific document](docs/METHODS.md)

## Supported SSD modules in methods are:
-ip (IPAM - IP Address Management)
