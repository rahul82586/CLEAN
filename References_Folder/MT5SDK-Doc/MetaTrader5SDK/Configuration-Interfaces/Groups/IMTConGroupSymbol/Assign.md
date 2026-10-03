[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConGroupSymbol::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::Assign(
       const IMTConGroupSymbol*  group      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.Assign(
       CIMTConGroupSymbol        group      // Source object
       )

### Parameters

**group**  
Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
