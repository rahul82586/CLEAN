[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests Flags

[Previous](Requests-Comment.md) | [Next](Requests-DealID.md)

# IMTConfirm::Flags

Get the current options of conformation of trade requests.

C++
    
    
    UINT  IMTConfirm::Flags()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConfirm.Flags()

### Return Value

A value of the [IMTConfirm::EnConfirmFlags (#enconfirmflags)](Requests-Enumerations.md#enconfirmflags) enumeration.

# IMTConfirm::Flags

Set the options of conformation of trade requests.

C++
    
    
    MTAPIRES  IMTConfirm::Flags(
       const UINT  flags      // Options
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.Flags(
       uint        flags      // Options
       )

### Parameters

**flags**  
[in] Options of conformation of trade requests. To pass the options, theIMTConfirmn::EnConfirmFlagsenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
