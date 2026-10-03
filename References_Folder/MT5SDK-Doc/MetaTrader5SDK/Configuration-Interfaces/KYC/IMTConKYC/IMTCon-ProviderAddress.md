[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon ProviderAddress

[Previous](IMTCon-ProviderType.md) | [Next](IMTCon-ProviderLogin.md)

# IMTConKYC::ProviderAddress

Get the KYC provider's server address in the configuration.

C++
    
    
    LPCWSTR  IMTConKYC::ProviderAddress()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConKYC.ProviderAddress()

### Return Value

If successful, a pointer to a string with the server address is returned. Otherwise, NULL is returned.

### Note

The availability of (and the need to fill) this parameter depends on the selected KYC provider ([IMTConKYC::ProviderType](IMTCon-ProviderType.md)). Please contact the provider for details.

# IMTConKYC::ProviderAddress

Set the KYC provider's server address in the configuration.

C++
    
    
    MTAPIRES  IMTConKYC::ProviderAddress(
       LPCWSTR  address   // Server address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.ProviderAddress(
       srting   address   // Server address
       )

### Parameters

**name**  
[in] Provider's server address.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

The availability of (and the need to fill) this parameter depends on the selected KYC provider ([IMTConKYC::ProviderType](IMTCon-ProviderType.md)). Please contact the provider for details.
