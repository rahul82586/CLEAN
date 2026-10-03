[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAgreement](../IMTConAccountAgreement.md) / CaptionType

[Previous](Clear.md) | [Next](CaptionCustomText.md)

# IMTConAccountAgreement::CaptionType

Get the agreement type.

C++
    
    
    UINT  IMTConAccountAgreement::Type()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAccountAgreement.Type()

### Return Value

One of the values of the [IMTConAccountAgreement::EnCaptionType (#encaptiontype)](Enumerations.md#encaptiontype) values.

# IMTConAccountAgreement::CaptionType

Set the agreement type.

C++
    
    
    MTAPIRES  IMTConAccountAgreement::Type(
       const UINT  type      // Agreement type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAgreement.Type(
       uint        type      // Agreement type
       )

### Parameters

**type**  
[in] The agreement type is passed using theIMTConAccountAgreement::EnCaptionTypeenumeration.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.
