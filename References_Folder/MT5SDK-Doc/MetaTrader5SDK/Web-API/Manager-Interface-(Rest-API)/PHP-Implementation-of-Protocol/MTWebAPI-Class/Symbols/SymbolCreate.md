[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Symbols](../Symbols.md) / SymbolCreate

[Previous](../Symbols.md) | [Next](SymbolAdd.md)

# MTWebAPI::SymbolCreate

Create an object of a symbol.
    
    
    MTUser  MTWebAPI::SymbolCreate()

### Return Value

It returns a pointer to the created MTConSymbol object used to describe the symbol. The symbol parameters are described in the ["Data Structure"](../../../Configuration-Databases/Symbols/Data-Structure.md).

### Note

This method creates an MTConSymbol object completely filled with default symbol parameters.
