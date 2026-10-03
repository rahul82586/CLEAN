[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon RuleNext

[Previous](IMTCon-RuleTotal.md) | [Next](IMTCon-GroupAdd.md)

# IMTConVPS::RuleNext

Getting the VPS allocation rule by index in the list.

C++
    
    
    MTAPIRES  IMTConVPS::RuleNext(
       const UINT             pos,       // Rule position
       IMTConVPSRule*         rule       // Rule object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.RuleNext(
       uint                   pos,       // Rule position
       CIMTConVPSRule         rule       // Rule object
       )

Python
    
    
    MTConVPS.RuleNext(
       pos                    # Rule position
       )
    
    
    MTConVPS.RuleGet()

### Parameters

**pos**  
[in] Rule position in the list starting from 0.

**rule**  
[out]IMTConVPSRulerule object. The object must first be created using theIMTServerAPI::VPSCreateRuleorIMTAdminAPI::VPSCreateRulemethod.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
