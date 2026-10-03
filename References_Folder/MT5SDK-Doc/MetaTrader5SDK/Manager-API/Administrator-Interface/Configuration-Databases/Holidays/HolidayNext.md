[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / HolidayNext

[Previous](HolidayTotal.md) | [Next](../Firewall.md)

# IMTAdminAPI::HolidayNext

Gets a holiday configuration with the specified index.

C++
    
    
    MTAPIRES  IMTAdminAPI::HolidayNext(
       const UINT      pos,        // Position of the configuration
       IMTConHoliday*  config      // Holiday configuration object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.HolidayNext(
       uint            pos,        // Position of the configuration
       CIMTConHoliday  obj         // Holiday configuration object
       )

Python
    
    
    AdminAPI.HolidayNext(
       pos             # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**config**  
[out] An object of holiday configuration. The config object must first be created using theIMTAdminAPI::HolidayCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a holiday with a specified index to the config object.
