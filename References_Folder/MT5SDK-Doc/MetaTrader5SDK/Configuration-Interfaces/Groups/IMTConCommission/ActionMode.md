[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / ActionMode

[Previous](EntryMode.md) | [Next](ProfitMode.md)

# IMTConCommission::ActionMode

Get the commission calculation mode depending on the deal type.

C++
    
    
    UINT  IMTConCommission::ActionMode()  const

.NET (Gateway/Manager API)
    
    
    EnCommChargeMode  CIMTConCommission.ActionMode()

Python (Manager API)
    
    
    MTConCommission.ActionMode

### Return Value

A value from the [IMTConCommission::EnCommActionMode (#encommactionmode)](Enumerations.md#encommactionmode) enumeration.

### Note

The mode is only used for instantly charged commissions ([IMTConCommission::COMM_CHARGE_INSTANT (#encommchargemode)](Enumerations.md#encommchargemode)).

# IMTConCommission::ActionMode

Set the commission mode depending on the deal type.

C++
    
    
    MTAPIRES  IMTConCommission::ActionMode(
       const UINT        mode  // Commission mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.ActionMode(
       EnCommChargeMode  mode  // Commission mode
       )

Python (Manager API)
    
    
    MTConCommission.ActionMode

### Parameters

**mode**  
[in] Commission mode depending on deal type. The commission mode is passed using theIMTConCommission::EnCommActionModeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a relevant error code is returned.

### Note

The mode is only used for instantly charged commissions ([IMTConCommission::COMM_CHARGE_INSTANT (#encommchargemode)](Enumerations.md#encommchargemode)).
