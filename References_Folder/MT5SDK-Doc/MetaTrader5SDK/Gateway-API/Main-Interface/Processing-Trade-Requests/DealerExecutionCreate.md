[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Processing Trade Requests](../Processing-Trade-Requests.md) / DealerExecutionCreate

[Previous](DealerConfirmCreate.md) | [Next](DealerStart.md)

# IMTGatewayAPI::DealerExecutionCreate

Create trade execution method of this object.

C++
    
    
    IMTExecution*  IMTGatewayAPI::DealerExecutionCreate()

.NET
    
    
    CIMTExecution  CIMTGatewayAPI.DealerExecutionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTExecution](../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTExecution.md) interface. In case of failure, it returns NULL.

### Note

It returns a pointer to the created object that implements the [IMTExecution::Release](../../../Database-Interfaces/Trade/Trade-Requests/IMTExecution/Requests-Release.md) method of this project.
