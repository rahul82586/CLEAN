[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / Login

[Previous](ExternalID.md) | [Next](Dealer.md)

# IMTOrder::Login

Get the login of the client, to whom the order belongs.

C++
    
    
    UINT64  IMTOrder::Login()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTOrder.Login()

Python
    
    
    MTOrder.Login()

### Return Value

The login of the client, to whom the order belongs.

# IMTOrder::Login

Set the login of the client, to whom the order belongs.

C++
    
    
    MTAPIRES  IMTOrder::Login(
       const UINT64  order      // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.Login(
       ulong         order      // Login
       )

Python
    
    
    MTOrder.Login()

### Parameters

**order**  
[in] The login of the client, to whom the order belongs.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
