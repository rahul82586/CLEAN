[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Dataset](../Dataset.md) / Create

[Previous](../Dataset.md) | [Next](RequestCreate.md)

# IMTServerAPI::DatasetCreate

Create a dataset object.
    
    
    IMTDataset*  IMTServerAPI::DatasetCreate()

### Return Value

Returns a pointer to the created object which implements the [IMTDataset](../../../Report-API/Dataset-Interfaces/IMTDataset.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTDataset::Release](../../../Report-API/Dataset-Interfaces/IMTDataset/Release.md) method of this object.
