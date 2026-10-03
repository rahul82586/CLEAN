[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests Print

[Previous](Requests-Clear.md) | [Next](Requests-ID.md)

# IMTConfirm::Print

Get the string description of trade request confirmation.

C++
    
    
    LPCWSTR  IMTConfirm::Print(
       MTAPISTR&  string      // Confirmation description string
       )  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConfirm.Print()

### Parameters

**string**  
[out] The request confirmation description string.

### Return Value

A pointer to string that is passed as a parameter.
