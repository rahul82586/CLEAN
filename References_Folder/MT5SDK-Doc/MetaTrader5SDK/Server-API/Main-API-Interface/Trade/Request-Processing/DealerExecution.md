[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Request Processing](../Request-Processing.md) / DealerExecution

[Previous](DealerAnswer.md) | [Next](DealerRequestTotal.md)

# IMTServerAPI::DealerExecution

Apply a [trade execution](../../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTExecution.md). This method enables the use of the [gateway trading mechanism](../../../../Gateway-API/Development-and-Debugging-of-Gateways.md) from the plugin: thus you can open, execute and cancel orders, calculate variation margin and perform other service operations. All these operations are available in the [IMTExecution::EnTradeExecutions (#entradeexecutions)](../../../../Database-Interfaces/Trade/Trade-Requests/IMTExecution/Requests-Enumerations.md#entradeexecutions) enumeration. Unlike [IMTGatewayAPI::DealerExecuteAsync](../../../../Gateway-API/Main-Interface/Processing-Trade-Requests/DealerExecuteAsync.md) which is used in gateways, IMTServerAPI::DealerExecution is synchronous. It does not send an execution command to a queue but immediately applies the trade execution to the database and returns the result.
    
    
    MTAPIRES  IMTServerAPI::DealerExecution(
       LPCWSTR       gateway_name,  // gateway name
       LPCWSTR       gateway_type,  // gateway type
       IMTExecution* execution      // trade execution object
       )

### Parameters

**gateway_name**  
[in] The name of the gateway from which the trade execution arrived. The value is used for logging information about the applied trade execution into a trade server journal.

**gateway_type**  
[in] Gateway module name (IMTConGateway::Module) from which the trade execution arrived. The value is written to theIMTDeal::Gatewayfield of the deals executed as a result of the application of a trade execution.

**execution**  
[in] Filledtrade execution object. TheIMTExecution::GatewayIDfield must be filled in the object, since the execution runs in the context of settings of a particular gateway, including the settings of available groups, allowed symbols, and price translation rules.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Upon the execution of this method, an operation corresponding to the [passed trade execution type (#entradeexecutions)](../../../../Database-Interfaces/Trade/Trade-Requests/IMTExecution/Requests-Enumerations.md#entradeexecutions) is performed in the platform.
