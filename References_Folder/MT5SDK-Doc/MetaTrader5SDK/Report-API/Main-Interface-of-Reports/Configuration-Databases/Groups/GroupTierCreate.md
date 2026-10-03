[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupTierCreate

[Previous](GroupCommissionCreate.md) | [Next](GroupTotal.md)

# IMTReportAPI::GroupTierCreate

Create an object of commission range configuration for a group.
    
    
    IMTConCommTier*  IMTReportAPI::GroupTierCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConCommTier](../../../../Configuration-Interfaces/Groups/IMTConCommTier.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConCommTier::Release](../../../../Configuration-Interfaces/Groups/IMTConCommTier/Release.md) method of this object.
