[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueVolume

[Previous](ValueMoney.md) | [Next](ValueDatetime.md)

# IMTConAutoParam::ValueVolume

Get the value of the parameter that expresses the volume.

C++
    
    
    UINT64  IMTConAutoParam::ValueVolume()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConAutoParam.ValueVolume()

Python
    
    
    MTConAutoParam.ValueVolume

### Return Value

A value in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

# IMTConAutoParam::ValueVolume

Set the value of the parameter that expresses the volume.

C++
    
    
    MTAPIRES  IMTConAutoParam::ValueVolume(
       const UINT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueVolume(
       ulong         value      // Value
       )

Python
    
    
    MTConAutoParam.ValueVolume

### Parameters

**value**  
[in] A value in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
