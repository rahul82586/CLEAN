[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests Print

[Previous](Requests-Clear.md) | [Next](Requests-ID.md)

# IMTExecution::Print

Get a string description of a trade execution.

C++
    
    
    LPCWSTR  IMTExecution::Print(
       MTAPISTR&  string      // Trade execution description string
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTExecution.Print()

### Parameters

**string**  
[in] Trade execution description string.

### Return Value

A pointer to string that is passed as a parameter.
