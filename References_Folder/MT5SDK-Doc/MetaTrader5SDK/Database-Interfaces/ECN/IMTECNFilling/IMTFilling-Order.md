[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling Order

[Previous](IMTFilling-Login.md) | [Next](IMTFilling-Server.md)

# IMTECNFilling::Order

Get the filling order ticket in the MetaTrader 5 platform.

C++
    
    
    UINT64  IMTECNFilling::Order()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNFilling.Order()

### Return Value

The ticket of the filling order in the MetaTrader 5 platform.

# IMTECNFilling::Order

Set the filling order ticket in the MetaTrader 5 platform.

C++
    
    
    MTAPIRES  IMTECNFilling::Order(
       const UINT64  order      // order ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.Order(
       ulong         order      // order ticket
       )

### Parameters

**order**  
[in] The ticket of the filling order in the MetaTrader 5 platform.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
