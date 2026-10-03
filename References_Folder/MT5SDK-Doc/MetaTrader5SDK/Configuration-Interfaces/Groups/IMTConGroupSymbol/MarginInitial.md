[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginInitial

[Previous](MarginFlagsDefault.md) | [Next](MarginInitialDefault.md)

# IMTConGroupSymbol::MarginInitial

Get the size of initial symbol margin for the group.

C++
    
    
    double  IMTConGroupSymbol::MarginInitial()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginInitial()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginInitial

### Return Value

The size of initial symbol margin for the group.

# IMTConGroupSymbol::MarginInitial

Set the size of initial symbol margin for the group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::MarginInitial(
       const double  margin      // Initial margin
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.MarginInitial(
       double        margin      // Initial margin
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginInitial

### Parameters

**margin**  
[in] The size of initial symbol margin for the group.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
