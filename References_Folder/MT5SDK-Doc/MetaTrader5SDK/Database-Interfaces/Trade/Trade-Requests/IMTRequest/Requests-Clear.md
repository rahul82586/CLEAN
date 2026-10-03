[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Clear

[Previous](Requests-Assign.md) | [Next](Requests-Print.md)

# IMTRequest::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTRequest::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
