[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommTier](../IMTConCommTier.md) / Type

[Previous](Mode.md) | [Next](Value.md)

# IMTConCommTier::Type

Get the type of commission charging.

C++
    
    
    UINT  IMTConCommTier::Type()  const

.NET (Gateway/Manager API)
    
    
    EnCommissionVolumeType  CIMTConCommTier.Type()

Python (Manager API)
    
    
    MTConCommTier.Type

### Return Value

A value from the [IMTConCommTier::EnCommissionVolumeType (#encommissionvolumetype)](Enumerations.md#encommissionvolumetype) enumeration.

# IMTConCommTier::Type

Set the type of commission charging.

C++
    
    
    MTAPIRES  IMTConCommTier::Type(
       const UINT              type  // Type of commission charging
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommTier.Type(
       EnCommissionVolumeType  type  // Type of commission charging
       )

Python (Manager API)
    
    
    MTConCommTier.Type

### Parameters

**type**  
[in] TheIMTConCommTier::EnCommissionVolumeTypeenumeration is used to pass the type of commission charging.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
