[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests ConfirmCreate

[Previous](Requests-RequestCreateArray.md) | [Next](Requests-ExecutionCreate.md)

# IMTServerAPI::TradeConfirmCreate

Create an object of a trade request confirmation.
    
    
    IMTConfirm*  IMTServerAPI::TradeConfirmCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConfirm](../../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTConfirm.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConfirm::Release](../../../../Database-Interfaces/Trade/Trade-Requests/IMTConfirm/Requests-Release.md) method of this object.
