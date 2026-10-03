[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / Mode

[Previous](Path.md) | [Next](RangeMode.md)

# IMTConCommission::Mode

Get the type of commission.

C++
    
    
    UINT  IMTConCommission::Mode()  const

.NET (Gateway/Manager API)
    
    
    EnCommMode  CIMTConCommission.Mode()

Python (Manager API)
    
    
    MTConCommission.Mode

### Return Value

One of the values of the [IMTConCommission::EnCommMode (#encommmode)](Enumerations.md#encommmode) enumeration.

# IMTConCommission::Mode

Set the commission type.

C++
    
    
    MTAPIRES  IMTConCommission::Mode(
       const UINT  mode      // Type of commission
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.Mode(
       EnCommMode  mode      // Type of commission
       )

Python (Manager API)
    
    
    MTConCommission.Mode

### Parameters

**mode**  
[in] Type of commission. TheIMTConCommission::EnCommModeenumeration is used to pass the commission type..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
