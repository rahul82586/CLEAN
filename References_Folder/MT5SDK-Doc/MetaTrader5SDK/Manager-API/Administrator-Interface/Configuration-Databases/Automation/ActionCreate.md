[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / ActionCreate

[Previous](ConditionCreate.md) | [Next](ParamCreate.md)

# IMTAdminAPI::AutomationActionCreate

Create an automation task action object.

C++
    
    
    IMTConAutoAction*  IMTAdminAPI::AutomationActionCreate()

.NET
    
    
    CIMTConAutoAction  CIMTAdminAPI.AutomationActionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConAutoAction](../../../../Configuration-Interfaces/Automations/IMTConAutoAction.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConAutoAction::Release](../../../../Configuration-Interfaces/Automations/IMTConAutoAction/Release.md) method of this object.
