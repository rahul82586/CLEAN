[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Logging Management](../Logging-Management.md) / SetLoggerWriteDebug

[Previous](SetLoggerFilePrefix.md) | [Next](../Service-Commands.md)

# MTWebAPI::SetLoggerWriteDebug

Enable/disable logging of debug messages of the Web API.
    
    
    void  MTWebAPI::SetLoggerWriteDebug(
       bool  $is_write      // Flag of logging
       )

### Parameters

**$is_write**  
[in] Flag of logging. The true value enables logging, false disables it.
