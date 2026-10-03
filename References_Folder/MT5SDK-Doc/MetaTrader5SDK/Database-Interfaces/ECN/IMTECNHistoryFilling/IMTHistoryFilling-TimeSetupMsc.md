[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling TimeSetupMsc

[Previous](IMTHistoryFilling-Server.md) | [Next](IMTHistoryFilling-TimeDoneMsc.md)

# IMTECNHistoryFilling::TimeSetupMsc

Get order creation time in the ECN.

C++
    
    
    INT64  IMTECNHistoryFilling::TimeSetupMsc()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTECNHistoryFilling.TimeSetupMsc()

### Return Value

Time of filling order creation in the ECN, in milliseconds since 01.01.1970.

# IMTECNHistoryFilling::TimeSetupMsc

Set order creation time in the ECN.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::TimeSetupMsc(
       const INT64   time      // order placing time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.TimeSetupMsc(
       long          time      // order placing time
       )

### Parameters

**time**  
[in] Time of order creation in the ECN, in milliseconds since 01.01.1970.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
