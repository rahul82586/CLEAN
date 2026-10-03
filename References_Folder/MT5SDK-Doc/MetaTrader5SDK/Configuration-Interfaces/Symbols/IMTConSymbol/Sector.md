[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Sector

[Previous](CFI.md) | [Next](Industry.md)

# IMTConSymbol::Sector

Get the economic sector the instrument belongs to.

C++
    
    
    UINT  IMTConSymbol::Sector()  const

.NET (Gateway/Manager API)
    
    
    EnSectors  CIMTConSymbol.Sector()

Python (Manager API)
    
    
    MTConSymbol.Sector

### Return Value

[IMTConSymbol::EnSectors (#ensectors)](Enumerations.md#ensectors) enumeration value.

# IMTConSymbol::Sector

Set the economic sector the instrument belongs to.

C++
    
    
    MTAPIRES  IMTConSymbol::Sector(
       const UINT  sector    // economic sector
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Sector(
       EnGTCMode   sector    // economic sector
       )

Python (Manager API)
    
    
    MTConSymbol.Sector

### Parameters

**sector**  
[in] TheIMTConSymbol::EnSectorsenumeration type is used to pass the economic sector.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
