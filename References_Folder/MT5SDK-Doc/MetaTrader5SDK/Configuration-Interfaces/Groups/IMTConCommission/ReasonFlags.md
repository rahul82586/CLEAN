[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / ReasonFlags

[Previous](ProfitMode.md) | [Next](TurnoverCurrency.md)

# IMTConCommission::ReasonFlags

Get commission calculation mode depending on the reason for the deal execution.

C++
    
    
    UINT  IMTConCommission::ReasonFlags()  const

.NET (Gateway/Manager API)
    
    
    EnCommChargeMode  CIMTConCommission.ReasonFlags()

Python (Manager API)
    
    
    MTConCommission.ReasonFlags

### Return Value

A value from the [IMTConCommission::EnCommReasonFlags (#encommreasonflags)](Enumerations.md#encommreasonflags) enumeration.

### Note

The mode is only used for instantly charged commissions ([IMTConCommission::COMM_CHARGE_INSTANT (#encommchargemode)](Enumerations.md#encommchargemode)).

# IMTConCommission::ReasonFlags

Set commission calculation mode depending on the reason for the deal execution.

C++
    
    
    MTAPIRES  IMTConCommission::ReasonFlags(
       const UINT        flags  // Commission mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.ReasonFlags(
       EnCommChargeMode  flags  // Commission mode
       )

Python (Manager API)
    
    
    MTConCommission.ReasonFlags

### Parameters

**flags**  
[in] Commission calculation mode (flags) depending on the reason for the deal execution. TheIMTConCommission::EnCommReasonFlagsenumeration is used to pass the commission mode.

### Return Value

An indication of success is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred and the corresponding code is returned.

### Note

The mode is only used for instantly charged commissions ([IMTConCommission::COMM_CHARGE_INSTANT (#encommchargemode)](Enumerations.md#encommchargemode)).
