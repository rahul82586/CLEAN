[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupCreate

[Previous](../Groups.md) | [Next](GroupSymbolCreate.md)

# IMTReportAPI::GroupCreate

Create an object of the group configuration.
    
    
    IMTConGroup*  IMTReportAPI::GroupCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConGroup](../../../../Configuration-Interfaces/Groups/IMTConGroup.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConGroup::Release](../../../../Configuration-Interfaces/Groups/IMTConGroup/Release.md) method of this object.
