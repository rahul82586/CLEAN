[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../MT5WebAPI-Class.md) / Constructor

[Previous](../MT5WebAPI-Class.md) | [Next](Enumerations.md)

# Constructor

The following parameters can be set in the MT5WebAPI class constructor:
    
    
    MT5WebAPI.MT5WebAPI(
       string            agent,     // IP address
       CallbackLogWrite  logWrite   // Logging function
       )

### Parameters

**agent**  
[in] The name of the Web client. The default value is WEBAPI. This information will be displayed in the server log, along with information about the connection with the manager account.

**logWrite**  
[in] A pointer to the logging function implemented in your project (site). Thus, the Web API client will output its messages in the log of your site.

****
