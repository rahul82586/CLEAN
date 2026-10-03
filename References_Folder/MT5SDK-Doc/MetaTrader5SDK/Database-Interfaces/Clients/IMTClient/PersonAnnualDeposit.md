[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / PersonAnnualDeposit

[Previous](PersonNetWorth.md) | [Next](CompanyName.md)

# IMTClient::PersonAnnualDeposit

Get the amount of the client's annual deposit.

C++
    
    
    double  IMTClient::PersonAnnualDeposit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTClient.PersonAnnualDeposit()

### Return Value

Client's annual deposit in USD.

# IMTClient::PersonAnnualDeposit

Set the amount of the client's annual deposit.

C++
    
    
    MTAPIRES  IMTClient::PersonAnnualDeposit(
       const double  deposit    // Annual deposit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.PersonAnnualDeposit(
       double        deposit    // Annual deposit
       )

### Parameters

**deposit**  
[in] Client's annual deposit in USD.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
