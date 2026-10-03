[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / CurrencyMarginDigitsSet

[Previous](CurrencyMarginDigits.md) | [Next](Color.md)

# IMTConSymbol::CurrencyMarginDigitsSet

Set the accuracy of conversion into the margin currency.

C++
    
    
    MTAPIRES  IMTConSymbol::CurrencyMarginDigitsSet(
       const UINT  digits     // Accuracy
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.CurrencyMarginDigitsSet(
       uint        digits     // Accuracy
       )

Python (Manager API)
    
    
    MTConSymbol.CurrencyMarginDigits

### Parameters

**digits**  
[in] The number of decimal places in the rate of conversion to the margin currency.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

For standard world currencies, such as USD, EUR, GBP, JPY, CHF, RUR, etc., the number of digits is set by the platform and cannot be modified. The accuracy of cryptocurrencies (and other non-standard currencies) can be changed manually. A higher accuracy enables a proper calculation of profit and margin through cross-rates, in which such currencies are used. If the accuracy is small, the resulting profit or margin value can be equal to zero due to rounding.
