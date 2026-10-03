[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon ProviderToken

[Previous](IMTCon-ProviderPassword.md) | [Next](IMTCon-Flags.md)

# IMTConKYC::ProviderToken

Get the authorization token used for connection to the KYC provider.

C++
    
    
    LPCWSTR  IMTConKYC::ProviderToken()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConKYC.ProviderToken()

### Return Value

If successful, the method returns a pointer to a string with the token. Otherwise, NULL is returned.

### Note

The availability of (and the need to fill) this parameter depends on the selected KYC provider ([IMTConKYC::ProviderType](IMTCon-ProviderType.md)). Please contact the provider for details.

# IMTConKYC::ProviderToken

Set the authorization token used for connection to the KYC provider.

C++
    
    
    MTAPIRES  IMTConKYC::ProviderToken(
       LPCWSTR  token     // Authorization token
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.ProviderToken(
       srting   token     // Authorization token
       )

### Parameters

**token**  
[in] The authentication token, which is used for connecting to the KYC provider.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

The availability of (and the need to fill) this parameter depends on the selected KYC provider ([IMTConKYC::ProviderType](IMTCon-ProviderType.md)). Please contact the provider for details.
