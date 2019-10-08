# Azure CLI Module Creation Report

## peering

### peering create

create a peering.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
|**--location**|str|The location of the resource.|/location|/location|
|--peering-service-location|str|The PeeringServiceLocation of the Customer.|/peering_service_location|/properties/peeringServiceLocation|
|--peering-service-provider|str|The MAPS Provider Name.|/peering_service_provider|/properties/peeringServiceProvider|
|--tags|dictionary|The resource tags.|/tags|/tags|

**Example: Create a  peering service**

```
peering create --resource-group rgName
        --name peeringServiceName
        --peering-service-location state1
        --peering-service-provider serviceProvider1
        --location eastus
```
### peering update

update a peering.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
|**--location**|str|The location of the resource.|/location|/location|
|--peering-service-location|str|The PeeringServiceLocation of the Customer.|/peering_service_location|/properties/peeringServiceLocation|
|--peering-service-provider|str|The MAPS Provider Name.|/peering_service_provider|/properties/peeringServiceProvider|
|--tags|dictionary|The resource tags.|/tags|/tags|

**Example: Update peering service tags**

```
peering update --resource-group rgName
        --name peeringServiceName
```
### peering delete

delete a peering.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the peering service.|peering_service_name|peeringServiceName|

**Example: Delete a peering service**

```
peering delete --resource-group rgName
        --name peeringServiceName
```
### peering list

list a peering.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
### peering show

show a peering.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
## peering prefixe

### peering prefixe create

create a peering prefixe.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--peering-service-name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
|**--name**|str|The name of the prefix.|prefix_name|prefixName|
|--prefix|str|The prefix from which your traffic originates.|/prefix|/properties/prefix|

**Example: Create or update a prefix for the peering service**

```
peering prefixe create --resource-group rgName
        --peering-service-name peeringServiceName
        --name peeringServicePrefixName
        --prefix 192.168.1.0/24
```
### peering prefixe update

update a peering prefixe.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--peering-service-name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
|**--name**|str|The name of the prefix.|prefix_name|prefixName|
|--prefix|str|The prefix from which your traffic originates.|/prefix|/properties/prefix|
### peering prefixe delete

delete a peering prefixe.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--peering-service-name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
|**--name**|str|The name of the prefix.|prefix_name|prefixName|

**Example: Delete a prefix associated with the peering service**

```
peering prefixe delete --resource-group rgName
        --peering-service-name peeringServiceName
        --name peeringServicePrefixName
```
### peering prefixe list

list a peering prefixe.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--peering-service-name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
### peering prefixe show

show a peering prefixe.

|Option|Type|Description|Path (SDK)|Path (swagger)|
|------|----|-----------|----------|--------------|
|**--resource-group**|str|The name of the resource group.|resource_group_name|resourceGroupName|
|**--peering-service-name**|str|The name of the peering service.|peering_service_name|peeringServiceName|
|**--name**|str|The name of the prefix.|prefix_name|prefixName|