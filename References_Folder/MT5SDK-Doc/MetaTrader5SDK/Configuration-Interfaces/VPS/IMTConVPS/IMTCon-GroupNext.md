[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon GroupNext

[Previous](IMTCon-GroupTotal.md) | [Next](../IMTConRule.md)

# IMTConVPS::GroupNext

Get the group in which the Sponsored VPS is allowed by its index in the list.

C++
    
    
    MTAPIRES  IMTConVPS::GroupNext(
       const UINT             pos,       // Group position
       IMTConVPSGroup*        group      // Group object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.GroupNext(
       uint                   pos,       // Group position
       CIMTConVPSGroup        group      // Group object
       )

Python
    
    
    MTConVPS.GroupNext(
       pos                    # Group position
       )
    
    
    MTConVPS.GroupGet()

### Parameters

**pos**  
[in] Position of the group in the list, starting with 0.

**group**  
[out] Group object. The 'group' object must be previously created via theIMTServerAPI::VPSCreateGrouporIMTAdminAPI::VPSCreateGroupmethod.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used.
