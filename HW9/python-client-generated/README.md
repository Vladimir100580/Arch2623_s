# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudsApi(swagger_client.ApiClient(configuration))
cloud_id = 'cloud_id_example' # str | Идентификатор заказа в облаке

try:
    # Отмена заказа в облаке по ID
    api_instance.cancel_cloud_by_id(cloud_id)
except ApiException as e:
    print("Exception when calling CloudsApi->cancel_cloud_by_id: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.CloudsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Error() # Error |  (optional)

try:
    # Создание заказа в облаке
    api_response = api_instance.create_cloud(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudsApi->create_cloud: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.CloudsApi(swagger_client.ApiClient(configuration))

try:
    # Метод получения списка ресурсов на облаке
    api_response = api_instance.get_all_clouds()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudsApi->get_all_clouds: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.CloudsApi(swagger_client.ApiClient(configuration))
cloud_id = 'cloud_id_example' # str | Идентификатор заказа в облаке

try:
    # Метод получения заказа по ID
    api_response = api_instance.get_cloud(cloud_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudsApi->get_cloud: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8080/api/v1/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CloudsApi* | [**cancel_cloud_by_id**](docs/CloudsApi.md#cancel_cloud_by_id) | **DELETE** /clouds/{cloud_id} | Отмена заказа в облаке по ID
*CloudsApi* | [**create_cloud**](docs/CloudsApi.md#create_cloud) | **POST** /clouds | Создание заказа в облаке
*CloudsApi* | [**get_all_clouds**](docs/CloudsApi.md#get_all_clouds) | **GET** /clouds | Метод получения списка ресурсов на облаке
*CloudsApi* | [**get_cloud**](docs/CloudsApi.md#get_cloud) | **GET** /clouds/{cloud_id} | Метод получения заказа по ID

## Documentation For Models

 - [Cloud](docs/Cloud.md)
 - [Clouds](docs/Clouds.md)
 - [Error](docs/Error.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

