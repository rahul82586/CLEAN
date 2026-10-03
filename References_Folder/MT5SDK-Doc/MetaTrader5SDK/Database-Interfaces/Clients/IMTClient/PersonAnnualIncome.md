[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonAnnualIncome

[Previous](PersonWealthSource.md) | [Next](PersonNetWorth.md)

# IMTClient::PersonAnnualIncome

Get the client's annual income amount

C++
    
    
    double  IMTClient::PersonAnnualIncome()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTClient.PersonAnnualIncome()

### Return Value

Client's annual income in USD.

# IMTClient::PersonAnnualIncome

Set the client's annual income amount

C++
    
    
    MTAPIRES  IMTClient::PersonAnnualIncome(
       const double  income    // Annual income
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonAnnualIncome(
       double        income    // Annual income
       )

### Parameters

**income**  
[in] Client's annual income in USD.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
