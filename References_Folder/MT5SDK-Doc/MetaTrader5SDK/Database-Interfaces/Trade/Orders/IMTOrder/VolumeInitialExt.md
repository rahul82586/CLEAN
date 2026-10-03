[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / VolumeInitialExt

[Previous](VolumeInitial.md) | [Next](VolumeCurrent.md)

# IMTOrder::VolumeInitialExt

Gets the initial order volume with an extended accuracy.

C++
    
    
    UINT64  IMTOrder::VolumeInitialExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTOrder.VolumeInitialExt()

Python
    
    
    MTOrder.VolumeInitialExt()

### Return Value

The initial volume requested in the order, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTOrder::VolumeInitial](VolumeInitial.md) method.

# IMTOrder::VolumeInitialExt

Sets the initial order volume with an extended accuracy.

C++
    
    
    MTAPIRES  IMTOrder::VolumeInitialExt(
       const UINT64  volume      // Initial volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.VolumeInitialExt(
       ulong         volume      // Initial volume
       )

Python
    
    
    MTOrder.VolumeInitialExt()

### Program Parameters

**volume**  
[in] Initial order volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTOrder::VolumeInitial](VolumeInitial.md) method.
