[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverage](../IMTConLeverage.md) / RuleGet

[Previous](RuleNext.md) | [Next](../IMTConLeverageArray.md)

# IMTConLeverage::RuleGet

Get a rule from a floating margin configuration by name.

C++
    
    
    LPCWSTR  IMTConLeverage::RuleGet(
       LPCWSTR               name, // Rule name
       IMTConLeverageRule*   cfg   // Rule object
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConLeverage.RuleGet(
       string                name, // Rule object
       CIMTConLeverageRule   cfg   // Rule object
       )

Python (Manager API)
    
    
    MTConLeverage.RuleGet(
       name                  # Rule object
       )

### Parameters

**name**  
[in] Rule name. Matches theIMTConLeverage::Namefield.

**cfg**  
[out]IMTConLeverageRulerule object. The object must be created in advance using theIMTServerAPI::LeverageCreate,IMTAdminAPI::LeverageCreate, orIMTManagerAPI::LeverageCreatemethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
