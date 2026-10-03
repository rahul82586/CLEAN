[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAgreement](../IMTConAccountAgreement.md) / CaptionCustomText

[Previous](CaptionType.md) | [Next](URL.md)

# IMTConAccountAgreement::Name

Get the name of the user agreement.

C++
    
    
    LPCWSTR  IMTConAccountAgreement::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConAccountAgreement.Name()

### Return Value

The method returns a pointer to the string with the server name on success. Otherwise, NULL is returned.

### Note

The method is only used for the [IMTConAccountAgreement::CAPTION_CUSTOM (#encaptiontype)](Enumerations.md#encaptiontype) agreement types.

# IMTConAccountAgreement::Name

Setting the name for the user agreement.

C++
    
    
    MTAPIRES  IMTConAccountAgreement::Name(
       LPCWSTR  name      // Agreement name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAgreement.Name(
       string   name      // Agreement name
       )

### Parameters

**name**  
[in] The name of the user agreement.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is only used for the [IMTConAccountAgreement::CAPTION_CUSTOM (#encaptiontype)](Enumerations.md#encaptiontype) agreement types.
