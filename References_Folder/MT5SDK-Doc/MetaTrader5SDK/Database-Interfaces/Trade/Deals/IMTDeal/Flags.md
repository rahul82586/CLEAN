[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Flags

[Previous](TickSize.md) | [Next](TimeMsc.md)

# IMTDeal::Flags

Get the common flags of a deal.

C++
    
    
    UINT64  IMTDeal::Flags()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDeal.Flags()

### Return Value

Common flags of a deal.

### Note

This method is reserved for future use.

# IMTDeal::Flags

Set the common flags of a deal.

C++
    
    
    MTAPIRES  IMTDeal::Flags(
       const UINT64  flags      // Common flags of a deal
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Flags(
       ulong         flags      // Common flags of a deal
       )

### Parameters

**flags**  
[in] Common flags of a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method is reserved for future use.
