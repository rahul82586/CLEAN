[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / Symbol

[Previous](Dealer.md) | [Next](Digits.md)

# IMTOrder::Symbol

Gets the symbol of an order.

C++
    
    
    LPCWSTR  IMTOrder::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTOrder.Symbol()

Python
    
    
    MTOrder.Symbol()

### Return Value

If successful, it returns a pointer to a string with the name and path to the symbol. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTOrder](../IMTOrder.md) object.

# IMTOrder::Symbol

Set the symbol of an order.

C++
    
    
    MTAPIRES  IMTOrder::Symbol(
       LPCWSTR  symbol      // Symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.Symbol(
       string   symbol      // Symbol
       )

Python
    
    
    MTOrder.Symbol()

### Parameters

**symbol**  
[in] A trading instrument of an order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

[IMTConSymbol::Symbol](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md) value is used as the symbol name.
