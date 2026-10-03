[🏠 Document Start](../README.md) / [Manager API](README.md) / Recommendations for Developers

[Previous](Purpose-of.md) | [Next](Getting-Started.md)

<a id="recommendations-for-developers"></a>
# Recommendations for Developers (#recommendations-for-developers)

This section contains general recommendations and solutions of typical issues programmers face when developing applications via Manager API.

<a id="principles-of-applications"></a>
## Principles of Applications (#principles-of-applications)

In the work of applications, there are the following main steps:

  * Loading MT5APIManager.dll using the [CMTManagerAPIFactory::Initialize](CMTManagerAPIFactory/Initialize.md) method of he Manager API factory.
  * Creating the manager or administrator interface using the [CMTManagerAPIFactory::CreateManager](CMTManagerAPIFactory/CreateManager.md) or [CMTManagerAPIFactory::CreateAdmin](CMTManagerAPIFactory/CreateAdmin.md) method respectively.
  * Verifying that the versions of the main header file MT5APIManager.h (the version parameter of one of the interface creation methods) and of the loaded DLL (passed by [CMTManagerAPIFactory::Version](CMTManagerAPIFactory/Version.md)) match.
  * Connecting an application to a server with the Connect method, using the created [administrator](Administrator-Interface/Connection-to-the-Server/Connect.md) or [manager](Manager-Interface/Connection-to-the-Server/Connect.md) interface, as well as details of the manager account created on the server.
  * After the work is completed, the application is disconnected from the server using the Disconnect method.
  * Next the created interface is deleted using the Release method.
  * The last stage is unloading the DLL of the manager API from the memory using the [CMTManagerAPIFactory::Shutdown](CMTManagerAPIFactory/Shutdown.md) method.



  * With the MetaTrader 5 Manager API, you can develop 32- and 64-bit applications using the appropriate DLLs included into the installation package.


  * Applications are only developed for Windows. Manager API DLLs are not suitable for developing applications for Linux or other operating systems.

  
---  
  
<a id="application-requirements"></a>
## Application Requirements (#application-requirements)

When developing applications, it is necessary to meet the following requirements:

  * An application should be as efficient in memory usage as possible.
  * An application should fragment memory as little as possible.
  * An application should not cause memory leaks.
  * An application must quickly return control from event handlers.
  * During calls of any *Request methods (such as [IMTManagerAPI::SymbolRequest](Manager-Interface/Configuration-Databases/Symbols/SymbolRequest.md) or [IMTManager::GroupRequest](Manager-Interface/Configuration-Databases/Groups/GroupRequest.md)), information is requested straight from the server. Too frequent requests can lead to the activation of the anti flood control system, as a result of which connection between the Manager API and the server can be lost. In order not to overload the server, control the frequency of these method calls and, if possible, use *Get methods, which receive information from the local application cache.
  * All methods of event handling interfaces (IMT*Sink) are called from the network thread. Therefore, any methods of the same manager or administrator interface, which send commands to the trade server (such as *Request, *Update, *Delete, *Send, etc.) are prohibited in these interfaces. Only methods working with local data (*Get, *Next, *Total, etc.) can be called from event handlers.



<a id="base"></a>
## Working with the configuration base and database interfaces (#base)

When working with [configuration base](../Configuration-Interfaces/README.md) and [database](../Database-Interfaces/README.md) interfaces, please consider the following features:

  * Any *Add, *Update, *Delete and *Clear methods of these interfaces only affect the appropriate local object. To send changes to a server, you should call the corresponding *Add or *Update method of the Manager API. For example, the [IMTConGroup::SymbolUpdate](../Configuration-Interfaces/Groups/IMTConGroup/SymbolUpdate.md) method only updates a symbol configuration in the group object. To send these changes to a server, you should call the [IMTAdminAPI::GroupUpdate](Administrator-Interface/Configuration-Databases/Groups/GroupUpdate.md) method.



<a id="escape"></a>
## Escaping special characters (#escape)

When using special characters = (equal sign), | (vertical bar), \ (slash) and line feed as method parameter values, you must escape them with the \ (slash) character.

> If the \ (slash) character is not followed by special characters listed above, then it is processed as is.

The table below shows examples of processing escaped characters on a trading server.

Character sent to the server | character recognized by the server  
---|---  
\= | =  
\| | |  
\(line feed) | (line feed)  
\\\ | \  
  
<a id="journal"></a>
## Using Logs to Analyze Possible Problems (#journal)

Logs assist in tracking application events and errors. Use Logger* functions available in the [Administrator](Administrator-Interface/Common-Functions/LoggerOut.md) and [Manager interfaces](Manager-Interface/Common-Functions/LoggerOut.md) in crucial blocks of your application code to log information about its operation. This will make troubleshooting much easier.

By default, Manager API applications store logs under the \logs subdirectory of the directory from which they are launched. For example, if your application runs in the 'C:\ManagerAPI solution' directory, then the log will be located in 'C:\ManagerAPI solution\logs'. The files have .log extensions and are saved separately for each day. The data storage directory can be overridden when creating interfaces using the [CreateAdmin](CMTManagerAPIFactory/CreateAdmin.md) and [CreateManager](CMTManagerAPIFactory/CreateManager.md) methods.
