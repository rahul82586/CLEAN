[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests ExecutionCreate

[Previous](Requests-ConfirmCreate.md) | [Next](Requests-Subscribe.md)

# IMTServerAPI::TradeExecutionCreate

Create an object of a trade request.
    
    
    IMTExecution*  IMTServerAPI::TradeExecutionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTExecution](../../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTExecution.md) interface. In case of failure, it returns NULL.

### Note

It returns a pointer to the created object that implements the [IMTExecution::Release](../../../../Database-Interfaces/Trade/Trade-Requests/IMTExecution/Requests-Release.md) method of this project.
