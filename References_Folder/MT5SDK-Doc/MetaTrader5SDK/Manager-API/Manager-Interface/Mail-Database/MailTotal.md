[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Mail Database](../Mail-Database.md) / MailTotal

[Previous](MailUnsubscribe.md) | [Next](MailNext.md)

# IMTManagerAPI::MailTotal

Get the total number of messages in the manager's mailbox.

C++
    
    
    UINT  IMTManagerAPI::MailTotal()

.NET
    
    
    uint  CIMTManagerAPI.MailTotal()

### Return Value

The total number of messages in a mailbox of the manager whose account is used for connecting to the server.

### Note

The method is valid only if the [IMTManagerAPI::PUMP_MODE_MAIL](../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
