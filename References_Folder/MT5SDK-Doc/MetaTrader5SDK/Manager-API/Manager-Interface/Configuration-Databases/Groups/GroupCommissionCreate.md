[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Groups](../Groups.md) / GroupCommissionCreate

[Previous](GroupSymbolCreate.md) | [Next](GroupTierCreate.md)

# IMTManagerAPI::GroupCommissionCreate

Create an object of commission configuration for a group.

C++
    
    
    IMTConCommission*  IMTManagerAPI::GroupCommissionCreate()

.NET
    
    
    CIMTConCommission  CIMTManagerAPI.GroupCommissionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConCommission](../../../../Configuration-Interfaces/Groups/IMTConCommission.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTConCommission::Release](../../../../Configuration-Interfaces/Groups/IMTConCommission/Release.md) method of this object.
