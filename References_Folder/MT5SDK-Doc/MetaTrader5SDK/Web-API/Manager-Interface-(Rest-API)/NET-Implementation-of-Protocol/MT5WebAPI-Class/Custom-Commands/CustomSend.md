[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Custom Commands](../Custom-Commands.md) / CustomSend

[Previous](../Custom-Commands.md) | [Next](../../WebTrader.md)

# MT5WebAPI.CustomSend

Send a custom command to the server.
    
    
    MTRetCode  MT5WebAPI.CustomSend(
       string                     command,     // Command
       Dictionary(string,string)  parameters,  // Parameter
       byte[]                     body,        // Additional body
       out string                 answer       // Server response
       )

### Parameters

**command**  
[in] A custom command.

**parameters**  
[in] Array of parameters of the custom command.

**body**  
[in] Additional body of the command.

**answer**  
[out] Server response. Both a response command and an additional body can be returned in the response.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
