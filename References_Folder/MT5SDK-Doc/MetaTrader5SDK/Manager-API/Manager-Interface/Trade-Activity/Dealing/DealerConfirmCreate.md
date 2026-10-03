[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Dealing](../Dealing.md) / DealerConfirmCreate

[Previous](../Dealing.md) | [Next](DealerUnsubscribe.md)

# IMTManagerAPI::DealerConfirmCreate

Create request confirmation interface object.

C++
    
    
    IMTConfirm*  IMTManagerAPI::DealerConfirmCreate()

.NET
    
    
    CIMTConfirm  CIMTManagerAPI.DealerConfirmCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConfirm](../../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTConfirm.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConfirm::Release](../../../../Database-Interfaces/Trade/Trade-Requests/IMTConfirm/Requests-Release.md) method of this object.
