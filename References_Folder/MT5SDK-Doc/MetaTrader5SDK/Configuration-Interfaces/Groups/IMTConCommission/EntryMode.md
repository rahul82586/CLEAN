[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / EntryMode

[Previous](ChargeMode.md) | [Next](ActionMode.md)

# IMTConCommission::EntryMode

Get the commission calculation mode depending on the deal direction.

C++
    
    
    UINT  IMTConCommission::EntryMode()  const

.NET (Gateway/Manager API)
    
    
    EnCommChargeMode  CIMTConCommission.EntryMode()

Python (Manager API)
    
    
    MTConCommission.EntryMode

### Return Value

A value from the [IMTConCommission::EnCommEntryMode (#encommentrymode)](Enumerations.md#encommentrymode) enumeration.

### Note

The mode is only used for instantly charged commissions ([IMTConCommission::COMM_CHARGE_INSTANT (#encommchargemode)](Enumerations.md#encommchargemode)).

# IMTConCommission::EntryMode

Set commission calculation mode depending on the deal direction.

C++
    
    
    MTAPIRES  IMTConCommission::EntryMode(
       const UINT        mode  // Commission charging mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.EntryMode(
       EnCommChargeMode  mode  // Charging mode
       )

Python (Manager API)
    
    
    MTConCommission.EntryMode

### Parameters

**mode**  
[in] Commission charging mode depending on the direction of deals. TheIMTConCommission::EnCommEntryModeenumeration is used to pass the mode of commission charging.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The mode is only used for instantly charged commissions ([IMTConCommission::COMM_CHARGE_INSTANT (#encommchargemode)](Enumerations.md#encommchargemode)).
