[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / ManagerNext

[Previous](ManagerTotal.md) | [Next](ManagerGet.md)

# IMTReportAPI::ManagerNext

Gets a manager configuration with the specified index.
    
    
    MTAPIRES  IMTReportAPI::ManagerNext(
       const UINT      pos,         // Position of the configuration
       IMTConManager*  manager      // An object of manager configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**manager**  
[out] An object of manager configuration. The manager object must be first created using theIMTReportAPI::ManagerCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a manager with a specified index to the manager object.
