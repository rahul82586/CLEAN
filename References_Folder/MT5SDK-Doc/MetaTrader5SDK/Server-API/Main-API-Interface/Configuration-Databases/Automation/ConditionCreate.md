[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / ConditionCreate

[Previous](Create.md) | [Next](ActionCreate.md)

# IMTServerAPI::AutomationConditionCreate

Create an automation task condition object.
    
    
    IMTConAutoCondition*  IMTServerAPI::AutomationConditionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConAutoCondition](../../../../Configuration-Interfaces/Automations/IMTConAutoCondition.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConAutoCondition::Release](../../../../Configuration-Interfaces/Automations/IMTConAutoCondition/Release.md) method of this object.
