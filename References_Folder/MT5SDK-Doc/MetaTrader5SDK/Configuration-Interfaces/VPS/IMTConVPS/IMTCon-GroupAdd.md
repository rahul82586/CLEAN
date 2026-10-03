[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon GroupAdd

[Previous](IMTCon-RuleNext.md) | [Next](IMTCon-GroupUpdate.md)

# IMTConVPS::GroupAdd

Add a group of accounts in which the Sponsored VPS is allowed.

C++
    
    
    MTAPIRES  IMTConVPS::GroupAdd(
       IMTConVPSGroup*  group      // Group object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.GroupAdd(
       CIMTConVPSGroup  group      // Group object
       )

Python
    
    
    MTConVPS.GroupAdd(
       group            # Group object
       )

### Parameters

**group**  
[in] Group objectIMTConVPSGroup.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used.
