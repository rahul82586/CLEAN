[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching TimeDoneMsc

[Previous](IMTHistoryMatching-TimeSetupMsc.md) | [Next](IMTHistoryMatching-TimeExpiration.md)

# IMTECNHistoryMatching::TimeDoneMsc

Get order execution time in the ECN.

C++
    
    
    INT64  IMTECNHistoryMatching::TimeDoneMsc()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTECNHistoryMatching.TimeDoneMsc()

### Return Value

Time of order execution in the ECN, in milliseconds since 01.01.1970.

# IMTECNHistoryMatching::TimeDoneMsc

Set order execution time in the ECN.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::TimeDoneMsc(
       const INT64   time      // execution time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.TimeDoneMsc(
       long          time      // execution time
       )

### Parameters

**time**  
[in] Time of order execution in the ECN, in milliseconds since 01.01.1970.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
