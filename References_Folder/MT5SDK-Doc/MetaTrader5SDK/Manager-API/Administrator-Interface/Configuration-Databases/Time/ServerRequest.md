[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Time](../Time.md) / ServerRequest

[Previous](Server.md) | [Next](../Holidays.md)

# IMTAdminAPI::TimeServerRequest

Get the current time of the trading server.

C++
    
    
    MTAPIRES  IMTAdminAPI::TimeServerRequest(
       INT64&       time_msc    // server time
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.TimeServerRequest(
       out long     time_msc    // server time
       )

Python
    
    
    AdminAPI.TimeServerRequest()

### Parameters

**time_msc**  
[out] The current trading time of the platform in the number of milliseconds elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Unlike [TimeServer](Server.md), the TimeServerRequest section directly requests time from the trading server rather than calculating it.

In all configurations, databases and logs, the platform trading time is used, except where explicitly stated otherwise.
