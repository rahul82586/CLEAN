[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests TickLast

[Previous](Requests-TickAsk.md) | [Next](Requests-Comment.md)

# IMTConfirm::TickLast

Get the Last price (price of the last conducted deal) sent in response to a trade request.

C++
    
    
    double  IMTConfirm::TickLast()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConfirm.TickLast()

### Return Value

The Last price sent in response to a trade request.

### Note

If a trade request is a request for the price, then in response to it the price of the respective symbol is returned to the client.

# IMTConfirm::TickLast

Set the Last price (price of the last conducted deal) price sent in response to a trade request.

C++
    
    
    MTAPIRES  IMTConfirm::TickLast(
       const double  ticklast      // Last price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.TickLast(
       double        ticklast      // Last price
       )

### Parameters

**ticklast**  
[in] The Last price sent in response to a trade request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

If a trade request is a request for the price, then in response to it the price of the respective symbol is returned to the client.
