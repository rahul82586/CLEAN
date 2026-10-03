[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon Name

[Previous](IMTCon-Clear.md) | [Next](IMTCon-ProviderType.md)

# IMTConKYC::Name

Get the name of the KYC provider configuration.

C++
    
    
    LPCWSTR  IMTConKYC::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConKYC.Name()

### Return Value

If successful, the method returns a pointer to a string with the configuration name. Otherwise, NULL is returned.

### Note

A pointer to the resulting string is valid for the lifetime of the [IMTConKYC](../IMTCon.md) object.

# IMTConKYC::Name

Set the name of the KYC provider configuration.

C++
    
    
    MTAPIRES  IMTConKYC::Name(
       LPCWSTR  name      // Provider configuration name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConKYC.Name(
       srting   name      // Provider configuration name
       )

### Parameters

**name**  
[in] Provider configuration name.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

The name length is limited to 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be truncated to this length.
