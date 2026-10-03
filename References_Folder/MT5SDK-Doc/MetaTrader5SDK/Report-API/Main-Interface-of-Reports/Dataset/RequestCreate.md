[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Dataset](../Dataset.md) / RequestCreate

[Previous](Next.md) | [Next](../Data-cache.md)

# IMTReportAPI::DatasetRequestCreate

Create a data request object.
    
    
    IMTDatasetRequest*  IMTReportAPI::DatasetRequestCreate()

### Return Value

Returns a pointer to the created object which implements the [IMTDatasetRequest](../../Dataset-Interfaces/IMTDatasetRequest.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTDatasetRequest::Release](../../Dataset-Interfaces/IMTDatasetRequest/Release.md) method of this object.
