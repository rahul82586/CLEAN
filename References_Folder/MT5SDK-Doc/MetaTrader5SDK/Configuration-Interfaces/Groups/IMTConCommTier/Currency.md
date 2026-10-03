[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommTier](../IMTConCommTier.md) / Currency

[Previous](RangeTo.md) | [Next](../../Floating-Margin.md)

# IMTConCommTier::Currency

Gets commission calculation currency.

C++
    
    
    LPCWSTR  IMTConCommTier::Currency()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommTier.Currency()

Python (Manager API)
    
    
    MTConCommTier.Currency

### Return Value

The currency used for commission calculation.

### Note

The currency has a three-letter representation, e.g. EUR, USD, JPY etc.

# IMTConCommTier::Currency

Gets commission calculation currency.

C++
    
    
    MTAPIRES  IMTConCommTier::Currency(
       LPCWSTR  currency      // Currency name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommTier.Currency(
       string   currency      // Currency name
       )

Python (Manager API)
    
    
    MTConCommTier.Currency

### Parameters

**currency**  
[in] A three-letter representation of the currency, e.g. EUR, USD, JPY etc.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The currency has a three-letter representation, e.g. EUR, USD, JPY etc.
