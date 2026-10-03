[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAgreement](../IMTConAccountAgreement.md) / Clear

[Previous](Assign.md) | [Next](CaptionType.md)

# IMTConAccountAgreement::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConAccountAgreement::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAgreement.Clear()

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method clears all field values and removes all nested objects.
