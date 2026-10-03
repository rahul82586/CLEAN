[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Dataset Interfaces](../../Dataset-Interfaces.md) / [IMTDataset](../IMTDataset.md) / Release

[Previous](Enumerations.md) | [Next](Assign.md)

# IMTDataset::Release

Delete the current object.
    
    
    void  IMTDataset::Release()

### Note

The method can only be used in [Server API](../../../Server-API/README.md). For Report API, the IMTDataset interface collection is owned by the API object. The collection can be managed using the [IMTReportAPI::Dataset*](../../Main-Interface-of-Reports/Dataset.md) methods. For Server API, IMTDataset interfaces are owned by the API user. Objects are created using the [IMTServerAPI::DatasetCreate](../../../Server-API/Main-API-Interface/Dataset/Create.md) method, and they are released using IMTDataset::Release.
