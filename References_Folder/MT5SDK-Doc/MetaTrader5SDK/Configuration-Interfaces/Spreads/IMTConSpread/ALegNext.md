[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / ALegNext

[Previous](ALegTotal.md) | [Next](BLegAdd.md)

# IMTConSpread::ALegNext

Get spread A leg configuration by the index.

C++
    
    
    MTAPIRES  IMTConSpread::ALegNext(
       const UINT            pos,         // Configuration position
       IMTConSpreadLeg*      leg          // Spread leg object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.ALegNext(
       uint                  pos,         // Configuration position
       CIMTConSpreadLeg      leg          // Spread leg object
       )

Python (Manager API)
    
    
    MTConSpread.ALegNext(
       pos                   # Configuration position
       )
    
    
    MTConSpread.ALegGet()

### Parameters

**pos**  
[in] Spread leg configuration position starting from 0.

**leg**  
[out] Spread leg configuration object. The leg object should be first created usingIMTManagerAPI::SpreadLegCreate,IMTAdminAPI::SpreadLegCreateorIMTGatewayAPI::SpreadLegCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
