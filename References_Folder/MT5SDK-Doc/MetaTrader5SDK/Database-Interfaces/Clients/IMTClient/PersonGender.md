[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonGender

[Previous](PersonCitizenship.md) | [Next](PersonTaxID.md)

# IMTClient::PersonGender

Get the client's gender.

C++
    
    
    UINT  IMTClient::PersonGender()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTClient.PersonGender()

### Return Value

A value from the [IMTClient::EnGender (#engender)](Enumerations.md#engender) enumeration.

# IMTClient::PersonGender

Set the client's gender.

C++
    
    
    MTAPIRES  IMTClient::PersonGender(
       const UINT  gender    // Client gender
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonGender(
       uint        gender    // Client gender
       )

### Parameters

**gender**  
[in] Client gender. The gender is passed using theIMTClient::EnGenderenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
