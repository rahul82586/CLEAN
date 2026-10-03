[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / ParentID

[Previous](ID.md) | [Next](ParentIDSet.md)

# IMTConAutomation::ParentID

Get the ID of the subdirectory in which the automation task is located.

C++
    
    
    UINT64  IMTConAutomation::ParentID()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConAutomation.ParentID()

Python
    
    
    MTConAutomation.ParentID

### Return Value

The unique identifier for the directory.

### Note

For convenience, tasks can be grouped by directories. The [IMTConAutomation](../IMTConAutomation.md) configuration object can be either a description of the automation task or a description of a subdirectory of tasks. This can be determined by the [IMTConAutomation::FLAG_FOLDER (#enflags)](Enumerations.md#enflags) flag.
