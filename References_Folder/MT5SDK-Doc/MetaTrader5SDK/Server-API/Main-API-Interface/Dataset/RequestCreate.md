[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Dataset](../Dataset.md) / RequestCreate

[Previous](Create.md) | [Next](../Custom-Functions.md)

# IMTServerAPI::DatasetRequestCreate

Create a data request object.
    
    
    IMTDatasetRequest*  IMTServerAPI::DatasetRequestCreate()

### Return Value

Returns a pointer to the created object which implements the [IMTDatasetRequest](../../../Report-API/Dataset-Interfaces/IMTDatasetRequest.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTDatasetRequest::Release](../../../Report-API/Dataset-Interfaces/IMTDatasetRequest/Release.md) method of this object.
