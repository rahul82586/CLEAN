[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon ProviderLogin

[Previous](IMTCon-ProviderAddress.md) | [Next](IMTCon-ProviderPassword.md)

# IMTConKYC::ProviderLogin

Get the login of the account used for connecting to the KYC-provider.

C++
    
    
    LPCWSTR  IMTConKYC::ProviderLogin()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConKYC.ProviderLogin()

### Return Value

If successful, the method returns a pointer to a string with the login. Otherwise, NULL is returned.

### Note

The availability of (and the need to fill) this parameter depends on the selected KYC provider ([IMTConKYC::ProviderType](IMTCon-ProviderType.md)). Please contact the provider for details.

# IMTConKYC::ProviderLogin

Set the login of the account used for connecting to the KYC-provider.

C++
    
    
    MTAPIRES  IMTConKYC::ProviderLogin(
       LPCWSTR  login     // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.ProviderLogin(
       srting   login     // Login
       )

### Parameters

**name**  
[in] The login of the account used for connecting to the KYC-provider.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

The availability of (and the need to fill) this parameter depends on the selected KYC provider ([IMTConKYC::ProviderType](IMTCon-ProviderType.md)). Please contact the provider for details.
