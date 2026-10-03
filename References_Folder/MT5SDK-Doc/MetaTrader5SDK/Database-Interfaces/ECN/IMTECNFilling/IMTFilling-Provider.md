[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling Provider

[Previous](IMTFilling-Deviation.md) | [Next](IMTFilling-Comment.md)

# IMTECNFilling::Provider

Get the ID of the provider through which the order is forwarded to the external system.

C++
    
    
    UINT64  IMTECNFilling::Provider()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNFilling.Provider()

### Return Value

The identifier of the provider through which the order is forwarded to the external system.

### Note

The value corresponds to [IMTECNProvider::ProviderID](../IMTECNProvider/IMTProvider-ProviderID.md).

# IMTECNFilling::Provider

Set the identifier of the provider through which the order is forwarded to the external system.

C++
    
    
    MTAPIRES  IMTECNFilling::Provider(
       const UINT64  provider_id  // provider
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.Provider(
       ulong         provider_id  // provider
       )

### Parameters

**provider_id**  
[in] The identifier of the provider through which the order is forwarded to the external system.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The value corresponds to [IMTECNProvider::ProviderID](../IMTECNProvider/IMTProvider-ProviderID.md).
