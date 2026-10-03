[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests Clear

[Previous](Requests-Assign.md) | [Next](Requests-Print.md)

# IMTExecution::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTExecution::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
