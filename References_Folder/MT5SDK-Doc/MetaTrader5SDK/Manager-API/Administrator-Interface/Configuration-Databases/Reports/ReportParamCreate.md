[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / ReportParamCreate

[Previous](ReportModuleCreate.md) | [Next](ReportSubscribe.md)

# IMTAdminAPI::ReportParamCreate

Create an object of a report parameter.

C++
    
    
    IMTConParam*  IMTAdminAPI::ReportParamCreate()

.NET
    
    
    CIMTConParam  CIMTAdminAPI.ReportParamCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConParam](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConParam::Release](../../../../Configuration-Interfaces/Additional-Parameters/IMTConParam/Release.md) method of this object.
