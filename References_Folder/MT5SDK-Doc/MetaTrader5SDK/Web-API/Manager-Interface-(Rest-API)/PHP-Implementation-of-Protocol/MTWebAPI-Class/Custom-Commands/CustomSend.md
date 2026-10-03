[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Custom Commands](../Custom-Commands.md) / CustomSend

[Previous](../Custom-Commands.md) | [Next](../../Examples.md)

# MTWebAPI::CustomSend

Send a custom command to the server.
    
    
    MTAPIRES  MTWebAPI::CustomSend(
       string                $command,       // Command
       array(string,string)  $params,        // Parameters
       string                $body,          // Additional body
       array(string,string)  &$answer,       // Response command
       string                &$answer_body   // Additional body of the response
       )

### Parameters

**$command**  
[in] A custom command.

**$params**  
[in] Array of parameters of the custom command. For example:

**$body**  
[in] Additional body of the command.

**$ &answer**  
[out] Array of parameters of the command of the server answer. For example:

**$ &answer_body**  
[out] Additional body of the server answer.

  * $params[PARAM1] = VALUE1;
  * $params[PARAM2] = VALUE2;


  * $answer[PARAM1] = VALUE1;
  * $answer[PARAM2] = VALUE2;



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The strings specifying the command and the additional body must be passed in the UTF-8 format.
