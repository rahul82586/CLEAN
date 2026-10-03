[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Interface of Custom Events](../Interface-of-Custom-Events.md) / HookWebAPICommand

[Previous](HookManagerCommand.md) | [Next](HookPluginCommand.md)

# IMTCustomSink::HookWebAPICommand

A hook of an event of execution of a [Web client's custom command](../../Web-API/Protocol-Extension.md).
    
    
    MTAPIRES  IMTCustomSink::HookWebAPICommand(
       const UINT64          session,         // Session identifier
       LPCWSTR               ip,              // IP address of the Web client
       const IMTConManager*  manager,         // An object of the manager configuration
       LPCWSTR               command,         // A command of the Web client
       IMTByteStream*        indata,          // Input data
       IMTByteStream*        outdata,         // Output data
       )

### Parameters

**session**  
[in] A unique ID of Web client connection session. This identifier does not change during the connection session. Each ID is unique for the entire cluster of the platform and is never repeated.

**ip**  
[in] The IP address of the manager who has sent the custom command.

**manager**  
[in] The object of configuration of a manager account using which the Web client connects.

**command**  
[in] A command sent by a Web client.

**indata**  
[in]The object of the data streamsent to the server.

**outdata**  
[out] A pointer to theobject of the data streamreturned in response to the command.

### Return Value

If the hook does not handle the event, it returns [MT_RET_OK_NONE](../../Return-Codes/Successful-completion.md). If the event is handled, the return code is forwarded to the Web client together with the outdata buffer.

### Note

The hook is called consistently in accordance with the order of plugins in the list until the first plugin that has returned a response code other than [MT_RET_OK_NONE](../../Return-Codes/Successful-completion.md).

## Features of Client Command Processing in Web API

When reading and sending commands through the indata and outdata parameters respectively, it is necessary to consider the format of Web API commands:
    
    
    COMMAND|PARAM1=VALUE1|PARAM2=VALUE2|\r\n
    additional_body

A command can consist of three elements:

  * A text command of the Web API — in response to a request, the server generates forms this part of the command, which is identical to the received command.
  * Command parameters and their values ​​— each command can have multiple parameters, separated by the character "|". The end of a command is the newline character "\r\n". In response to a request, the server automatically generates one additional parameter: RETCODE=response code returned from a hook.
  * An additional body — this part is used only in commands sent from a server to a client.



The PHP and .NET Web API implementations for sending custom commands feature the [MTWebAPI::CustomSend](../../Web-API/Manager-Interface-(Rest-API)/PHP-Implementation-of-Protocol/MTWebAPI-Class/Custom-Commands/CustomSend.md) and [MTWebAPI.CustomSend](../../Web-API/Manager-Interface-(Rest-API)/NET-Implementation-of-Protocol/MT5WebAPI-Class/Custom-Commands/CustomSend.md) methods respectively.

### The Order of Reading Input Data

To read input data from indata methods, the WebRead* methods of the [IMTByteStream](../../Database-Interfaces/Byte-Stream/IMTByteStream.md) interface are used. Methods should be called in the order that corresponds to the format of Web API commands:

  * Reading a command — the [IMTByteStream::WebReadCommand](../../Database-Interfaces/Byte-Stream/IMTByteStream/WebReadCommand.md) method.
  * Reading the parameter name — [IMTByteStream::WebReadParamName](../../Database-Interfaces/Byte-Stream/IMTByteStream/WebReadParamName.md).
  * Reading the parameter value — one of the [IMTByteStream::WebReadParam*](../../Database-Interfaces/Byte-Stream/IMTByteStream/WebReadParamStr.md) methods, which corresponds to the value type.
  * Then the name and value of each of the remaining parameters is read one by one using the methods described above. After all parameters are read, in response to the IMTByteStream::WebReadParamName method, the server returns the [MT_RET_ERR _NOTFOUND](../../Return-Codes/Common-errors.md) response code.
  * To read the additional body of commands, common reading methods [IMTByteStream::Read*](../../Database-Interfaces/Byte-Stream/IMTByteStream/Read.md) are used.



> When calling the [IMTByteStream::ReadReset](../../Database-Interfaces/Byte-Stream/IMTByteStream/ReadReset.md) method, command reading should be started in the order described above.

An Example of Data Reading:
    
    
    MTAPISTR       cmd={0},name={0},myparam1={0};
       MTAPISTR       retcode;
    //--- Check if this is our command
       if(CMTStr::CompareNoCase(command,L"MYCOMMAND")!=0) return(MT_RET_OK_NONE);
    //--- Necessarily read the command
    //--- It will match what was passed in command
       if(indata->WebReadCommand(cmd)!=MT_RET_OK)
         {
          //--- Error
          return(MT_RET_ERR_DATA);
         }
    //--- Read parameters
       while((retcode=indata->WebReadParamName(name))==MT_RET_OK)
         {
          //--- Is this MYPARAM1?
          if(CMTStr::CompareNoCase(name,L"MYPARAM1")==0)
            {
             //--- Get the value
             if(indata->WebReadParamStr(myparam1)!=MT_RET_OK)
               {
                //--- Error
                return(MT_RET_ERR_DATA);
               }
            }
          //--- We don't know other parameters, skip them
          if(indata->WebReadParamSkip()!=MT_RET_OK)
            {
             //--- Error
             return(MT_RET_ERR_DATA);
            }
         }
    //--- Are parameters over or is there any error?
       if(retcode!=MT_RET_ERR_NOTFOUND)
         {
          //--- Error
          return(MT_RET_ERR_DATA);
         }

### The Order of Generation of Output Data

When forming output data (outdata), it should be taken into account that the server automatically generates the necessary part of the response command:
    
    
    Received command|RETCODE=Response code of the hook|

  * The remaining parameters must be formed by using the [IMTByteStream::WebAddParam*](../../Database-Interfaces/Byte-Stream/IMTByteStream/WebAddParamStr.md) methods.
  * To complete work with parameters, call the [IMTByteStream::WebAddParamFinalize](../../Database-Interfaces/Byte-Stream/IMTByteStream/WebAddParamFinalize.md) method. In fact, it adds the line break character \r\n, which means the end of the main body of a command.
  * Next, using the [IMTByteStream::Add*](../../Database-Interfaces/Byte-Stream/IMTByteStream/Add.md) methods you can create an additional body of a command.



An Example of Data Forming:
    
    
    //--- Add our own output parameter
       if(outdata->WebAddParamStr(L"MYRESULT",L"HELLO WORLD!!!")!=MT_RET_OK)
         {
          //--- Error
          return(MT_RET_ERROR);
         }
    //--- Finalize parameters
       if(outdata->WebAddParamFinalize()!=MT_RET_OK)
         {
          //--- Error
          return(MT_RET_ERROR);
         }
    //--- A structure with our additional parameters
       MyData data={0};
    //--- Add as an additional body
       if(outdata->Add(&data,sizeof(data))!=MT_RET_OK)
         {
          //--- Error
          return(MT_RET_ERROR);
         }

### Reserved Names of Commands

There are special names reserved for use in the trading platform. These names cannot be used for custom commands:

  * AUTH_*
  * USER_*
  * TRADE_*
  * TIME_*
  * GROUP_*
  * ORDER_*
  * POSITION_*
  * DEAL_*
  * HISTORY_*
  * TICK_*
  * MAIL_*
  * NEWS_*
  * COMMON_*
  * QUIT*
  * TEST_TRADE
  * TEST_ACCESS



> When extending the Web API protocol, it is recommended that you use command names that will not intersect with the commands implemented on the side of MetaTrader 5 servers or any other third-party plugins. For example, you can use the company name in the command name: MYCOMPANY_MYCOMMAND.
