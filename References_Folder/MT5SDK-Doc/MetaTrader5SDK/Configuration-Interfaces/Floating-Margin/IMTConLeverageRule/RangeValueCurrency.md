[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageRule](../IMTConLeverageRule.md) / RangeValueCurrency

[Previous](RangeMode.md) | [Next](TierAdd.md)

# IMTConLeverageRule::RangeValueCurrency

Get the currency to which the notional value of positions in [IMTConLeverageRule::RANGE_VALUE* (#enrangemode)](Enumerations.md#enrangemode) modes is converted.

C++
    
    
    LPCWSTR  IMTConLeverageRule::RangeValueCurrency()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConLeverageRule.RangeValueCurrency()

Python (Manager API)
    
    
    MTConLeverageRule.RangeValueCurrency

### Return Value

If successful, it returns a pointer to a string with the configuration name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid throughout the lifetime of the [IMTConLeverageRule](../IMTConLeverageRule.md) object.

# IMTConLeverageRule::RangeValueCurrency

Set the currency to which the notional value of positions in [IMTConLeverageRule::RANGE_VALUE* (#enrangemode)](Enumerations.md#enrangemode) modes is converted.

C++
    
    
    MTAPIRES  IMTConLeverageRule::RangeValueCurrency(
       LPCWSTR  currency  // Currency
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageRule.RangeValueCurrency(
       srting   currency  // Currency
       )

Python (Manager API)
    
    
    MTConLeverageRule.RangeValueCurrency

### Parameters

**path**  
[in] Three-character currency name. For example, EUR, USD, JPY, etc.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If the currency is not specified, conversion is made using the deposit currency of the group for which the margin is calculated.
