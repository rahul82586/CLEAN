[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonNetWorth

[Previous](PersonAnnualIncome.md) | [Next](PersonAnnualDeposit.md)

# IMTClient::PersonAnnualIncome

Get the amount of the client's net assets.

C++
    
    
    double  IMTClient::PersonNetWorth()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTClient.PersonNetWorth()

### Return Value

Client's net assets in USD.

# IMTClient::PersonNetWorth

Set the amount of the client's net assets.

C++
    
    
    MTAPIRES  IMTClient::PersonNetWorth(
       const double  worth     // Net assets
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonNetWorth(
       double        worth     // Net assets
       )

### Parameters

**worth**  
[in] Client's net assets in USD.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
