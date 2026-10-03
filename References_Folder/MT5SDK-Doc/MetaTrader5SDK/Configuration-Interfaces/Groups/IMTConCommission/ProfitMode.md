[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / ProfitMode

[Previous](ActionMode.md) | [Next](ReasonFlags.md)

# IMTConCommission::ProfitMode

Get commission calculation mode depending on the deal profit.

C++
    
    
    UINT  IMTConCommission::ProfitMode()  const

.NET (Gateway/Manager API)
    
    
    EnCommChargeMode  CIMTConCommission.ProfitMode()

Python (Manager API)
    
    
    MTConCommission.ProfitMode

### Return Value

A value from the [IMTConCommission::EnCommProfitMode (#encommprofitmode)](Enumerations.md#encommprofitmode) enumeration.

### Note

The mode is only used for instantly charged commissions ([IMTConCommission::COMM_CHARGE_INSTANT (#encommchargemode)](Enumerations.md#encommchargemode)).

# IMTConCommission::ProfitMode

Set commission calculation mode depending on the deal profit.

C++
    
    
    MTAPIRES  IMTConCommission::ProfitMode(
       const UINT        mode  // Commission mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.ProfitMode(
       EnCommChargeMode  mode  // Commission mode
       )

Python (Manager API)
    
    
    MTConCommission.ProfitMode

### Parameters

**mode**  
[in] Commission mode depending on the deal profit. TheIMTConCommission::EnCommProfitModeenumeration is used to pass the commission mode.

### Return Value

An indication of success is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred and the corresponding code is returned.

### Note

The mode is only used for instantly charged commissions ([IMTConCommission::COMM_CHARGE_INSTANT (#encommchargemode)](Enumerations.md#encommchargemode)).
