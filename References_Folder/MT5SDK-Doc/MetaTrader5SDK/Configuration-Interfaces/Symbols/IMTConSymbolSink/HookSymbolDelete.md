[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolSink](../IMTConSymbolSink.md) / HookSymbolDelete

[Previous](HookSymbolUpdate.md) | [Next](../../Spreads.md)

# IMTConSymbolSink::HookSymbolDelete

Symbol deletion hook.

C++
    
    
    virtual MTAPIRES  IMTConSymbolSink::HookSymbolDelete(
       const UINT64         login,     // Manager login
       const IMTConSymbol*  cfg        // A pointer to the symbol object
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTConSymbolSink.HookSymbolDelete(
       ulong                login,     // Manager login
       CIMTConSymbol        cfg        // Symbol object
       )

### Parameters

**login**  
[in]The login of the managerwho is deleting the symbol. If the symbol is to be deleted by the plugin, 0 is specified in the parameter.

**cfg**  
[in] A pointer to thesymbol object.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called right before deleting a record from the configuration database. The main purpose of this hook is prevent the unwanted deletion of records.
