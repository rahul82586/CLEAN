[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Mail Database](../Mail-Database.md) / MailCreate

[Previous](../Mail-Database.md) | [Next](MailSend.md)

# IMTGatewayAPI::MailCreate

Create an object of a message in the internal mail system.

C++
    
    
    IMTMail*  IMTGatewayAPI::MailCreate()

.NET
    
    
    CIMTMail  CIMTGatewayAPI.MailCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTMail](../../../Database-Interfaces/Mail-Database/IMTMail.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTMail::Release](../../../Database-Interfaces/Mail-Database/IMTMail/Release.md) method of this object.
