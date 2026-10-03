[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Custom Functions](../Custom-Functions.md) / CustomCommand

[Previous](CustomCreateStream.md) | [Next](../../Interface-of-Server-Events.md)

# IMTServerAPI::CustomCommand

A custom command can only be sent to another plugin running within the same cluster. Using this method, you can implement your own data exchange mechanism between the servers of your platform:

  * On one server, create a plugin that sends custom commands using IMTServerAPI::CustomCommand.
  * On the second server, create a plugin that processes commands using [IMTCustomSink::HookPluginCommand](../../Interface-of-Custom-Events/HookPluginCommand.md).



This enables the transfer of any data between them. For example, from a plugin on the main trading server, you can request data on positions from a non-main trading server. Such a request cannot be implemented using standard means since each server uses its own databases. Accordingly, each plugin has access only to its specific database.
    
    
    virtual MTAPIRES  IMTServerAPI::CustomCommand(
       const UINT64   server_id,      // server ID
       LPCVOID        indata,         // input data
       const UINT     indata_len,     // input data size
       LPVOID&        outdata,        // output data
       UINT&          outdata_len     // output data size
       )

### Parameters

**server_id**  
[in] The ID of the server to which the command is sent. Corresponds toIMTConServer::Id.

**indata**  
[in] Data transmitted to the server.

**indata_len**  
[in] Input data size in bytes.

**outdata**  
[out] A reference to the data returned in response to the command. After use, the memory must be freed usingIMTServerAPI::Free.

**outdata_len**  
[out] A reference to the output data size in bytes.

### Return Value

The response code sent by the plugin that processed the custom command. If no plugin processed the command in 30 seconds, the response code [MT_RET_OK_NONE](../../../Return-Codes/Successful-completion.md) will be returned. In case of an error in sending the command, an appropriate response code will be returned.

### Note

To process a custom command, a plugin implementing the [IMTCustomSink::HookPluginCommand](../../Interface-of-Custom-Events/HookPluginCommand.md) hook must be installed on the server.

# IMTServerAPI::CustomCommand

Send a custom command to the server.
    
    
    virtual MTAPIRES  IMTServerAPI::CustomCommand(
       const UINT64   server_id,      // server ID
       IMTByteStream*  indata,      // input data
       IMTByteStream*  outdata,     // output data
       )

### Parameters

**server_id**  
[in] The ID of the server to which the command is sent. Corresponds toIMTConServer::Id.

**indata**  
[in] A pointer to thedata stream objecttransmitted to the server.

**outdata**  
[out] A pointer to thedata steam objectreturned in response to the command.

### Return Value

The response code sent by the plugin that processed the custom command. If no plugin processed the command, the response code [MT_RET_OK_NONE](../../../Return-Codes/Successful-completion.md) will be returned. In case of an error in sending the command, an appropriate response code will be returned.

### Note

To process a custom command, a plugin implementing the [IMTCustomSink::HookPluginCommand](../../Interface-of-Custom-Events/HookPluginCommand.md) hook must be installed on the server.
