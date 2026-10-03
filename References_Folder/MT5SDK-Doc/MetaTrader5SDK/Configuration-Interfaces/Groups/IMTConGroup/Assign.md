[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConGroup::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConGroup::Assign(
       const IMTConGroup*  group      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.Assign(
       CIMTConGroup        group      // Source object
       )

### Parameters

**group**  
Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
