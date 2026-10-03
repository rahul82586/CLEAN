[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Volume

[Previous](PriceTP.md) | [Next](VolumeExt.md)

# IMTDeal::Volume

Gets the volume of a deal.

C++
    
    
    UINT64  IMTDeal::Volume()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTDeal.Volume()

### Return Value

The deal volume in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTDeal::VolumeExt](VolumeExt.md) method.

# IMTDeal::Volume

Sets the volume of a deal.

C++
    
    
    MTAPIRES  IMTDeal::Volume(
       const UINT64  volume      // Deal volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Volume(
       ulong         volume      // Deal volume
       )

### Parameters

**volume**  
[in] The deal volume in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTDeal::VolumeExt](VolumeExt.md) method.
