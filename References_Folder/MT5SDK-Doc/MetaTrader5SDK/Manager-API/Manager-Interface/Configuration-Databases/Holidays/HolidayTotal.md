[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Holidays](../Holidays.md) / HolidayTotal

[Previous](HolidayUnsubscribe.md) | [Next](HolidayNext.md)

# IMTManagerAPI::HolidayTotal

The total number of configurations of holidays available in the platform.

C++
    
    
    UINT  IMTManagerAPI::HolidayTotal()

.NET
    
    
    uint  CIMTManagerAPI.HolidayTotal()

Python
    
    
    ManagerAPI.HolidayTotal()

### Return Value

The number of configurations of holidays in the trading platform.

### Note

The method is valid only if the [IMTManagerAPI::PUMP_MODE_HOLIDAYS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
