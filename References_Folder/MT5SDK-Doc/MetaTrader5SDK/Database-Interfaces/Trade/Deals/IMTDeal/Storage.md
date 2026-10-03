[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Storage

[Previous](Value.md) | [Next](Commission.md)

# IMTDeal::Storage

Get the swap size for a deal.

C++
    
    
    double  IMTDeal::Storage()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.Storage()

### Return Value

The swap size for a deal.

# IMTDeal::Storage

Set the swap size for a deal.

C++
    
    
    MTAPIRES  IMTDeal::Storage(
       const double  storage      // Swap
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Storage(
       double        storage      // Swap
       )

### Parameters

**storage**  
[in] The swap size for a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
