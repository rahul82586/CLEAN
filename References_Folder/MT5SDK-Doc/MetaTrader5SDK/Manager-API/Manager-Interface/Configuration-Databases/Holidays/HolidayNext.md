[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / HolidayNext

[Previous](HolidayTotal.md) | [Next](../Groups.md)

# IMTManagerAPI::HolidayNext

Gets a holiday configuration with the specified index.

C++
    
    
    MTAPIRES  IMTManagerAPI::HolidayNext(
       const UINT      pos,        // Position of the configuration
       IMTConHoliday*  config      // Holiday configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.HolidayNext(
       uint            pos,        // Position of the configuration
       CIMTConHoliday  obj         // Holiday configuration object
       )

Python
    
    
    ManagerAPI.HolidayNext(
       pos             # Position of the configuration
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**config**  
[out] An object of holiday configuration. The config object must first be created using theIMTManagerAPI::HolidayCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a holiday with a specified index to the config object. The method is valid only if the [IMTManagerAPI::PUMP_MODE_HOLIDAYS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
