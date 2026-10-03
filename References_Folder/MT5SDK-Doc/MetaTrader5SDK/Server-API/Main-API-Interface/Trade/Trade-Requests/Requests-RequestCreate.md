[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests RequestCreate

[Previous](../Requests.md) | [Next](Requests-RequestCreateArray.md)

# IMTServerAPI::TradeRequestCreate

Create an object of a trade request.
    
    
    IMTRequest*  IMTServerAPI::TradeRequestCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTRequest](../../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTRequest::Release](../../../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-Release.md) method of this object.
