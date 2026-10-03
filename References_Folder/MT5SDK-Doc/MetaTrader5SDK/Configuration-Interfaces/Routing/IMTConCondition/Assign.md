[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Routing](../../Routing.md) / [IMTConCondition](../IMTConCondition.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConCondition::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConCondition::Assign(
       const IMTConCondition*  config      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCondition.Assign(
       CIMTConCondition        config      // Source object
       )

### Parameters

**config**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
