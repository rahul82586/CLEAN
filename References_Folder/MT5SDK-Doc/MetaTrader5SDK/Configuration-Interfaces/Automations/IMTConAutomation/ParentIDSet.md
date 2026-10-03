[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / ParentIDSet

[Previous](ParentID.md) | [Next](Name.md)

# IMTConAutomation::ParentIDSet

Set an ID of the subdirectory in which the automation task is located.

C++
    
    
    MTAPIRES  IMTConAutomation::ParentIDSet(
       const UINT64  parent_id  // Identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.ParentIDSet(
       ulong         parent_id  // Identifier
       )

Python
    
    
    MTConAutomation.ParentID

### Parameters

**parent_id**  
[in] A unique identifier for the directory.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

For convenience, tasks can be grouped by directories. The [IMTConAutomation](../IMTConAutomation.md) configuration object can be either a description of the automation task or a description of a subdirectory of tasks. This can be determined by the [IMTConAutomation::FLAG_FOLDER (#enflags)](Enumerations.md#enflags) flag.
