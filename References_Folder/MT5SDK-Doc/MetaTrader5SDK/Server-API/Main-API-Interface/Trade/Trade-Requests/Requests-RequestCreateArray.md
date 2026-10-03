[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests RequestCreateArray

[Previous](Requests-RequestCreate.md) | [Next](Requests-ConfirmCreate.md)

# IMTServerAPI::TradeRequestCreateArray

Create an object of the array of trade requests.
    
    
    IMTRequestArray*  IMTServerAPI::TradeRequestCreateArray()

### Return value

It returns a pointer to the created object that implements the [IMTRequestArray](../../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequestArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTRequestArray::Release](../../../../Database-Interfaces/Trade/Trade-Requests/IMTRequestArray/Requests-Release.md) method of this object.
