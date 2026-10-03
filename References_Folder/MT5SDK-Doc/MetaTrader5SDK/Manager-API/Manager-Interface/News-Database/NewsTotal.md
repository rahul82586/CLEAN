[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [News Database](../News-Database.md) / NewsTotal

[Previous](NewsUnsubscribe.md) | [Next](NewsNext.md)

# IMTManagerAPI::NewsTotal

Get the total number of news items received by the manager.

C++
    
    
    UINT  IMTManagerAPI::NewsTotal()

.NET
    
    
    uint  CIMTManagerAPI.NewsTotal()

Python
    
    
    ManagerAPI.NewsTotal()

### Return Value

The total number of news items received by the manager whose account is used for connecting to the server.

### Note

The method is valid only if the [IMTManagerAPI::PUMP_MODE_NEWS](../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
