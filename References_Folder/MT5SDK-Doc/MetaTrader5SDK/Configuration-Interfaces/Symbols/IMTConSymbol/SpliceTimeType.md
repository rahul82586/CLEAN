[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SpliceTimeType

[Previous](SpliceType.md) | [Next](SpliceTimeDays.md)

# IMTConSymbol::SpliceTimeType

Gets the date of splicing of futures contracts.

C++
    
    
    UINT  IMTConSymbol::SpliceTimeType()  const

.NET (Gateway/Manager API)
    
    
    EnSpliceTimeType  CIMTConSymbol.SpliceTimeType()

Python (Manager API)
    
    
    MTConSymbol.SpliceTimeType

### Return Value

A value of the [IMTConSymbol::EnSpliceTimeType (#ensplicetimetype)](Enumerations.md#ensplicetimetype) enumeration.

# IMTConSymbol::SpliceTimeType

Sets the date of splicing of futures contracts.

C++
    
    
    MTAPIRES  IMTConSymbol::SpliceTimeType(
       const UINT        time_type  // Splicing date
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SpliceTimeType(
       EnSpliceTimeType  time_type  // Splicing date
       )

Python (Manager API)
    
    
    MTConSymbol.SpliceTimeType

### Parameters

**time_type**  
[in] Futures contracts splicing date.IMTConSymbol::EnSpliceTimeTypeis used to pass the date.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
