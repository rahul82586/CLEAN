[🏠 Document Start](../../../README.md) / [Tools](../../README.md) / [SMTMath](../../SMTMath.md) / [Functions of Monetary Units](../Functions-of-Monetary-Units.md) / MoneyDigits

[Previous](MoneyEqual.md) | [Next](../../SMTSearch.md)

# SMTMath::MoneyDigits

Get the number of decimal places for the specified currency.

C++
    
    
    static UINT  SMTMath::MoneyDigits(
       LPCWSTR  currency        // Currency
       )

.NET (Gateway/Manager API)
    
    
    static uint  SMTMath.MoneyDigits(
       string   currency        // Currency
       )

### Parameters

**currency**  
[in] The name of the currency in the three-letter format. For example, JPY,EUR,USD etc.

### Return Value

The number of decimal places in the specified currency.

### Note

For all currencies the accuracy is 2 decimal places. The exceptions are JPY (Yen) and VND (Vietnamese Dong), for them the accuracy is 0.
