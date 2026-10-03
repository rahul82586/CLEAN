[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests TickAsk

[Previous](Requests-TickBid.md) | [Next](Requests-TickLast.md)

# IMTConfirm::TickAsk

Get the Ask price sent in response to a trade request.
    
    
    double  IMTConfirm::TickAsk()  const

### Return Value

The Ask price sent in response to a trade request.

### Note

If a trade request is a request for the price, then in response to it the price of the respective symbol is returned to the client.

# IMTConfirm::TickAsk

Set the Ask price sent in response to a trade request.
    
    
    MTAPIRES  IMTConfirm::TickAsk(
       const double  tickask      // Ask price
       )

### Parameters

**tickask**  
[in] The Ask price sent in response to a trade request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If a trade request is a request for the price, then in response to it the price of the respective symbol is returned to the client.
