[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / Exchange

[Previous](Category.md) | [Next](CFI.md)

# IMTConSymbol::Exchange

Get the name of the exchange in which the symbol is traded.

C++
    
    
    LPCWSTR  IMTConSymbol::Exchange()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSymbol.Exchange()

Python (Manager API)
    
    
    MTConSymbol.Exchange

### Return Value

If successful, it returns a pointer to a string with the name of the exchange. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConSymbol](../IMTConSymbol.md) object.

# IMTConSymbol::Exchange

Set the name of the exchange in which the symbol is traded.

C++
    
    
    MTAPIRES  IMTConSymbol::Exchange(
       LPCWSTR  exchange    // The name of the exchange
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.Exchange(
       string   exchange    // The name of the exchange
       )

Python (Manager API)
    
    
    MTConSymbol.Exchange

### Parameters

**exchange**  
[in] The name of the exchange in which the symbol is traded.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum length of the exchange name is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it is cut to this length.
