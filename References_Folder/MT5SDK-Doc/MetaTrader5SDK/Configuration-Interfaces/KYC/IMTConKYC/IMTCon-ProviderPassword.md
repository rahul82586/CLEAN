[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon ProviderPassword

[Previous](IMTCon-ProviderLogin.md) | [Next](IMTCon-ProviderToken.md)

# IMTConKYC::ProviderPassword

Get the password of the account used for connecting to the KYC-provider.

C++
    
    
    LPCWSTR  IMTConKYC::ProviderPassword()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConKYC.ProviderPassword()

### Return Value

If successful, the method returns a pointer to a string with the password. Otherwise, NULL is returned.

### Note

The availability of (and the need to fill) this parameter depends on the selected KYC provider ([IMTConKYC::ProviderType](IMTCon-ProviderType.md)). Please contact the provider for details.

# IMTConKYC::ProviderPassword

Set the password of the account used for connecting to the KYC-provider.

C++
    
    
    MTAPIRES  IMTConKYC::ProviderPassword(
       LPCWSTR  password  // Password
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.ProviderPassword(
       srting   password  // Password
       )

### Parameters

**password**  
[in] The password of the account used for connecting to the KYC-provider.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

The availability of (and the need to fill) this parameter depends on the selected KYC provider ([IMTConKYC::ProviderType](IMTCon-ProviderType.md)). Please contact the provider for details.
