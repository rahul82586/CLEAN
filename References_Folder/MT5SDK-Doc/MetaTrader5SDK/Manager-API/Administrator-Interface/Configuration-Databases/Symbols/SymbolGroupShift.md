[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolGroupShift

[Previous](SymbolGroupDelete.md) | [Next](SymbolGroupTotal.md)

# IMTAdminAPI::SymbolGroupShift

Change the position of a subgroup of symbols in a list.

C++
    
    
    MTAPIRES  IMTAdminAPI::SymbolGroupShift(
       const UINT  pos,       // the position of the symbol subgroup
       const int   shift      // shift
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.SymbolGroupShift(
       uint        pos,       // the position of the symbol subgroup
       int         shift      // shift
       )

Python
    
    
    AdminAPI.SymbolGroupShift(
       int         pos,       # the position of the symbol subgroup
       int         shift      # shift
       )

### Parameters

**pos**  
[in] Position of the symbol subgroup, starting from 0.

**shift**  
[in] The shift of the subgroup relative to its current position. A negative value means shift towards the top of the list, a positive value shifts the subgroup towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The subgroup position can only be changed from the applications running on the main server. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned.
