[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupTotal

[Previous](GroupUpdateBatch.md) | [Next](GroupNext.md)

# IMTManagerAPI::GroupTotal

The total number of group configurations available in the platform.

C++
    
    
    UINT  IMTManagerAPI::GroupTotal()

.NET
    
    
    uint  CIMTManagerAPI.GroupTotal()

Python
    
    
    ManagerAPI.GroupTotal()

### Return Value

The number of group configurations in the trading platform.

### Note

The method is valid only if the [IMTManagerAPI::PUMP_MODE_GROUPS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
