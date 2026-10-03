[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal Provider

[Previous](IMTHistoryDeal-Commission.md) | [Next](../IMTHistoryDealArray.md)

# IMTECNHistoryDeal::Provider

Get the identifier of the provider through which the deal was executed.

C++
    
    
    UINT64  IMTECNHistoryDeal::Provider()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTECNHistoryDeal.Provider()

### Return Value

The identifier of the provider through which the deal was executed.

### Note

The value corresponds to [IMTECNProvider::ProviderID](../IMTECNProvider/IMTProvider-ProviderID.md).

# IMTECNHistoryDeal::Provider

Set the identifier of the provider through which the deal was executed.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::Provider(
       const UINT64  provider_id  // provider
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.Provider(
       ulong         provider_id  // provider
       )

### Parameters

**provider_id**  
[in] The identifier of the provider through which the deal was executed.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The value corresponds to [IMTECNProvider::ProviderID](../IMTECNProvider/IMTProvider-ProviderID.md).

A gateway or MetaTrader 5 cluster is used as a provider.
