[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Report Parameters](../Report-Parameters.md) / ParamCreate

[Previous](../Report-Parameters.md) | [Next](ParamTotal.md)

# IMTReportAPI::ParamCreate

Create an object of a report parameter.
    
    
    IMTConParam*  IMTReportAPI::ParamCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConParam](../../../Configuration-Interfaces/Additional-Parameters/IMTConParam.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConParam::Release](../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Release.md) method of this object.
