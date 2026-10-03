[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Exported Functions](../Exported-Functions.md) / MTGatewayCreateLocal

[Previous](MTGatewayCreate.md) | [Next](../CMTGatewayAPIFactory.md)

# MTGatewayCreateLocal

MTGatewayCreateLocal exported function creates a new [IMTGatewayAPI](../Main-Interface.md) interface copy with predetermined parameters submitted in the command line and returns a pointer to it.
    
    
    MTAPIRES  MTGatewayCreate(
       MTGatewayInfo&   info      // Reference to MTGatewayInfo
       IMTGatewayAPI**  gateway   // Pointer to a pointer o the interface
       int              argc      // Number of command line parameters
       wchar_t**        argv      // Command line parameters
       )

### Parameters

**info**  
[out] A reference to theMTGatewayInfostructure.

**gateway**  
[out] A pointer to a pointer to the createdIMTGatewayAPIinterface.

**argc**  
[in] Number ofcommand line parameters.

**argv**  
[in]Parameters of the command linethat launched the gateway/data feed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

This function type is called instead of [MTGatewayCreate](MTGatewayCreate.md), in case additional parameters were indicated in a command line during the run of a gateway/data feed executable file. Parameters of the command line are passed to the argc and argv parameters. The following additional running parameters are possible:

  * /name:XXX — the name of the gateway/data feed that will be used for the folder, in which the application data (like operation logs) will be stored. This folder is created in the directory where the executable file of the gateway/data feed is located.
  * /address:XXX — the default address on which the server port GatewayAPI runs;
  * /login:XXX — the default login that will be used for connecting history and trade servers to a gateway/data feed.
  * /password:XXX — the default password that will be used for connecting history and trade servers to a gateway/data feed.
  * /timezone:XXX — time zone in minutes (for example, GMT +01:00 corresponds to 60, GMT -01:00 corresponds to -60), that will be used in gateway/data feed settings.
  * /timecorrect — if this parameter is used, DST adjustment is enabled.
  * /standalone — when this flag is enabled, the [IMTGatewaySink::OnGatewayShutdown](../Event-Interface/OnGatewayShutdown.md) event handler, which notifies of trading platform shutdown, will not be called.
  * /description — the history server runs a gateway/data feed with this parameter, when it is required to get the description of the gateway/data feed module. The description is used for including the module in the list of available gateways/data feeds when creating/modifying the corresponding configuration via MetaTrader 5 Administrator. In addition, the description is used for convenient managing the gateway/data feed settings via MetaTrader 5 Administrator — this description determines modes of the gateway/data feed operation, its default setting, etc. The description represents a [MTGatewayInfo](../../Structures/MTGatewayInfo.md) structure.



> The address, on which the gateway/data feed runs, and the parameters of the account for connecting to it are provided to facilitate application debugging.
