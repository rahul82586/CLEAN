[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching Server

[Previous](IMTHistoryMatching-Login.md) | [Next](IMTHistoryMatching-State.md)

# IMTECNHistoryMatching::Server

Get the identifier of the trade server on which the matching order was placed.

C++
    
    
    UINT64  IMTECNHistoryMatching::Server()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryMatching.Server()

### Return Value

The identifier of the trade server on which the matching order was placed.

# IMTECNHistoryMatching::Server

Set the identifier of the trade server on which the matching order was placed.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::Server(
       const UINT64  server     // identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.Server(
       ulong         server     // identifier
       )

### Parameters

**server**  
[in] The identifier of the trade server on which the matching order was placed.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
