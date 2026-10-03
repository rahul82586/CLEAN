[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching Server

[Previous](IMTMatching-Login.md) | [Next](IMTMatching-Group.md)

# IMTECNMatching::Server

Get the identifier of the trade server on which the matching order was placed.

C++
    
    
    UINT64  IMTECNMatching::Server()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNMatching.Server()

### Return Value

The identifier of the trade server on which the matching order was placed.

# IMTECNMatching::Server

Set the identifier of the trade server on which the matching order was placed.

C++
    
    
    MTAPIRES  IMTECNMatching::Server(
       const UINT64  server     // identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.Server(
       ulong         server     // identifier
       )

### Parameters

**server**  
[in] The identifier of the trade server on which the matching order was placed.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
