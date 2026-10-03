[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / ChargeMode

[Previous](RangeMode.md) | [Next](EntryMode.md)

# IMTConCommission::ChargeMode

Get the time of commission charging.

C++
    
    
    UINT  IMTConCommission::ChargeMode()  const

.NET (Gateway/Manager API)
    
    
    EnCommChargeMode  CIMTConCommission.ChargeMode()

Python (Manager API)
    
    
    MTConCommission.ChargeMode

### Return Value

A value of the [IMTConCommission::EnCommChargeMode (#encommchargemode)](Enumerations.md#encommchargemode) enumeration.

# IMTConCommission::ChargeMode

Set the time of commission charging.

C++
    
    
    MTAPIRES  IMTConCommission::ChargeMode(
       const UINT        mode  // Charging mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.ChargeMode(
       EnCommChargeMode  mode  // Charging mode
       )

Python (Manager API)
    
    
    MTConCommission.ChargeMode

### Parameters

**mode**  
[in] Tome of commission charging. TheIMTConCommission::EnCommChargeModeenumeration is used to pass the mode of commission charging.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
