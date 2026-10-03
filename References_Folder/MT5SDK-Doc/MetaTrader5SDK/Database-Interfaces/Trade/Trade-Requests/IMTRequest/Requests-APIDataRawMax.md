[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests APIDataRawMax

[Previous](Requests-APIDataRaw.md) | [Next](Requests-ApiDataClear.md)

# IMTRequest::APIDataRawMax

Get the maximum possible size of custom parameters of a trade request.

C++
    
    
    UINT  IMTRequest::APIDataRawMax()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTRequest.APIDataRawMax()

### Return Value

the maximum possible size of custom parameters of a trade request in bytes.

### Note

Use this method when reading and writing custom parameters in a raw form via [IMTRequest::APIDataRaw](Requests-APIDataRaw.md).
