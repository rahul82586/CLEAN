[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / ParamCreate

[Previous](ActionCreate.md) | [Next](Subscribe.md)

# IMTAdminAPI::AutomationParamCreate

Create an automation condition parameter object.

C++
    
    
    IMTConAutoParam*  IMTAdminAPI::AutomationParamCreate()

.NET
    
    
    CIMTConAutoParam  CIMTAdminAPI.AutomationParamCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTConAutoParam](../../../../Configuration-Interfaces/Automations/IMTConAutoParam.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTConAutoParam::Release](../../../../Configuration-Interfaces/Automations/IMTConAutoParam/Release.md) method of this object.
