[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Industry

[Previous](Sector.md) | [Next](Country.md)

# IMTConSymbol::Industry

Get the industry branch the instrument belongs to.

C++
    
    
    UINT  IMTConSymbol::Industry()  const

.NET (Gateway/Manager API)
    
    
    EnIndustries  CIMTConSymbol.Industry()

Python (Manager API)
    
    
    MTConSymbol.Industry

### Return Value

[IMTConSymbol::EnIndustries (#enindustries)](Enumerations.md#enindustries) enumeration value.

# IMTConSymbol::Industry

Set the industry branch the instrument belongs to.

C++
    
    
    MTAPIRES  IMTConSymbol::Industry(
       const UINT    industry  // industry type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Industry(
       EnIndustries  industry  // industry type
       )

Python (Manager API)
    
    
    MTConSymbol.Industry

### Parameters

**industry**  
[in] TheIMTConSymbol::EnIndustriesenumeration type is used to pass the industry type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
