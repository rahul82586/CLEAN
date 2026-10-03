[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonWealthSource

[Previous](PersonEducation.md) | [Next](PersonAnnualIncome.md)

# IMTClient::PersonWealthSource

Get the client's income source.

C++
    
    
    UINT  IMTClient::PersonWealthSource()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.PersonWealthSource()

### Return Value

A value from the [IMTClient::EnWealthSource (#enwealthsource)](Enumerations.md#enwealthsource) enumeration.

# IMTClient::PersonWealthSource

Set the client's income source.

C++
    
    
    MTAPIRES  IMTClient::PersonWealthSource(
       const UINT  source      // Source of income
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonWealthSource(
       uint        source      // Source of income
       )

### Parameters

**source**  
[in] Client's source of income. The value is passed using theIMTClient::EnWealthSourceenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
