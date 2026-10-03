[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatching](../IMTMatching.md) / IMTMatching Price

[Previous](IMTMatching-TypeTime.md) | [Next](IMTMatching-PriceClient.md)

# IMTECNMatching::Price

Get the price of the order created in the ECN for the filling of the client order.

C++
    
    
    double  IMTECNMatching::Price()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTECNMatching.Price()

### Return Value

Order price in the ECN.

# IMTECNMatching::Price

Set the price of the order created in the ECN for the filling of the client order.

C++
    
    
    MTAPIRES  IMTECNMatching::Price(
       const double  price      // order price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNMatching.Price(
       double        price      // order price
       )

### Parameters

**price**  
[in] Order price in the ECN.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
