[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching TimeExpiration

[Previous](IMTMatching-TimeSetupMsc.md) | [Next](IMTMatching-Symbol.md)

# IMTECNMatching::TimeExpiration

Get order expiration time in the ECN.

C++
    
    
    INT64  IMTECNMatching::TimeExpiration()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTECNMatching.TimeExpiration()

### Return Value

Order expiration time in the ECN, in milliseconds since 01.01.1970.

# IMTECNMatching::TimeExpiration

Set order expiration time in the ECN.

C++
    
    
    MTAPIRES  IMTECNMatching::TimeExpiration(
       const INT64   time      // expiration time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.TimeExpiration(
       long          time      // expiration time
       )

### Parameters

**time**  
[in] Order execution time in the ECN, in milliseconds since 01.01.1970.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
