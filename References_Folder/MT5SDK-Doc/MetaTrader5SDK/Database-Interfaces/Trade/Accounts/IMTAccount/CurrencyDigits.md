[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / CurrencyDigits

[Previous](Login.md) | [Next](Balance.md)

# IMTAccount::CurrencyDigits

Get the number of decimal places in the account deposit currency.

C++
    
    
    UINT  IMTAccount::CurrencyDigits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTAccount.CurrencyDigits()

### Return Value

Number of decimal places.

# IMTAccount::CurrencyDigits

Set the number of decimal places in the account deposit currency.

C++
    
    
    MTAPIRES  IMTAccount::CurrencyDigits(
       const UNIT  digits      // Accuracy
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.CurrencyDigits(
       uint        digits      // Accuracy
       )

### Parameters

**digits**  
[in] Number of decimal places.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
