[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching TimeSetupMsc

[Previous](IMTHistoryMatching-State.md) | [Next](IMTHistoryMatching-TimeDoneMsc.md)

# IMTECNHistoryMatching::TimeSetupMsc

Get order placing time in the ECN.

C++
    
    
    INT64  IMTECNHistoryMatching::TimeSetupMsc()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTECNHistoryMatching.TimeSetupMsc()

### Return Value

Time when the order was placed in the ECN, in milliseconds since 01.01.1970.

# IMTECNHistoryMatching::TimeSetupMsc

Set order placing time in the ECN.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::TimeSetupMsc(
       const INT64   time      // order placing time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.TimeSetupMsc(
       long          time      // order placing time
       )

### Parameters

**time**  
[in] Time of order placing in the ECN, in milliseconds since 01.01.1970.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
