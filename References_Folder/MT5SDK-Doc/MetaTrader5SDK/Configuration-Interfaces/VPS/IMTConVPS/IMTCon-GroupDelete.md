[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon GroupDelete

[Previous](IMTCon-GroupUpdate.md) | [Next](IMTCon-GroupClear.md)

# IMTConVPS::GroupDelete

Remove a group of accounts from the list of groups in which the Sponsored VPS is allowed.

C++
    
    
    MTAPIRES  IMTConVPS::GroupDelete(
       const UINT  pos      // Group position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.GroupDelete(
       uint        pos      // Group position
       )

Python
    
    
    MTConVPS.GroupDelete(
       pos         # Group position
       )

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used.
