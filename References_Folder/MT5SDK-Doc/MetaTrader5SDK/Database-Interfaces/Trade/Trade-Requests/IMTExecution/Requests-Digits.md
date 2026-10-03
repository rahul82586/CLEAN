[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests Digits

[Previous](Requests-SymbolNew.md) | [Next](Requests-Comment.md)

# IMTExecution::Digits

Get the number of decimal places in the price of a symbol, for which trade execution is performed.

C++
    
    
    UINT  IMTExecution::Digits()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTExecution.Digits()

### Return Value

The number of decimal places in the price of a symbol, for which trade execution is performed.

# IMTExecution::Digits

Set the number of decimal places in the price of a symbol, for which trade execution is performed.

C++
    
    
    MTAPIRES  IMTExecution::Digits(
       const UINT  digits      // Decimal places
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.Digits(
       uint        digits      // Decimal places
       )

### Parameters

**digits**  
[in] The number of decimal places in the price of a symbol, for which trade execution is performed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum number of decimal places is 8.
