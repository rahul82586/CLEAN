[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / HolidayNext

[Previous](HolidayTotal.md) | [Next](../Firewall.md)

# IMTServerAPI::HolidayNext

Gets a holiday configuration with the specified index.
    
    
    MTAPIRES  IMTServerAPI::HolidayNext(
       const UINT      pos,        // Position of the configuration
       IMTConHoliday*  config      // Holiday configuration object
       )

### Parameters

**pos**  
[in] Position of the configuration, starting with 0.

**config**  
[out] An object of holiday configuration. The config object must first be created using theIMTServerAPI::HolidayCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the configuration data of a holiday with a specified index to the config object.
