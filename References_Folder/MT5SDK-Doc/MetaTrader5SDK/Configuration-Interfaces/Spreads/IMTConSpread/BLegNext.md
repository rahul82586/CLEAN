[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / BLegNext

[Previous](BLegTotal.md) | [Next](../IMTConSpreadLeg.md)

# IMTConSpread::BLegNext

Get spread B leg configuration by the index.

C++
    
    
    MTAPIRES  IMTConSpread::BLegNext(
       const UINT            pos,         // Configuration position
       IMTConSpreadLeg*      leg          // Spread leg object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.BLegNext(
       uint                  pos,         // Configuration position
       CIMTConSpreadLeg      leg          // Spread leg object
       )

Python (Manager API)
    
    
    MTConSpread.BLegNext(
       pos,                  # Configuration position
       leg                   # Spread leg object
       )
    
    
    MTConSpread.BLegGet()

### Parameters

**pos**  
[in] Spread leg configuration position starting from 0.

**leg**  
[out] Spread leg configuration object. The leg object should be first created usingIMTManagerAPI::SpreadLegCreate,IMTAdminAPI::SpreadLegCreateorIMTGatewayAPI::SpreadLegCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
