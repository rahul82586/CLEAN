[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverage](../IMTConLeverage.md) / RuleNext

[Previous](RuleTotal.md) | [Next](RuleGet.md)

# IMTConLeverage::RuleNext

Get a rule from a floating margin configuration by index.

C++
    
    
    LPCWSTR  IMTConLeverage::RuleNext(
       const UINT            pos  // Rule position
       IMTConLeverageRule*   cfg  // Rule object
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConLeverage.RuleNext(
       uint                  pos, // Rule position
       CIMTConLeverageRule   cfg  // Rule object
       )

Python (Manager API)
    
    
    MTConLeverage.RuleNext(
       pos                   # Rule position
       )

### Parameters

**pos**  
[in] Position of the rule in the list.

**cfg**  
[out]IMTConLeverageRulerule object. The object must be created in advance using theIMTServerAPI::LeverageCreate,IMTAdminAPI::LeverageCreate, orIMTManagerAPI::LeverageCreatemethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
