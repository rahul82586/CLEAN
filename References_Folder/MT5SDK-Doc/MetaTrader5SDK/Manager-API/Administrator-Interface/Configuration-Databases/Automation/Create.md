[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / Create

[Previous](../Automation.md) | [Next](ConditionCreate.md)

# IMTAdminAPI::AutomationCreate

Create an automation configuration object.

C++
    
    
    IMTConAutomation*  IMTAdminAPI::AutomationCreate()

.NET
    
    
    CIMTConAutomation  CIMTAdminAPI.AutomationCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConAutomation](../../../../Configuration-Interfaces/Automations/IMTConAutomation.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConAutomation::Release](../../../../Configuration-Interfaces/Automations/IMTConAutomation/Release.md) method of this object.
