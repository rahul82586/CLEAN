[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling Server

[Previous](IMTFilling-Order.md) | [Next](IMTFilling-TimeSetupMsc.md)

# IMTECNFilling::Server

Get the identifier of the trade server on which the filling order was placed.

C++
    
    
    UINT64  IMTECNFilling::Server()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNFilling.Server()

### Return Value

The identifier of the trade server on which the filling order was placed.

# IMTECNFilling::Server

Set the identifier of the trade server on which the filling order was placed.

C++
    
    
    MTAPIRES  IMTECNFilling::Server(
       const UINT64  server     // identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.Server(
       ulong         server     // identifier
       )

### Parameters

**server**  
[in] The identifier of the trade server on which the filling order was placed.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
