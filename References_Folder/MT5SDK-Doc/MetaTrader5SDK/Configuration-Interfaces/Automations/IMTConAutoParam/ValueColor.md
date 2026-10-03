[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueColor

[Previous](ValueString.md) | [Next](ValueMoney.md)

# IMTConAutoParam::ValueColor

Get a parameter value of the colorref type.

C++
    
    
    COLORREF  IMTConAutoParam::ValueColor()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutoParam.ValueColor()

Python
    
    
    MTConAutoParam.ValueColor

### Return Value

The parameter value of a colorref type.

# IMTConAutoParam::ValueColor

Set a parameter value of the colorref type.

C++
    
    
    MTAPIRES  IMTConAutoParam::ValueColor(
       const COLORREF  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueColor(
       uint            value      // Value
       )

Python
    
    
    MTConAutoParam.ValueColor

### Parameters

**value**  
[in] A value of colorref type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
