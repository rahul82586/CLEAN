[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / CurrencyProfitDigitsSet

[Previous](CurrencyProfitDigits.md) | [Next](CurrencyMargin.md)

# IMTConSymbol::CurrencyProfitDigitsSet

Set the accuracy of conversion into the profit currency.

C++
    
    
    MTAPIRES  IMTConSymbol::CurrencyProfitDigitsSet(
       const UINT  digits     // Accuracy
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.CurrencyProfitDigitsSet(
       uint        digits     // Accuracy
       )

Python (Manager API)
    
    
    MTConSymbol.CurrencyProfitDigits

### Parameters

**digits**  
[in] The number of decimal places in the rate of conversion to the profit currency.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

For standard world currencies, such as USD, EUR, GBP, JPY, CHF, RUR, etc., the number of digits is set by the platform and cannot be modified. The accuracy of cryptocurrencies (and other non-standard currencies) can be changed manually. A higher accuracy enables a proper calculation of profit and margin through cross-rates, in which such currencies are used. If the accuracy is small, the resulting profit or margin value can be equal to zero due to rounding.
