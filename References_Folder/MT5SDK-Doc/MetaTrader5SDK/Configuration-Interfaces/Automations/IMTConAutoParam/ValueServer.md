[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / ValueServer

[Previous](ValueLanguage.md) | [Next](ValueHTML.md)

# IMTConAutoParam::ValueServer

Get the value of the parameter that expresses the server ID.

C++
    
    
    UINT64  IMTConAutoParam::ValueServer()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConAutoParam.ValueServer()

Python
    
    
    MTConAutoParam.ValueServer

### Return Value

[Server ID](../../Network/IMTConServer/Id.md).

# IMTConAutoParam::ValueServer

Set the value of the parameter that expresses the server ID.

C++
    
    
    MTAPIRES  IMTConAutoParam::ValueServer(
       const UINT64  value      // Value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.ValueServer(
       ulong         value      // Value
       )

Python
    
    
    MTConAutoParam.ValueServer

### Parameters

**value**  
[in]Server ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
