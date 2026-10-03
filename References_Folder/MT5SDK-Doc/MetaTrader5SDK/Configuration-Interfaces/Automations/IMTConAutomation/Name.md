[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / Name

[Previous](ParentIDSet.md) | [Next](Trigger.md)

# IMTConAutomation::Name

Get the name of the automation task.

C++
    
    
    LPCWSTR  IMTConAutomation::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConAutomation.Name()

Python
    
    
    MTConAutomation.Name

### Return Value

If successful, it returns a pointer to a string with the configuration name. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConAutomation](../../Messengers/IMTConMessenger.md) object.

# IMTConAutomation::Name

Set the name of the automation task.

C++
    
    
    MTAPIRES  IMTConAutomation::Name(
       LPCWSTR  name      // Name of the automation task
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.Name(
       srting   name      // Name of the automation task
       )

Python
    
    
    MTConAutomation.Name

### Parameters

**name**  
[in] Name of the automation task.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The name length is limited 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be truncated to this length.
