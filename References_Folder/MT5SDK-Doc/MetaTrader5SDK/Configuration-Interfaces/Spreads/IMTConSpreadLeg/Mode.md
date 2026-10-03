[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpreadLeg](../IMTConSpreadLeg.md) / Mode

[Previous](Clear.md) | [Next](Symbol.md)

# IMTConSpreadLeg::Mode

Getting symbol specification mode for a spread leg.

C++
    
    
    UINT  IMTConSpreadLeg::Mode()  const

.NET (Gateway/Manager API)
    
    
    EnLegMode  CIMTConSpreadLeg.Mode()

Python (Manager API)
    
    
    MTConSpreadLeg.Mode

### Return Value

[IMTConSpreadLeg::EnLegMode (#enlegmode)](Enumerations.md#enlegmode) enumeration is used to pass a symbol specification mode.

# IMTConSpreadLeg::Mode

Setting symbol specification mode for a spread leg.

C++
    
    
    MTAPIRES  IMTConSpreadLeg::Mode(
       const UINT  mode      // symbol specification mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpreadLeg.Mode(
       EnLegMode   mode      // symbol specification mode
       )

Python (Manager API)
    
    
    MTConSpreadLeg.Mode

### Parameters

**open**  
[in] Symbol specification mode for a spread leg. It is passed asIMTConSpreadLeg::EnLegModeenumeration value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
