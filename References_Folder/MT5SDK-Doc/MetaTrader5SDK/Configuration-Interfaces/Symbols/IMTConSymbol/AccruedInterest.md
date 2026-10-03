[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / AccruedInterest

[Previous](FaceValue.md) | [Next](SpliceType.md)

# IMTConSymbol::AccruedInterest

Get the accrued interest of a bond.

C++
    
    
    double  IMTConSymbol::AccruedInterest()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.AccruedInterest()

Python (Manager API)
    
    
    MTConSymbol.AccruedInterest

### Return Value

The accrued interest of a bond.

# IMTConSymbol::AccruedInterest

Set the accrued interest of a bond.

C++
    
    
    MTAPIRES  IMTConSymbol::AccruedInterest(
       const double  interest   // Accrued interest
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.AccruedInterest(
       double        interest   // Accrued interest
       )

Python (Manager API)
    
    
    MTConSymbol.AccruedInterest

### Parameters

**value**  
[in] The accrued interest of a bond.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
