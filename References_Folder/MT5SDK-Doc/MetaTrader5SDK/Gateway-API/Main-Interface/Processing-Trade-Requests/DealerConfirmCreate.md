[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Processing Trade Requests](../Processing-Trade-Requests.md) / DealerConfirmCreate

[Previous](../Processing-Trade-Requests.md) | [Next](DealerExecutionCreate.md)

# IMTGatewayAPI::DealerConfirmCreate

Create request confirmation interface object.

C++
    
    
    IMTConfirm*  IMTGatewayAPI::DealerConfirmCreate()

.NET
    
    
    CIMTConfirm  CIMTGatewayAPI.DealerConfirmCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConfirm](../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTConfirm.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConfirm::Release](../../../Database-Interfaces/Trade/Trade-Requests/IMTConfirm/Requests-Release.md) method of this object.
