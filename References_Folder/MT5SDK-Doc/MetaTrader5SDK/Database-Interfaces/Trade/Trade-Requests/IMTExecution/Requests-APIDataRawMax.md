[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests APIDataRawMax

[Previous](Requests-APIDataRawGet.md) | [Next](Requests-ApiDataClear.md)

# IMTExecution::APIDataRawMax

Get the maximum possible size of custom parameters of a trade execution.

C++
    
    
    UINT  IMTExecution::APIDataRawMax()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTExecution.APIDataRawMax()

### Return Value

the maximum possible size of custom parameters of a trade request in bytes.

### Note

Use this method when reading and writing custom parameters in a raw form via [IMTExecution::APIDataRawGet](Requests-APIDataRawGet.md) and [IMTExecution::APIDataRawSet](Requests-APIDataRawSet.md).
