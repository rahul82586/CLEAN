[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Common](../Common.md) / Create

[Previous](../Common.md) | [Next](CreateAllocation.md)

# IMTReportAPI::CommonCreate

Create an object of the common platform configuration.
    
    
    IMTConCommon*  IMTReportAPI::CommonCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConCommon](../../../../Configuration-Interfaces/Common/IMTCon.md) interface. In case of failure, it returns Null.

### Note

The created object must be destroyed by calling the [IMTConCommon:Release](../../../../Configuration-Interfaces/Common/IMTConCommon/IMTCon-Release.md) method of this object.
