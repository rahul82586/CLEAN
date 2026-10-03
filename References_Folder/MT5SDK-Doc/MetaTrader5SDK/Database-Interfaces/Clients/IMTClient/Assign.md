[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTClient::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTClient::Assign(
       const IMTClient*  deal      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.Assign(
       CIMTClient        deal      // Source object
       )

### Parameters

**client**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
