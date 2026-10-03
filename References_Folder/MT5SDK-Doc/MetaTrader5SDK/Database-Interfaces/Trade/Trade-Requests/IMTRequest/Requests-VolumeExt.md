[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests VolumeExt

[Previous](Requests-Volume.md) | [Next](Requests-VolumeCurrent.md)

# IMTRequest::VolumeExt

Gets the operation volume in a request, with an extended accuracy.

C++
    
    
    UINT64  IMTRequest::VolumeExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTRequest.VolumeExt()

### Return Value

The operation volume set in the request, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTRequest::Volume](Requests-Volume.md) method.

# IMTRequest::VolumeExt

Sets the operation volume in a request, with an extended accuracy.

C++
    
    
    MTAPIRES  IMTRequest::VolumeExt(
       const UINT64  volume      // Volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.VolumeExt(
       ulong         volume      // Volume
       )

### Program Parameters

**volume**  
[in] The operation volume in the request, in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the extended volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (8 decimal places). For standard volume accuracy, use the [IMTRequest::Volume](Requests-Volume.md) method.
