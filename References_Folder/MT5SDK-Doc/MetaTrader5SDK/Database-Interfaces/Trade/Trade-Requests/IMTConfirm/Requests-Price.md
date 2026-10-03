[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests Price

[Previous](Requests-VolumeExt.md) | [Next](Requests-TickBid.md)

# IMTConfirm::Price

Get the price, at which the trade request was confirmed.

C++
    
    
    double  IMTConfirm::Price()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConfirm.Price()

### Return Value

The price, at which the trade request was confirmed.

# IMTConfirm::Price

Set the price of request confirmation.

C++
    
    
    MTAPIRES  IMTConfirm::Price(
       const double  price      // Confirmation price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.Price(
       double        price      // Confirmation price
       )

### Parameters

**price**  
[in] Trade request confirmation price.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
