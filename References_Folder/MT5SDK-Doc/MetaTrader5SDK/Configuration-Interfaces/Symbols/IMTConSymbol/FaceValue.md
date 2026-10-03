[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / FaceValue

[Previous](OrderFlags.md) | [Next](AccruedInterest.md)

# IMTConSymbol::FaceValue

Get the face value of a bond.

C++
    
    
    double  IMTConSymbol::FaceValue()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.FaceValue()

Python (Manager API)
    
    
    MTConSymbol.FaceValue

### Return Value

The face value of a bond.

# IMTConSymbol::FaceValue

Set the face value of a bond.

C++
    
    
    MTAPIRES  IMTConSymbol::FaceValue(
       const double  value      // Face value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.FaceValue(
       double        value      // Face value
       )

Python (Manager API)
    
    
    MTConSymbol.FaceValue

### Parameters

**value**  
[in] The face value of a bond.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
