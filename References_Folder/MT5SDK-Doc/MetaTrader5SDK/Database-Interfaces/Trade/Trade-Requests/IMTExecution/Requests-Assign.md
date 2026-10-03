[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests Assign

[Previous](Requests-Release.md) | [Next](Requests-Clear.md)

# IMTExecution::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTExecution::Assign(
       const IMTExecution*  exec      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.Assign(
       CIMTExecution        exec      // Source object
       )

### Parameters

**exec**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
