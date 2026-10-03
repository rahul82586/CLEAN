[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests Clear

[Previous](Requests-Assign.md) | [Next](Requests-Print.md)

# IMTConfirm::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConfirm::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
