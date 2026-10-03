[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon GroupClear

[Previous](IMTCon-GroupDelete.md) | [Next](IMTCon-GroupShift.md)

# IMTConVPS::GroupClear

Clear the list of groups in which the Sponsored VPS is allowed.

C++
    
    
    MTAPIRES  IMTConVPS::GroupClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.GroupClear()

Python
    
    
    IMTConVPS.GroupClear()

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used.
