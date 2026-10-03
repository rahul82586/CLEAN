[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolGetLight

[Previous](SymbolGet.md) | [Next](SymbolExist.md)

# IMTReportAPI::SymbolGetLight

Get an eased configuration of a symbol.
    
    
    MTAPIRES  IMTReportAPI::SymbolGetLight(
       LPCWSTR       name,        // Symbol name
       IMTConSymbol  *symbol      // An object of the symbol configuration
       )

### Parameters

**name**  
[in] Symbol name. TheIMTConSymbol::Symbol()value is used as the name.

***symbol**  
[out] An object of the symbol configuration. The symbol object must be first created using theIMTReportAPI::SymbolCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method submits all symbol parameters except quoted and trade sessions settings ([IMTConSymbol::Session*](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/SessionQuoteAdd.md)).
