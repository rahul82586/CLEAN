[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / Currency

[Previous](MaxCapital.md) | [Next](MaxInvestors.md)

# IMTConFund::Currency

Get the currency in which the [maximum fund investment amount](MaxCapital.md) is specified.

C++
    
    
    LPCWSTR  IMTConFund::Currency()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConFund.Currency()

### Return Value

If successful, the method returns a pointer to a string with the currency name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFund](../IMTConFund.md) object.

# IMTConFund::Name

Set the currency in which the [maximum fund investment amount](MaxCapital.md) is specified.

C++
    
    
    MTAPIRES  IMTConFund::Currency(
       LPCWSTR  currency   // Currency
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.Currency(
       srting   currency  // Currency
       )

### Parameters

**currency**  
[in] The currency in which the maximum fund investment amount is specified.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The name length is limited to 16 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
