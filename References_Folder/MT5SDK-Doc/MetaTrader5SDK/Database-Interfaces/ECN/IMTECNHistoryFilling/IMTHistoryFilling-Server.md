[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling Server

[Previous](IMTHistoryFilling-LoginMatching.md) | [Next](IMTHistoryFilling-TimeSetupMsc.md)

# IMTECNHistoryFilling::Server

Get the identifier of the trade server on which the filling order was placed.

C++
    
    
    UINT64  IMTECNHistoryFilling::Server()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryFilling.Server()

### Return Value

The identifier of the trade server on which the filling order was placed.

# IMTECNHistoryFilling::Server

Set the identifier of the trade server on which the filling order was placed.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::Server(
       const UINT64  server     // identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.Server(
       ulong         server     // identifier
       )

### Parameters

**server**  
[in] The identifier of the trade server on which the filling order was placed.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
