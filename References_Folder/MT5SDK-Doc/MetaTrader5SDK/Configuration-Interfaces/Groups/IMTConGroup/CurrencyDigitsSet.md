[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CurrencyDigitsSet

[Previous](CurrencyDigits.md) | [Next](ReportsMode.md)

# IMTConGroup::CurrencyDigitsSet

Set the number of digits after the decimal point in the group deposit currency.

C++
    
    
    MTAPIRES  IMTConGroup::CurrencyDigitsSet(
       UINT         digits        // accuracy of a deposit currency
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.CurrencyDigitsSet(
       uint         digits       // accuracy of a deposit currency
       )

Python (Manager API)
    
    
    MTConGroup.CurrencyDigits

### Parameters

**digits**  
[in] The number of digits after the decimal point in the group deposit currency. The valid values are 0-8.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The accuracy is predetermined for standard currencies, such as USD, EUR, GBP, JPY, CHF, RUR, etc. It cannot be changed. If attempting to do this, the server returns the [MT_RET_ERR_PARAMS](../../../Return-Codes/Common-errors.md) error. The method is intended for use with more exotic deposit currencies, like bitcoin (BTC).
