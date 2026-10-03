[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests TickBid

[Previous](Requests-Price.md) | [Next](Requests-TickAsk.md)

# IMTConfirm::TickBid

Get the Bid price sent in response to a trade request.

C++
    
    
    double  IMTConfirm::TickBid()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConfirm.TickBid()

### Return Value

The Bid price sent in response to a trade request.

### Note

If a trade request is a request for the price, then in response to it the price of the respective symbol is returned to the client.

# IMTConfirm::TickBid

Set the Bid price sent in response to a trade request.

C++
    
    
    MTAPIRES  IMTConfirm::TickBid(
       const double  tickbid      // Bid price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.TickBid(
       double        tickbid      // Bid price
       )

### Parameters

**tickbid**  
[in] The Bid price sent in response to a trade request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If a trade request is a request for the price, then in response to it the price of the respective symbol is returned to the client.
