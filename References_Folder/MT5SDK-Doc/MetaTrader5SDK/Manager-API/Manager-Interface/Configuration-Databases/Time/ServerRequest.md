[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / ServerRequest

[Previous](Server.md) | [Next](../Holidays.md)

# IMTManagerAPI::TimeServerRequest

Get the current time of the trading server.

C++
    
    
    MTAPIRES  IMTManagerAPI::TimeServerRequest(
       INT64&       time_msc    // server time
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TimeServerRequest(
       out long     time_msc    // server time
       )

Python
    
    
    ManagerAPI.TimeServerRequest()

### Parameters

**time_msc**  
[out] The current trading time of the platform in the number of milliseconds elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Unlike [TimeServer](Server.md), the TimeServerRequest section directly requests time from the trading server rather than calculating it.
