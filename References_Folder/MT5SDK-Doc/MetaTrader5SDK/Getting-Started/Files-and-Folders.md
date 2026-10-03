[🏠 Document Start](../README.md) / [Getting Started](../Getting-Started.md) / Files and Folders

[Previous](Setup.md) | [Next](Delete.md)

<a id="files-and-folders"></a>
# Files and Folders (#files-and-folders)

The [installation](Setup.md) directory contains the following files and folders:

  * \Docs — documentation CHM files.
  * \Examples — examples for each API type.
  * \Include — header files for each API type.
  * \Libs — [Manager API](../Manager-API/README.md) and [Gateway API](../Gateway-API/README.md) DLLs, including .NET versions
  * unins000.* — MetaTrader 5 API uninstall program files.



<a id="exmaples"></a>
## Examples (#exmaples)

The folder contains examples for API.

Folders | Description  
---|---  
Gateway | [Examples for Gateway API](../Gateway-API/Development-and-Debugging-of-Gateways.md).  
Manager | [Examples for Manager API](../Manager-API/Ready-made-Examples.md).  
Report | [Examples for Report API](../Report-API/Ready-made-Examples.md).  
Server | [Examples for Server API](../Server-API/Ready-made-Examples.md).  
Web | Web API implementation examples in [PHP](../Web-API/Manager-Interface-(Rest-API)/PHP-Implementation-of-Protocol.md) and [.NET](../Web-API/Manager-Interface-(Rest-API)/NET-Implementation-of-Protocol.md).  
  
<a id="include"></a>
## Include (#include)

This file contains header files for all APIs, as well as common header files.

Folders and files | Description | Files  
Bases | Descriptions of interfaces of common databases. | 

  * MT5APIAccount.h — [trading account state](../Database-Interfaces/Trade/Accounts/IMTAccount.md) description.
  * MT5Attachment.h — [attachment](../Database-Interfaces/Clients/IMTAttachment.md) description.
  * MT5APIBook.h — [Market Depth](../Structures/MTBookMTBookDiff.md) description.
  * MT5APIByteStream.h — [byte stream](../Database-Interfaces/Byte-Stream/IMTByteStream.md) description.
  * MT5APICertificate — [certificate](../Database-Interfaces/Certificates/IMTCertificate.md) description.
  * MT5APIChart — [chart bar](../Structures/MTChartBar.md) description.
  * MT5APIClient.h — [client](../Database-Interfaces/Clients/IMTClient.md) description.
  * MT5APIComment.h — [comment](../Database-Interfaces/Clients/IMTComment.md) description.
  * MT5APIConfirm.h — [trade request confirmation](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTConfirm.md) description.
  * MT5APIDaily.h — [daily report description](../Database-Interfaces/Trade/Daily-Reports/IMTDaily.md).
  * MT5APIDataset.h — [data set](../Report-API/Dataset-Interfaces/IMTDataset.md) description.
  * MT5APIDeal.h — [trade deal](../Database-Interfaces/Trade/Deals/IMTDeal.md) description.
  * MT5APIDocument.h — [client document](../Database-Interfaces/Clients/IMTDocument.md) description.
  * MT5APIExecution.h — [trade execution](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTExecution.md) description.
  * MT5APIExposure.h — [exposure](../Database-Interfaces/Trade/Assets/IMTExposure.md) description.
  * MT5APIMail.h — [mail database](../Database-Interfaces/Mail-Database/IMTMail.md) description.
  * MT5APINews.h — [news database](../Database-Interfaces/News-Database/IMTNews.md) description.
  * MT5APIOnline.h — description of [online users](../Database-Interfaces/Online-Connections/IMTOnline.md).
  * MT5APIOrder.h — [trade order](../Database-Interfaces/Trade/Orders/IMTOrder.md) description.
  * MT5APIPosition.h — [trade position](../Database-Interfaces/Trade/Positions/IMTPosition.md) description.
  * MT5APIRequest.h — [trade request](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) description.
  * MT5APISummary.h — [summary position](../Database-Interfaces/Trade/Summary-Positions/IMTSummary.md) description.
  * MT5APITick.h — [price data](../Structures/MTTick.md) description.
  * MT5APIUser.h — [account](../Database-Interfaces/Users/IMTUser.md) description.

  
Config | Description of the configuration interfaces. | 

  * MT5APIConfigCommon.h — [common settings](../Configuration-Interfaces/Common/IMTCon.md).
  * MT5APIConfigEmail.h — [mail server](../Configuration-Interfaces/Mail-Servers/IMTConEmail.md) settings.
  * MT5APIConfigFeeder.h — [data feed](../Configuration-Interfaces/Data-Feeds/IMTConFeeder.md) settings.
  * MT5APIConfigFirewall.h — [firewall](../Configuration-Interfaces/Firewall/IMTCon.md) settings.
  * MT5APIConfigFund.h — fund settings.
  * MT5APIConfigGateway.h — [gateway](../Configuration-Interfaces/Gateways/IMTConGateway.md) settings.
  * MT5APIConfigGroup.h — [group](../Configuration-Interfaces/Groups/IMTConGroup.md) settings.
  * MT5APIConfigHistory.h — [historical data synchronization](../Configuration-Interfaces/History-Synchronization/IMTConHistorySync.md) settings.
  * MT5APIConfigHoliday.h — [holiday](../Configuration-Interfaces/Holidays/IMTConHoliday.md) settings.
  * MT5APIConfigManager.h — [manager](../Configuration-Interfaces/Managers/IMTConManager.md) settings.
  * MT5APIConfigMessenger.h — [instant messenger](../Configuration-Interfaces/Messengers/IMTConMessenger.md) settings.
  * MT5APINetwork.h — settings of [platform components](../Configuration-Interfaces/Network/IMTConServer.md).
  * MT5APIConfigParam.h — settings of [parameters of different configurations](../Configuration-Interfaces/Additional-Parameters/IMTConParam.md) (for example, in data feeds, plugins, etc.).
  * MT5APIConfigPlugin.h — [plugin](../Configuration-Interfaces/Plugins/IMTConPlugin.md) settings.
  * MT5APIConfigReport — [report](../Configuration-Interfaces/Reports/IMTConReport.md) settings.
  * MT5APIConfigRoute.h — [routing](../Configuration-Interfaces/Routing/IMTConRoute.md) settings.
  * MT5APIConfigSpread.h — [spread](../Configuration-Interfaces/Spreads/IMTConSpread.md) settings.
  * MT5APIConfigSymbol.h — [symbol](../Configuration-Interfaces/Symbols/IMTConSymbol.md) settings.
  * MT5APIConfigTime.h — [time](../Configuration-Interfaces/Time/IMTCon.md) settings.

  
Classes | Classes of auxiliary functions. | 

  * MT5APIFile.h — functions for [operations with files](../Tools/CMTFile.md).
  * MT5APIFormat.h — [string formatting](../Tools/SMTFormat.md) functions.
  * MT5APIMath.h — [mathematical transformation](../Tools/SMTMath.md) functions.
  * MT5APIMemPack.h — functions for memory operation.
  * MT5APIProcess.h — functions for operations with processes.
  * MT5APISearch.h — [sort and search](../Tools/SMTSearch.md) functions.
  * MT5APIStorage.h — dynamic array class.
  * MT5APIStr.h — [string](../Tools/CMTStr.md) class.
  * MT5APISync.h — class for [critical synchronization between threads](../Tools/CMTSync.md).
  * MT5APIThread.h — [thread control](../Tools/CMTThread.md) functions.
  * MT5APITime.h — [time conversion](../Tools/SMTTime.md) functions.

  
MT5APIConstants.h | Common constants, such as error codes, etc.  
MT5APIGateway.h | The main header file of [Gateway API](../Gateway-API/Main-Interface.md).  
MT5APILogger.h | Constants and types used for the journal.  
MT5APIManager.h | The main header file of [Manager API](../Manager-API/README.md).  
MT5APIPublicKey.h | Public key for signing data.  
MT5APIReport.h | The main header file of [Report API](../Report-API/Main-Interface-of-Reports.md).  
MT5APIServer.h | The main header file of [Server API](../Server-API/Main-API-Interface.md).  
MT5APITools.h | Description of auxiliary functions and constants.  
MT5APITypes.h | Description of internal data types.  
  
<a id="libs"></a>
# Libs (#libs)

This folder contains Manager API and Gateway API DLLs, including .NET versions.

Folders | Description  
---|---  
MetaQuotes.MT5CommonAPI.dll | 32-bit DLL of common functions for the [Manager API](../Manager-API/NET-Implementation.md) and [Gateway API](../Gateway-API/NET-Implementation.md) .NET wrapper.  
MetaQuotes.MT5CommonAPI64.dll | 64-bit DLL of common functions for the [Manager API](../Manager-API/NET-Implementation.md) and [Gateway API](../Gateway-API/NET-Implementation.md) .NET wrapper.  
MetaQuotes.MT5GatewayAPI.dll | 32-bit DLL of [Gateway API](../Gateway-API/NET-Implementation.md) .NET version.  
MetaQuotes.MT5GatewayAPI64.dll | 64-bit DLL of [Gateway API](../Gateway-API/NET-Implementation.md) .NET version.  
MetaQuotes.MT5ManagerAPI.dll | 32-bit DLL of [Manager API](../Manager-API/NET-Implementation.md) .NET version.  
MetaQuotes.MT5ManagerAPI64.dll | 64-bit DLL of [Manager API](../Manager-API/NET-Implementation.md) .NET version.  
MetaQuotes.MT5WebAPI.dll | DLL of [Web API](../Web-API/Manager-Interface-(Rest-API)/NET-Implementation-of-Protocol.md) .NET implementation for 32 and 64 bit projects.  
MT5APIGateway.dll | 32-bit [Gateway API](../Gateway-API/README.md) DLL.  
MT5APIGateway64.dll | 64-bit [Gateway API](../Gateway-API/README.md) DLL.  
MT5APIManager.dll | 32-bit [Manager API](../Manager-API/README.md) DLL.  
MT5APIManager64.dll | 64-bit [Manager API](../Manager-API/README.md) DLL.
