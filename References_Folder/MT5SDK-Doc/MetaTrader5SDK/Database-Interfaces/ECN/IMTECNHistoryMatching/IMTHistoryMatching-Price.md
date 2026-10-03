[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryMatching](../IMTHistoryMatching.md) / IMTHistoryMatching Price

[Previous](IMTHistoryMatching-TypeTimeClient.md) | [Next](IMTHistoryMatching-PriceClient.md)

# IMTECNHistoryMatching::Price

Get the price of the order created in the ECN for the filling of the client order.

C++
    
    
    double  IMTECNHistoryMatching::Price()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTECNHistoryMatching.Price()

### Return Value

Order price in the ECN.

# IMTECNHistoryMatching::Price

Set the price of the order created in the ECN for the filling of the client order.

C++
    
    
    MTAPIRES  IMTECNHistoryMatching::Price(
       const double  price      // order price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryMatching.Price(
       double        price      // order price
       )

### Parameters

**price**  
[in] Order price in the ECN.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
