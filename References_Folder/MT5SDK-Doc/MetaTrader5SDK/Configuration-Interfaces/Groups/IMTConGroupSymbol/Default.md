[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / Default

[Previous](Clear.md) | [Next](Path.md)

# IMTConGroupSymbol::Default

Set default values for all parameters of group [symbols](../../Symbols.md).

C++
    
    
    MTAPIRES  IMTConGroupSymbol::Default()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.Default()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Default settings include the settings that are set for symbols in their [IMTConSymbol](../../Symbols/IMTConSymbol.md) configuration.
