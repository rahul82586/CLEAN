[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolSink](../IMTConSymbolSink.md) / HookSymbolUpdate

[Previous](HookSymbolAdd.md) | [Next](HookSymbolDelete.md)

# IMTConSymbolSink::HookSymbolUpdate

Hook for the update of symbol settings.

C++
    
    
    virtual MTAPIRES  IMTConSymbolSink::HookSymbolUpdate(
       const UINT64         login,     // Manager login
       const IMTConSymbol*  cfg,       // A pointer to the current symbol
       IMTConSymbol*        new_cfg    // A pointer to the updated symbol
       )

.NET (Gateway/Manager API)
    
    
    virtual MTRetCode  CIMTConSymbolSink.HookSymbolUpdate(
       ulong                login,     // Manager login
       CIMTConSymbol        cfg,       // Current symbol
       CIMTConSymbol        new_cfg    // Updated symbol
       )

### Parameters

**login**  
[in]The login of the manager, who is going to update the symbol settings. If the symbol is to be updated by the plugin, 0 is specified in the parameter.

**cfg**  
[in] A pointer to thecurrent symbol object.

**new_cfg**  
[out] A pointer to thesymbol objectafter making change.

### Return Value

In case there are no handlers if this event, [MT_RET_OK](../../../Return-Codes/Successful-completion.md) is returned.

### Note

The hook is called right before making changes to the configuration database. The main purpose of this hook is to modify an entry that is being updated, and, if necessary, to prevent the unwanted change of records.
