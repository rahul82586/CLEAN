[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling Deviation

[Previous](IMTHistoryFilling-Digits.md) | [Next](IMTHistoryFilling-Provider.md)

# IMTECNHistoryFilling::Deviation

Get the allowable deviation for the filling order.

C++
    
    
    UINT  IMTECNHistoryFilling::Deviation()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTECNHistoryFilling.Deviation()

### Return Value

Allowable deviation for the filling order. The value is specified in points.

### Note

The allowable deviation is set in the [ECN settings (#filling)](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_execution#filling).

# IMTECNHistoryFilling::Deviation

Set the allowable deviation for the filling order.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::Deviation(
       const UINT    deviation   // deviation
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.Deviation(
       uint          deviation   // deviation
       )

### Parameters

**deviation**  
[in] Allowable deviation for the filling order. The value is specified in points.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The allowable deviation is set in the [ECN settings (#filling)](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_execution#filling).
