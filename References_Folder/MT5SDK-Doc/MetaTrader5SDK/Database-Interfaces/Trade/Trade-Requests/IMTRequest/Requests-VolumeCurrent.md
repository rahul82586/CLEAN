[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests VolumeCurrent

[Previous](Requests-VolumeExt.md) | [Next](Requests-VolumeCurrentExt.md)

# IMTRequest::VolumeCurrent

Get the current unfilled (remaining) order volume specified in the request.

C++
    
    
    UINT64  IMTRequest::VolumeCurrent()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTRequest.VolumeCurrent()

### Return Value

Remaining order volume in UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lot).

### Note

The method is used for requests to modify partially filled orders, where it specifies the remaining order volume.

# IMTRequest::VolumeCurrent

Set the current unfilled (remaining) order volume in the request.

C++
    
    
    MTAPIRES  IMTRequest::VolumeCurrent(
       const UINT64  volume      // Volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.VolumeCurrent(
       ulong         volume      // Volume
       )

### Parameters

**volume**  
[in] Remaining order volume in UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lot).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is used for requests to modify partially filled orders, where it specifies the remaining order volume.
