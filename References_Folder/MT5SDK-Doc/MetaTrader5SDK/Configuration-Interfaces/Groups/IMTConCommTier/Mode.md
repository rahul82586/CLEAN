[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommTier](../IMTConCommTier.md) / Mode

[Previous](Clear.md) | [Next](Type.md)

# IMTConCommTier::Mode

Gets the method of commission charging.

C++
    
    
    UINT  IMTConCommTier::Mode()  const

.NET (Gateway/Manager API)
    
    
    EnCommissionMode  CIMTConCommTier.Mode()

Python (Manager API)
    
    
    MTConCommTier.Mode

### Return Value

One of the values of the [IMTConCommTier::EnCommissionMode (#encommissionmode)](Enumerations.md#encommissionmode) enumeration.

# IMTConCommTier::Mode

Sets the method of commission charging.

C++
    
    
    MTAPIRES  IMTConCommTier::Mode(
       const UINT        mode  // Commission charging method
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommTier.Mode(
       EnCommissionMode  mode  // Commission charging method
       )

Python (Manager API)
    
    
    MTConCommTier.Mode

### Parameters

**mode**  
[in] To pass the method of commission charging, theIMTConCommTier::EnCommissionModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
