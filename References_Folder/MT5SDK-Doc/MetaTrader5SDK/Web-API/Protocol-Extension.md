[🏠 Document Start](../README.md) / [Web API](README.md) / Protocol Extension

[Previous](Maintaining-Connections.md) | [Next](Examples.md)

# Protocol Extension

The MetaTrader 5 API protocol is extensible. In addition to standard [commands of manager connection](Manager-Interface-(Rest-API).md), a Web client can send any other text commands to a server. However, handling of such commands must be implemented on the server side.

Custom Web API commands can be handled using a server plugin created with the MetaTrader 5 Server API. For this purpose, the Server API provides a special hook [IMTCustomSink::HookWebAPICommand](../Server-API/Interface-of-Custom-Events/HookWebAPICommand.md).

Consider an example of sending a custom command:
    
    
    POST /echo
    {
      text: Request/Reply request,
      seq: 1
    }

The command can be handled on the plugin side as follows:
    
    
    MTAPISTR       cmd={},request{};
    MTAPIRES       retcode;
    //--- Check that this is our command
    if(CMTStr::CompareNoCase(command,L"ECHO")!=0)
       return(MT_RET_OK_NONE);
    //--- Check the content
    if(indata->WebReadCommand(cmd)!=MT_RET_OK)
      {
      //--- Error
       return(MT_RET_ERR_DATA);
      }
    //--- Read the request
    retcode=indata->ReadStr(request);
    if(retcode!=MT_RET_OK)
      {
      //--- Error
       return(MT_RET_ERR_DATA);
      }
    //--- Processing a custom command with custom parameters
    if(CMTStr::Compare(request,L"{text: Request/Reply request, seq: 1 }")!=0)
      {
      //--- Error
       return(MT_RET_ERR_DATA);
      }
    //--- Send a response
    retcode=outdata->AddStr(L"{text: Request/Reply reply, seq: 1}");
    if(retcode!=MT_RET_OK)
      {
      //--- Error
       return(retcode);
      }
    //--- Success
    return(MT_RET_OK);

The command will return the following in response to the command:
    
    
    {
      "retcode" : "0 Done",
      "answer" : {text: Request/Reply reply, seq: 1}
    }

Further details about the handling of custom commands is available under the [IMTCustomSink::HookWebAPICommand](../Server-API/Interface-of-Custom-Events/HookWebAPICommand.md) section.

## Reserved Names of Commands

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



> When extending the protocol, it is recommended that you use command names that will not intersect with the commands implemented on the side of MetaTrader 5 servers or any other third-party plugins. For example, you can use the company name in the command name: MYCOMPANY_MYCOMMAND.
