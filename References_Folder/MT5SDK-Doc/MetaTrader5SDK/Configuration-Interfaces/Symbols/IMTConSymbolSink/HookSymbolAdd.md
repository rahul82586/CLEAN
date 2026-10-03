[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolSink](../IMTConSymbolSink.md) / HookSymbolAdd

[Previous](OnSymbolSync.md) | [Next](HookSymbolUpdate.md)

# IMTConSymbolSink::HookSymbolAdd

Hook for adding of the new symbol.

C++
    
    
    virtual MTAPIRES  IMTConSymbolSink::HookSymbolAdd(
       const UINT64         login,     // Manager login
       IMTConSymbol*        new_cfg    // A pointer to the symbol object
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTConSymbolSink.HookSymbolAdd(
       ulong                login,     // Manager login
       CIMTConSymbol        new_cfg    // Symbol object
       )

### Parameters

**login**  
[in]The login of the manager, who is adding the new symbol. If the new symbol is being added by the plugin, 0 is specified in the parameter.

**new_cfg**  
[in/out] A pointer theobject of the symbol to be added.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called right before adding a symbol configuration to the client base. The main purpose of this hook is to modify an entry that is added, and, if necessary, to prevent the addition of unwanted records.
