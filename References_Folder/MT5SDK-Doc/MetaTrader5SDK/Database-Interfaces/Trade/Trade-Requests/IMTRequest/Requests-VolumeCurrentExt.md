[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests VolumeCurrentExt

[Previous](Requests-VolumeCurrent.md) | [Next](Requests-Order.md)

# IMTRequest::VolumeCurrentExt

Get the current unfilled (remaining) increased-precision volume of an order specified in the request.

C++
    
    
    UINT64  IMTRequest::VolumeCurrentExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTRequest.VolumeCurrentExt()

### Return Value

Remaining order volume in UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lot).

### Note

The method is used for requests to modify partially filled orders, where it specifies the remaining order volume.

# IMTRequest::VolumeCurrentExt

Set the current unfilled (remaining) order volume in the request as an increased-precision value.

C++
    
    
    MTAPIRES  IMTRequest::VolumeCurrentExt(
       const UINT64  volume      // Volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.VolumeCurrentExt(
       ulong         volume      // Volume
       )

### Parameters

**volume**  
[in] Remaining order volume in UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lot).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is used for requests to modify partially filled orders, where it specifies the remaining order volume.
