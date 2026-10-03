[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching TimeSetupMsc

[Previous](IMTMatching-Flags.md) | [Next](IMTMatching-TimeExpiration.md)

# IMTECNMatching::TimeSetupMsc

Get order placing time in the ECN.

C++
    
    
    INT64  IMTECNMatching::TimeSetupMsc()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTECNMatching.TimeSetupMsc()

### Return Value

Time when the order was placed in the ECN, in milliseconds since 01.01.1970.

# IMTECNMatching::TimeSetupMsc

Set order placing time in the ECN.

C++
    
    
    MTAPIRES  IMTECNMatching::TimeSetupMsc(
       const INT64   time      // order placing time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.TimeSetupMsc(
       long          time      // order placing time
       )

### Parameters

**time**  
[in] Time of order placing in the ECN, in milliseconds since 01.01.1970.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
