[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Volume

[Previous](Requests-Flags.md) | [Next](Requests-VolumeExt.md)

# IMTRequest::Volume

Gets the operation volume specified in a request.

C++
    
    
    UINT64  IMTRequest::Volume()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTRequest.Volume()

### Return Value

The operation volume specified in a request in the UINT64 format (one unit corresponds to 1/10,000 of a lot).

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTRequest::VolumeExt](Requests-VolumeExt.md) method.

# IMTRequest::Volume

Sets the operation volume in a request.

C++
    
    
    MTAPIRES  IMTRequest::Volume(
       const UINT64  volume      // Volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.Volume(
       ulong         volume      // Volume
       )

### Parameters

**volume**  
[in] The operation volume specified in a request in the UINT64 format (one unit corresponds to 1/10,000 of a lot).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method operates with [the standard volume accuracy (#volume)](../../../../Development-Features/README.md#volume) (4 decimal places). For extended volume accuracy, use the [IMTRequest::VolumeExt](Requests-VolumeExt.md) method.
