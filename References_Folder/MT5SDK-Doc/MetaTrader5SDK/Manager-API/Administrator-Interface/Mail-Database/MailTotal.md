[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Mail Database](../Mail-Database.md) / MailTotal

[Previous](MailUnsubscribe.md) | [Next](MailNext.md)

# IMTAdminAPI::MailTotal

Get the total number of messages in the manager's mailbox.

C++
    
    
    UINT  IMTAdminAPI::MailTotal()

.NET
    
    
    uint  CIMTAdminAPI.MailTotal()

### Return Value

The total number of messages in a mailbox of the manager whose account is used for connecting to the server.

### Note

The method is valid only if the [IMTAdminAPI::PUMP_MODE_MAIL](../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
