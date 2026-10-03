[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommTier](../IMTConCommTier.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConCommTier::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConCommTier::Assign(
       const IMTConCommTier*  group      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommTier.Assign(
       CIMTConCommTier        group      // Source object
       )

### Parameters

**group**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
