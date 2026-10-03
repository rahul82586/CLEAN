[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Automation](../Automation.md) / Trigger

[Previous](Get.md) | [Next](../VPS.md)

# IMTServerAPI::AutomationTrigger

Send an event to trigger an automation rule with the specified name.
    
    
    MTAPIRES  IMTServerAPI::AutomationTrigger(
       LPCWSTR            name,     // Configuration name
       const IMTUser*     user,     // User object
       const IMTAccount*  account,  // An object of the account trading state
       const IMTDeal*     deal,     // Deal object
       const IMTOrder*    order,    // Order object
       const IMTPosition* position  // Position object
       )

### Parameters

**name**  
[in] The name of the automation configuration for which the event is sent. TheIMTConAutomation::Namefields is used for the name.

**user**  
[in] TheIMTUseruser object. Optional parameter.

**account**  
[in] TheIMTAccountobject of the account trading state. Optional parameter.

**deal**  
[in] TheIMTDealdeal object. Optional parameter.

**order**  
[in] TheIMTOrderorder object. Optional parameter.

**position**  
[in] TheIMTPositionposition object. Optional parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Use this function to run automation tasks based on your own events. During the function call, a special event is generated for the task specified in the 'name' parameter. The event causes the task to trigger.
