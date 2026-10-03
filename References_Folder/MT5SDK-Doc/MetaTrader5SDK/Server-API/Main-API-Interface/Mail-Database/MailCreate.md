[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Mail Database](../Mail-Database.md) / MailCreate

[Previous](../Mail-Database.md) | [Next](MailSubscribe.md)

# IMTServeAPI::MailCreate

Create an object of a message in the internal mail system.
    
    
    IMTMail*  IMTServerAPI::MailCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTMail](../../../Database-Interfaces/Mail-Database/IMTMail.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTMail::Release](../../../Database-Interfaces/Mail-Database/IMTMail/Release.md) method of this object.
