[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestArray](../Requests-IMTRequestArray.md) / Requests UpdateCopy

[Previous](Requests-Update.md) | [Next](Requests-Shift.md)

# IMTRequestArray::UpdateCopy

Change a trade request at the specified position of an array by copying the parameters of a passed object of a trade request.

C++
    
    
    MTAPIRES  IMTRequestArray::UpdateCopy(
       const UINT          pos,         // Position
       const IMTRequest*   request      // An object of a trade request
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequestArray.UpdateCopy(
       uint                pos,         // Position
       CIMTRequest         request      // An object of a trade request
       )

### Parameters

**pos**  
[in] Position of a trade request in an array, starting with 0.

**order**  
[in] An object of a trade request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of the request object into an object of a trade request at the specified position of an array.
