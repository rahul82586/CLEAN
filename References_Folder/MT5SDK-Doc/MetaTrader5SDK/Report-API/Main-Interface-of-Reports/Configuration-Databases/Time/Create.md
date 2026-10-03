[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / Create

[Previous](../Time.md) | [Next](Current.md)

# IMTReportAPI::TimeCreate

Create an object of the time configuration.
    
    
    IMTConTime*  IMTReportAPI::TimeCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConTime](../../../../Configuration-Interfaces/Time/IMTCon.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConTime::Release](../../../../Configuration-Interfaces/Time/IMTConTime/IMTCon-Release.md) method of this object.
