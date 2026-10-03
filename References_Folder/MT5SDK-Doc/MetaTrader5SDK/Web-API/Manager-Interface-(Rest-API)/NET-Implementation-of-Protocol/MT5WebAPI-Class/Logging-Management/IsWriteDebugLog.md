[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Logging Management](../Logging-Management.md) / IsWriteDebugLog

[Previous](../Logging-Management.md) | [Next](../Service-Commands.md)

# MT5WebAPI.IsWriteDebugLog

Get the mode of output of debug messages in the Web API journal.
    
    
    bool  MT5WebAPI.IsWriteDebugLog()

### Return Value

If logging of debug messages is enabled, it returns true. Otherwise, it returns false.

### Note

Web client messages appear on the common journal of a project (site). A pointer to the logging function is passed in the [MT5WebAPI class constructor](../Constructor.md).

# MT5WebAPI.IsWriteDebugLog

Set the mode of output of debug messages in the Web API journal.
    
    
    void  MT5WebAPI.IsWriteDebugLog(
       bool  value      // Logging of debug messages
       )

### Parameters

**value**  
[in] The mode of logging of debug messages. To log messages set true. To disable logging set false.

### Note

Web client messages appear on the common journal of a project (site). A pointer to the logging function is passed in the [MT5WebAPI class constructor](../Constructor.md).
