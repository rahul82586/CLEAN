[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / MarginType

[Previous](ID.md) | [Next](MarginInitial.md)

# IMTConSpread::MarginType

Getting margin charging type.

C++
    
    
    UINT  IMTConSpread::MarginType()  const

.NET (Gateway/Manager API)
    
    
    EnSpreadMarginType  CIMTConSpread.MarginType()

Python (Manager API)
    
    
    MTConSpread.MarginType

### Return Value

Margin charging type as [IMTConSpread::EnSpreadMarginType (#enspreadmargintype)](Enumerations.md#enspreadmargintype) enumeration value.

# IMTConSpread::MarginType

Setting margin charging type.

C++
    
    
    MTAPIRES  IMTConSpread::MarginType(
       const UINT          type  // Margin charging type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.MarginType(
       EnSpreadMarginType  type  // Margin charging type
       )

Python (Manager API)
    
    
    MTConSpread.MarginType

### Parameters

**type**  
[in] Margin charging type. It is passed asIMTConSpread::EnSpreadMarginTypeenumeration value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
