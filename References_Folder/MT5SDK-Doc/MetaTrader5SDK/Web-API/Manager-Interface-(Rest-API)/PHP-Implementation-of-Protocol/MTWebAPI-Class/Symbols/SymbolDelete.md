[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Symbols](../Symbols.md) / SymbolDelete

[Previous](SymbolAdd.md) | [Next](SymbolTotal.md)

# MTWebAPI::SymbolDelete

Delete a symbol configuration with the specified name.
    
    
    MTAPIRES  MTWebAPI::SymbolDelete(
       string      $name        // Symbol name
       )

### Parameters

**$name**  
[in] The name of the symbol that you want to delete.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

  * This method works only when connected to the main trade server. Otherwise, error [MT_RET_ERR_NOTMAIN](../../../../../Return-Codes/API.md) is returned.


  * [The manager account](../../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have rights to connect as an administrator and edit configurations of symbols. Otherwise, error code [MT_RET_ERR_PERMISSIONS](../../../../../Return-Codes/Common-errors.md) is returned.
  * If a symbol with the specified name is not found, the error code [MT_RET_NOTFOUND](../../../../../Return-Codes/Common-errors.md) is returned.
  * The string specifying the group name must be passed in the UTF-8 format.


