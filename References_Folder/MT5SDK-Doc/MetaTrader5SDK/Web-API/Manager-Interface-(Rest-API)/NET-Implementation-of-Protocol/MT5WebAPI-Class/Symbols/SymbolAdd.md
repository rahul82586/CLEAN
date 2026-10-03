[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Symbols](../Symbols.md) / SymbolAdd

[Previous](../Symbols.md) | [Next](SymbolDelete.md)

# MT5WebAPI.SymbolAdd

Add or change a symbol configuration on the server.
    
    
    MTRetCode  MT5WebAPI.SymbolAdd(
       MTConSymbol      symbol,    // Description of the symbol to create
       out MTConSymbol  newSymbol  // Description of the created symbol
       )

### Parameters

**symbol**  
[in] The MTConSymbol structure that describes the configuration of the symbol that you need to create. Description of the structure parameters is provided in the"Data Structure"section.

**newSymbol**  
[Out] The MTConSymbol object that describes the configuration of the symbol that you need to create. Description of the structure parameters is provided in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

  * To create a symbol in the MTConSymbol structure, you only need to specify its name.


  * When creating an object using the MTConSymbol.CreateDefault method, all the structure fields are filled with zeros or default values. When updating a symbol, you should either set all its parameters manually or get its configuration using the [MT5WebAPI::SymbolNext](SymbolNext.md) or [MT5WebAPI::SymbolGet](SymbolGet.md) method and edit it appropriately.


  * This method works only when connected to the main trade server. Otherwise, error [MT_RET_ERR_NOTMAIN](../../../../../Return-Codes/API.md) is returned.
  * When the command is run the presence of the symbol you are adding is checked. A key field for comparison is the name of the symbol. If such a symbol already exists, its settings are updated.
  * Before adding, the correctness of the record is checked. If the record is incorrect, the error code [MT_RET_ERR_PARAMS](../../../../../Return-Codes/Common-errors.md) is returned.
  * To run the command, [the manager account](../../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have rights to connect as an administrator and edit symbol configurations. Otherwise, error code [MT_RET_ERR_PERMISSIONS](../../../../../Return-Codes/Common-errors.md) is returned.
  * To enable a newly added symbol, [restart the main trade server](../Service-Commands/ServerRestart.md).


