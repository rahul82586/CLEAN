[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SpliceType

[Previous](AccruedInterest.md) | [Next](SpliceTimeType.md)

# IMTConSymbol::SpliceType

Getting the type of splicing of futures contracts.

C++
    
    
    UINT  IMTConSymbol::SpliceType()  const

.NET (Gateway/Manager API)
    
    
    EnSpliceType  CIMTConSymbol.SpliceType()

Python (Manager API)
    
    
    MTConSymbol.SpliceType

### Return Value

A value of the [IMTConSymbol::EnSpliceType (#ensplicetype)](Enumerations.md#ensplicetype) enumeration.

# IMTConSymbol::SpliceType

Setting the type of splicing of futures contracts.

C++
    
    
    MTAPIRES  IMTConSymbol::AccruedInterest(
       const UINT    type  // Splicing type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.AccruedInterest(
       EnSpliceType  type  // Splicing type
       )

Python (Manager API)
    
    
    MTConSymbol.SpliceType

### Parameters

**type**  
[in] Futures contracts splicing type.IMTConSymbol::EnSpliceTypeis used to pass the type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
