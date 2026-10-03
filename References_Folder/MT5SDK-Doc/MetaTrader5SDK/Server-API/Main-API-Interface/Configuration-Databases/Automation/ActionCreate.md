[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / ActionCreate

[Previous](ConditionCreate.md) | [Next](ParamCreate.md)

# IMTServerAPI::AutomationActionCreate

Create an automation task action object.
    
    
    IMTConAutoAction*  IMTServerAPI::AutomationActionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConAutoAction](../../../../Configuration-Interfaces/Automations/IMTConAutoAction.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConAutoAction::Release](../../../../Configuration-Interfaces/Automations/IMTConAutoAction/Release.md) method of this object.
