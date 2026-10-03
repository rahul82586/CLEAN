[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Main API Interface](../Main-API-Interface.md) / Dataset

[Previous](Geo-Services/GeoResolveIPv6Bulk.md) | [Next](Dataset/Create.md)

# Dataset

The Server API enables highly efficient queries to the trading platform databases, with the flexible description of selection conditions (similar to SQL queries). The following two interfaces are provided for working with requests: [IMTDatasetField](../../Report-API/Dataset-Interfaces/IMTDatasetField.md) is used for describing conditions; [IMTDatasetRequest](../../Report-API/Dataset-Interfaces/IMTDatasetRequest.md) is used for describing a request as a set of conditions.

To request data perform the following steps:

1\. Use the [IMTServerAPI::DatasetRequestCreate](Dataset/RequestCreate.md) method to create a data request object ([IMTDatasetRequest](../../Report-API/Dataset-Interfaces/IMTDatasetRequest.md)).

2\. Use the [IMTServerAPI::DatasetCreate](Dataset/Create.md) method to create a dataset object to which the request results will be placed ([IMTDataset](../../Report-API/Dataset-Interfaces/IMTDataset.md))

3\. Use the [IMTDatasetRequest::FieldCreate](../../Report-API/Dataset-Interfaces/IMTDatasetRequest/FieldCreate.md) method to create the object of the field for which you wish to request data ([IMTDatasetField](../../Report-API/Dataset-Interfaces/IMTDatasetField.md)).

4\. Describe a request condition using [IMTDatasetField](../../Report-API/Dataset-Interfaces/IMTDatasetField.md) methods and add it to the request object using the [IMTDatasetRequest::FieldAdd](../../Report-API/Dataset-Interfaces/IMTDatasetRequest/FieldAdd.md) method.

5\. If you need to specify multiple conditions, repeat steps 3 and 4.

6\. Depending on the database from which you wish to query data, call [IMTServerAPI::OrderSelect*](Trade/Orders/OrderSelectByGroup.md), [IMTServerAPI::HistorySelect*](Trade/Orders/HistorySelectByGroup.md), [IMTServerAPI::DealSelect*](Trade/Deals/DealSelectByGroup.md) or [IMTServerAPI::DailySelect*](Daily-Reports/DailySelectByGroup.md), by passing the prepared request object to it ([IMTDatasetRequest](../../Report-API/Dataset-Interfaces/IMTDatasetRequest.md)).

7\. The request result will be added to the earlier created dataset object ([IMTDataset](../../Report-API/Dataset-Interfaces/IMTDataset.md)). Note that only fields marked as selected ([IMTDatasetField::FLAG_SELECT (#enfieldflags)](../../Report-API/Dataset-Interfaces/IMTDatasetField/Enumerations.md#enfieldflags)) are added to the resulting dataset.

The following methods are provided for operations with datasets in Server API:

Function | Purpose  
---|---  
[DatasetCreate](Dataset/Create.md) | Create a dataset object.  
[DatasetRequestCreate](../../Report-API/Main-Interface-of-Reports/Dataset/RequestCreate.md) | Create a data request object.
