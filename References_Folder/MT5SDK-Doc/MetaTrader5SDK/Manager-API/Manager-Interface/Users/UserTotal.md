[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserTotal

[Previous](UserUpdateBatchArray.md) | [Next](UserGet.md)

# IMTManagerAPI::UserTotal

Get the total number of users on a trade server.

C++
    
    
    UINT  IMTManagerAPI::UserTotal()

.NET
    
    
    uint  CIMTManagerAPI.UserTotal()

Python
    
    
    ManagerAPI.UserTotal()

### Return Value

The number of users on a trade server.

### Note

The method is valid only if the [IMTManagerAPI::PUMP_MODE_USERS](../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
