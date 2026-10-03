[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests Group

[Previous](Requests-Login.md) | [Next](Requests-Flags.md)

# IMTExecution::Group

Gets the group in the MetaTrader 5 platform, for the clients of which that execution can be applied.

C++
    
    
    LPCWSTR  IMTExecution::Group()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTExecution.Group()

### Return Value

If successful, it returns a pointer to a string with the client group. Otherwise, it returns NULL.

### Note

This field in a trade execution is optional.

# IMTExecution::Group

Sets the group in the MetaTrader 5 platform, for the clients of which that execution can be applied.

C++
    
    
    MTAPIRES  IMTExecution::Group(
       LPCWSTR  group      // Group
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.Group(
       string   group      // Group
       )

### Parameters

**group**  
[in] The client group in the MetaTrader 5 platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This field in a trade execution is optional.
