[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching TimeExpiration

[Previous](IMTHistoryMatching-TimeDoneMsc.md) | [Next](IMTHistoryMatching-Symbol.md)

# IMTECNHistoryMatching::TimeExpiration

Get order expiration time in the ECN.

C++
    
    
    INT64  IMTECNHistoryMatching::TimeExpiration()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTECNHistoryMatching.TimeExpiration()

### Return Value

Order expiration time in the ECN, in milliseconds since 01.01.1970.

# IMTECNHistoryMatching::TimeExpiration

Set order expiration time in the ECN.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::TimeExpiration(
       const INT64   time      // expiration time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.TimeExpiration(
       long          time      // expiration time
       )

### Parameters

**time**  
[in] Order execution time in the ECN, in milliseconds since 01.01.1970.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
