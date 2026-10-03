[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests ID

[Previous](Requests-Print.md) | [Next](Requests-Retcode.md)

# IMTConfirm::ID

Get the ID of a trade request.

C++
    
    
    UINT  IMTConfirm::ID()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConfirm.ID()

### Return Value

The ID of a trade request.

# IMTConfirm::ID

Set the ID of a trade request.

C++
    
    
    MTAPIRES  IMTConfirm::ID(
       const UINT  id      // Request ID
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.ID(
       uint        id      // Request ID
       )

### Parameters

**id**  
[in] Trade request ID.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
