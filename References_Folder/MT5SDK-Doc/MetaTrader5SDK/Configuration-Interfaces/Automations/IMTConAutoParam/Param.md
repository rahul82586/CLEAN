[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / Param

[Previous](Clear.md) | [Next](ValueType.md)

# IMTConAutoParam::Param

Get the automation action parameter type.

C++
    
    
    UINT  IMTConAutoParam::Param()  const

.NET (Gateway/Manager API)
    
    
    EnConditions  CIMTConAutoParam.Param()

Python
    
    
    MTConAutoParam.Param

### Return Value

A value of the [IMTConAutoParam::EnParams (#enparams)](Enumerations.md#enparams) enumeration.

# IMTConAutoParam::Param

Set the automation action parameter type.

C++
    
    
    MTAPIRES  IMTConAutoParam::Param(
       const UINT        param      // Parameter type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.Param(
       EnConditions      param      // Parameter
       )

Python
    
    
    MTConAutoParam.Param

### Parameters

**param**  
[in] The automation action parameter type. The parameter type is passed using theIMTConAutoParam::EnParamsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
