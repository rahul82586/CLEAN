[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginHedged

[Previous](MarginStopLimitDefault.md) | [Next](MarginHedgedDefault.md)

# IMTConGroupSymbol::MarginHedged

Gets the value of the hedged margin.

C++
    
    
    double  IMTConGroupSymbol::MarginHedged()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginHedged()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginHedged

### Return Value

The hedged margin value.

### Note

Hedged margin is the margin charged for each hedged lot of positions. If the initial margin is specified for a symbol, the hedged margin is specified as an absolute value (in monetary terms). If the initial margin is not set (equal to 0), the contract size is specified. The margin is calculated by the appropriate formula in accordance with the type of the financial instrument, using the specified contract size.

# IMTConGroupSymbol::MarginHedged

Sets the value of the hedged margin.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::MarginHedged(
       const double  margin      // Hedged margin
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.MarginHedged(
       double        margin      // Hedged margin
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginHedged

### Parameters

**margin**  
[in] The value of the hedged margin.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Hedged margin is the margin charged for each hedged lot of positions. If the initial margin is specified for a symbol, the hedged margin is specified as an absolute value (in monetary terms). If the initial margin is not set (equal to 0), the contract size is specified. The margin is calculated by the appropriate formula in accordance with the type of the financial instrument, using the specified contract size.
