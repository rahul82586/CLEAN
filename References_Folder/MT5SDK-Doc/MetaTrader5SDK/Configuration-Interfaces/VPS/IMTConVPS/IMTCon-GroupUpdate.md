[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon GroupUpdate

[Previous](IMTCon-GroupAdd.md) | [Next](IMTCon-GroupDelete.md)

# IMTConVPS::GroupUpdate

Change a group of accounts in which the Sponsored VPS is allowed.

C++
    
    
    MTAPIRES  IMTConVPS::GroupUpdate(
       const UINT               pos,      // Group position
       const IMTConVPSGroup*    group     // Group object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.GroupUpdate(
       uint                     pos,      // Group position
       CIMTConVPSGroup          group     // Group object
       )

Python
    
    
    MTConVPS.GroupUpdate(
       pos,                     # Group position
       group                    # Group object
       )
    
    
    MTConVPS.GroupSet(
       group_list               # List of groups
       )

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

**group**  
[in] Account group objectIMTConVPSGroup.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used.
