[🏠 Document Start](../README.md) / [Gateway API](README.md) / Development of Data Feeds

[Previous](Symbol-and-Price-Translation.md) | [Next](NET-Implementation.md)

<a id="developing-data-feeds"></a>
# Developing Data Feeds (#developing-data-feeds)

Creating the new MetaTrader 5 platform, we've done our best to facilitate integration with gateways and data feeds. For this purpose, we've developed MetaTrader 5 Gateway API - a special library for developers.

In this library, we've hidden all technical details of interaction with the trading platform and have provided an opportunity to manage integration using simple methods. Now, developer's code does not depend on the internal changes and is always operable.

The library is developed for working at win32 and x64 platforms and is included into the MetaTrader 5 distributive. Using MetaTrader 5 Gateway API, developers can implement their own trade gateways, as well as data feeds.

This section describes an example of writing a simple data feed for the MetaTrader 5 platform in C++.

<a id="how-do-data-feeds-work-in-metatrader-5"></a>
## How do Data Feeds work in MetaTrader 5? (#how-do-data-feeds-work-in-metatrader-5)

The main objective of a Data Feed is to receive quotes and news from external providers and transform these data into MetaTrader 5 format.

![How do Data Feeds work in MetaTrader 5?](images/datafeed_scheme.png)

Exchanging news and quotes data with MetaTrader 5 trading platform is done entirely via MetaTrader 5 History Server. Data Feed is a medium between History Server and external data source.

Each Data Feed is implemented as a standalone application, so the failure in its work does not affect the work of the platform. All Data Feeds processes are reentrant. You can run one Data Feed application several times, and each time new data source is provided.

Communicating with History Server is implemented via encrypted network connection. Using a network connection to communicate with History Server allows the trading platform to use Data Feeds that work on remote network computers. Data Feed application provides server port for connection, while the History Server creates client connection to the server port of Data Feed.

If the Data Feed executable file is stored in the 'datafeed' sub-folder of History Server, then application Start and Stop is done by History Server. When working remotely, Data Feed is a service that accepts and handles incoming connections from History Servers. To each Data Feed you can connect several servers.

<a id="metatrader-5-gateway-api-description"></a>
## MetaTrader 5 Gateway API Description (#metatrader-5-gateway-api-description)

The main task for a developer is to transfer all the data, obtained in the MetaTrader 5 Gateway API. For application programmers we can compose the following algorithm to work with this API:

  * Initialization. At this stage, developer has to load the library.
  * Obtaining and running server port interface. All interaction with API is done via server port interface. This interface contains methods of data management and sending. When you create a user interface API, developer must specify his own notification handler. Using this handler API will notify the developer about new connections of History Servers and their parameters (quotes symbols, operation mode, additional parameters). This information only notifies a user and its use is optional.
  * Sending data. Server port interface contains all the necessary methods for sending data to connected History Servers.
  * Exiting. At this stage, a developer has to release server port interface and unload the library.



MetaTrader 5 Gateway API is described in a single 'MT5APIGateway.h' file and implemented in the 'MT5APIGateway.dll' and 'MT5APIGateway64.dll' files for win32 and x64 platforms, respectively. For an application that uses API, it is necessary that these files must be available. Simply copy them into the application folder.

The library exports a few simple functions:

  * [MTGatewayVersion](Exported-Functions/MTGatewayVersion.md) \- returns the version of the Gateway API.
  * [MTGatewayCreateLocal](Exported-Functions/MTGatewayCreateLocal.md) \- creates and returns an instance of the gateway interface taking into account its description and parameters passed in the command line. In the command line from History Server passed are the time zone and the server port number, on which interface must be started as a server accepting incoming connections. Command line is also used to obtain Data Feed description. By passing command line parameters to the library, we've freed developers from parsing line parameters, time zone initialization and Data Feed description formatting. This method is used only by Data Feeds, controlled by History Server.
  * [MTGatewayCreate](Exported-Functions/MTGatewayCreate.md) \- creates and returns an instance of gateway interface.



When creating a gateway interface, we need to pass to it a correctly filled out [MTGatewayInfo](../Structures/MTGatewayInfo.md) structure. This structure contains the description of a data feed and its default settings.

<a id=""></a>
##  (#)

<a id="metatrader-5-gateway-api-description"></a>
## MetaTrader 5 Gateway API Description (#metatrader-5-gateway-api-description)

The major task of a developer is to transmit quoting data for the MetaTrader 5 Gateway API. From the point of view of an application programmer, the following algorithm for working with this API can be used:

  * Initialization. At this stage, the developer loads the library.
  * Get and run the gateway interface. All interaction with the API is done through the gateway's abstract interface. To enable the creation of data feeds, this interface provides methods for managing and sending quoting data. When creating an interface, an API developer should specify their own event handler. Through this handler, the API will notify the developer about new server connections and their parameters (for data feeds, these are quoted symbols, operation mode, and additional parameters). This information is optional and thus you may choose not to use it.
  * Send data. The gateway interface provides all the necessary methods for sending quoting data to all connected History servers.
  * Complete operations. At this stage, the developer releases the gateway interface and unloads the library.



MetaTrader 5 Gateway API is described in one file, 'MT5APIGateway.h', and it is implemented in files 'MT5APIGateway.dll' and 'MT5APIGateway64.dll', for win32 and x64 platforms respectively. Please make sure that these files are available, otherwise the application using the API will not work. To make the files available, simply copy them to the application directory.

The library exports a few simple functions:

  * [MTGatewayVersion](Exported-Functions/MTGatewayVersion.md) \- returns the Gateway API version.
  * [MTGatewayCreateLocal](Exported-Functions/MTGatewayCreateLocal.md) \- creates and returns an instance of the gateway interface, taking into account its description, with the parameters passed on the command line. The following parameters are passed on the command line from the History Server: time zone values and the port number on which the gateway interface will start running as a server that accepts incoming connections. The command line is also used to get the data feed description. By passing the command-line arguments to the library, we eliminate the need for the developer to parse the string parameters, to initialize the time zone and to generate the data feed description. This method is only used by the data feeds managed by the History server.
  * [MTGatewayCreate](Exported-Functions/MTGatewayCreate.md) \- creates and returns an instance of the gateway interface.



When creating a gateway interface, it must be passed a correctly filled [MTGatewayInfo](../Structures/MTGatewayInfo.md) structure. This structure contains the data feed description and its default settings.

<a id="representation"></a>
## Data feed presentation to users: logo and description (#representation)

MetaTrader 5 supports the loading of the data feed logo and description from resources. Use this option to present your product in the [data feed showcase in MetaTrader 5 Administrator](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_feeds), as well as to provide documentation on the spot.

![Data feed presentation in MetaTrader 5 Administrator](images/datafeed_showcase.png)

Add resources with the "DESCRIPTION" type and with the following IDs to your project:

  * 1000 — module description in free form, in UTF-8 format. Use an HTML document without classes and style, only with simple tags: h3, p, ul, ol, b, i. Standard Administrator terminal styles will be applied to the description and it will naturally fit into the interface.
  * 1001 — square logo for the showcase.
  * 1002 — square logo for high-resolution monitors.
  * 1003 — rectangle logo for the list of data feeds and the details page.
  * 1004 — rectangle logo for high-resolution monitors.



An example of a .RC project file block:
    
    
    1000 DESCRIPTION "res\\description.html"
    1001 DESCRIPTION "res\\200x200.png"
    1002 DESCRIPTION "res\\400x400.png"
    1003 DESCRIPTION "res\\360x100.png"
    1004 DESCRIPTION "res\\720x200.png"

When loading the data feed module, the history server will pass this data to the main server, from which the information will be displayed in MetaTrader 5 Administrator.

<a id="imtgatewayapi-interface"></a>
## IMTGatewayAPI Interface (#imtgatewayapi-interface)

The main interaction with API is done via [IMTGatewayAPI](Main-Interface.md) interface. Access to this interface is gained using functions exported by the library. To make it more simple, in 'MT5APIGateway.h' file there is implemented interface factory, which automatically loads correct 32 or 64 bit library and provides access to the exported functions. Example of creating server interface via factory:
    
    
    //+------------------------------------------------------------------+
    //| Example of gateway interface creation                            |
    //| using the interface factory                                      |
    //+------------------------------------------------------------------+
    int wmain(int argc,wchar_t** argv)
      {
       CMTGatewayAPIFactory  apifactory;
       IMTGatewayAPI        *gateway=NULL;
       MTGatewayInfo         info;
    //--- library initialization
       if(apifactory.Initialize()!=MT_RET_OK)
          return(-1);
    //--- generation of gateway description
       Info(info);
    //--- server interface creation
       if(apifactory.Create(info,&gateway,argc,argv)!=MT_RET_OK)
          return(-1);
     
    //---
    //--- use the gateway interface to send quoting data to a History Server
    //---
     
    //--- free the server interface
       server->Release();
    //--- shutting down the interface factory
       apifactory.Shutdown();
    //--- Successful
       return(0);
      }

The entire [IMTGatewayAPI](Main-Interface.md) interface is absolutely thread-safe - you can call methods of this interface any time from any thread of executed commands. All IMTGatewayAPI interface methods can be divided into methods of management and methods of sending price data to History Servers.

Let's consider methods of gateway management:

  * [Start](Main-Interface/Server/Start.md) \- start receiving incoming connections to the gateway by IP address and port specified in the 'address' parameter. The gateway will notify users by calling virtual methods of IMTGatewaySink interface. Developers can override notification methods with their own by implementing class, inherited from IMTGatewaySink. More detailed description of IMTGatewaySink interface is below.
  * [Stop](Main-Interface/Server/Stop.md) \- stop receiving incoming connections by the gateway.
  * [Release](Main-Interface/Common-Functions/Release.md) \- releasing gateway interface. After calling this method gateway object is destroyed, and the pointer to gateway interface becomes unavailable. Do not release interface by calling 'delete', because with this call API will not know about interface deletion. Interface should always be released using Release() method.
  * [ClientAdd](Main-Interface/Client-Connection/ClientAdd.md) \- using this method developer specifies allowed authentication data (login and password) for incoming connections. You can add multiple logins and passwords.
  * [ClientAllowIP](Main-Interface/Client-Connection/ClientAllowIP.md) \- adding IP addresses, from which incoming connection is allowed. If no addresses are added, then incoming connections are allowed from all addresses. You can add multiple addresses. You can add multiple addresses.
  * [ServerIP](Main-Interface/Server/IP.md) \- getting IP address, on which incoming connections are listened and received.
  * [ServerPort](Main-Interface/Server/Port.md) \- as a return value, the method passes the port number that is running and listening to incoming connections.
  * [ServerConnections](Main-Interface/Server/Connections.md) \- as a return value, the method passes the number of authorized and working incoming connections at the time of call.



Example of gateway management:
    
    
    //--- ...
    //--- add data to authorize gateway incoming connections
       if(gateway->ClientAdd(123,L"Password")!=MT_RET_OK)
         {
          //--- release the interface and exit
          gateway->Release();
          return(-1);
         }
    //--- add IP from which incoming connection to the gateway is allowed
       if(gateway->ClientAllowIP(L"192.168.0.2")!=MT_RET_OK)
         {
          //--- release the interface and exit
          gateway->Release();
          return(-1);
         }
    //--- start receiving incoming connections, address of the gateway - 192.168.0.1, port - 16384
       if(gateway->Start(&client,L"192.168.0.1:16384")!=MT_RET_OK)
         {
          //--- release the interface and exit
          gateway->Release();
          return(-1);
         }
    //--- wait till ESC pressing
       while(_getwch()!=27)
         {
     
          //---
          //--- here we can receive and send quotes and news
          //---
     
          //--- delay
          Sleep(100);
         }
    //--- gateway stopping
       gateway->Stop();
    //--- //--- 
       gateway->Release();
    //--- ....

Let's consider methods of sending data to History Servers.

There are 4 methods of transferring data in server port interface. All these methods work asynchronously. This means that the managing will return to the developer's code immediately after placing data to the API buffer for sending. Let's consider these methods in details:

  * [SendTickStats](Main-Interface/Quote-and-News-Feeds/SendTickStats.md) \- sending ticks statistics. This method accepts array of [MTTickStat](../Structures/MTTickStat.md) structures, counting 'stats_total' elements.
  * [SendTicks](Main-Interface/Quote-and-News-Feeds/SendTicks.md) \- sending ticks. This method accepts array of [MTTick](../Structures/MTTick.md) structures, counting 'ticks_total' elements. 
  * [SendBookDiffs](Main-Interface/Quote-and-News-Feeds/SendBookDiffs.md) \- sending changes in depth of market. This method accepts array of [MTBookDiff](../Structures/MTBookMTBookDiff.md) structures, counting 'bookdiffs_total' elements. MTBookDiff structure has a special feature, that contains an array of [MTBookItem](../Structures/MTBookItem.md) structures, and the number of structures is indicated in the 'items_total' value. These elements describe the change in depth of market.
  * [SendNews](Main-Interface/Quote-and-News-Feeds/SendNews.md) \- sending news. This method accepts array of [MTNews](../Structures/MTNews.md) structures, counting 'news_total' elements.
  * [LoggerOut](Main-Interface/Common-Functions/LoggerOut.md) \- adding entry into the API journal. For your convenience, API has its own journal. All technical details of working with journal - journal filename correct formation, journal file size controlling, receiving latest journal entries by request from History Server, etc. - are hidden from developers Example of using journal methods:


    
    
    gateway->LoggerOut(MTLogErr,L"last error(%d)",GetLastError());

<a id="filling-mtbookdiff-structure"></a>
### Filling MTBookDiff Structure (#filling-mtbookdiff-structure)

Each element of the aggregated depth of market is unique in type and price. The [MTBookDiff](../Structures/MTBookMTBookDiff.md) structure contains information about volume changes for a given type and price in the form of an array of MTBookItem [MTBookItem](../Structures/MTBookItem.md) elements. One MTBookDiff structure contains changes only for one instrument, described in the 'symbol' value of the structure.

Here are depth of market elements' change types and History Server actions, when receiving this types of elements to form an aggregated depth of market:

  * ItemReset - on receiving element with this type History Server will clean the aggregated depth of market for a given symbol.
  * ItemSell, ItemBuy - on receiving MTBookItem structure with this type, History Server will look for aggregated depth of market's element by type and price, given in MTBookItem. If the element is not found, then a new element (of MTBookItem type and price) is added to the aggregated depth of market. If the element is found in the aggregated depth of market, then element volume changes by the volume value, specified in the MTBookItem structure. If zero volume is indicated in the MTBookItem structure, then element, found in the aggregated depth of market, is deleted.



The volume of element change in the aggregated depth of market, described in MTBookItem, can be both positive and negative.

<a id="filling-mtnews-structure"></a>
### Filling MTNews Structure (#filling-mtnews-structure)

The 'language' field must contain news language identifier from the Windows Languages Identifier table. This field specifies the language of news, and is used when sending news to Client Terminals, in which only certain languages are selected.

News category is used for news filtration. String, separated by the '\' symbol, can be passed as a value of this parameter. Separator is used to define subcategories and allows you to build a tree of available news categories. This allows you to filter news in Client Terminal. Category example: "DJ Newswires\PrimeTass\Real-Time news".

[MTNews](../Structures/MTNews.md) structure is special, as it contains a pointer to dynamically allocated buffer for the news body. The length of news body is indicated in the 'body_len' field (in characters). Thus, to send the news body, a developer needs to create a memory buffer of desired size and copy the news body into it. Pointer to the buffer and buffer size in characters must be copied into the 'body' and 'body_len' field, respectively. After calling the method of sending news, you need to remove previously created buffer for news body in order to prevent memory leaks.

To send high priority news you should set the FLAG_PRIORITY flag in the 'flags' field.

<a id="imtgatewaysink-interface"></a>
## IMTGatewaySink Interface (#imtgatewaysink-interface)

[IMTGatewaySink](Event-Interface.md) interface is described in the 'MT5APIGateway.h' file and is used to organize API feedback from the developer's program In case of certain event, API calls the appropriate method of the IMTGatewaySink interface. All methods of this interface are virtual. This means that developers can create a class, inherited from IMTGatewaySink, and implement its own logic in these method, if needed.

In practice, class, inherited from IMTGatewaySink, is needed only when implementing Data Feed, managed by History Server. If Data Feed is implemented in the form of independent remote service, developers don't need feedback from API This means that there's no need to create a class, inherited from IMTGatewaySink. You can immediately use the IMTGatewaySink implementation from the 'MT5APIGateway.h' file.

All IMTGatewaySink methods calls are produced sequentially in time, in one of threads of commands handling pool. So the code in the overridden IMTClient methods must be thread-safe.

Let's consider IMTGatewaySink methods in details:

  * [HookServerConnect](Event-Interface/HookServerConnect.md) \- this call is made from API as a result of receiving of incoming connection. The address from which the connection is performed, type of the MetaTrader server that is connecting (History Server or Trade Server) and the server login is passed to the interface. This method can be used to restrict external connections by address and login.
  * [OnServerDisconnect](Event-Interface/OnServerDisconnect.md) \- notice about closing the connection. The method parameters coincide with the parameters passed in HookServerConnect.
  * [OnGatewayShutdown](Event-Interface/OnGatewayShutdown.md) \- notice about shutting down the server with the given login. If there are no external connections, API calls this method every 2 minutes with login 0. This is done in order to stop Data Feed, if there are no connections to History Server for a long time. Similarly to OnConfig(), you can skip overriding this method, if Data Feed works as an independent remote service. If Data Feed is controlled by History Server, then application must be shut down on this call.
  * [OnGatewayConfig](Event-Interface/OnGatewayConfig.md) \- this call is made after the HookServerConnect call and reports about the ser parameters of the data feed on the History Server that is connecting. Using the [IMTConFeeder](../Configuration-Interfaces/Data-Feeds/IMTConFeeder.md) interface you can get additional settings for external connection. These parameters are set in MetaTrader 5 Administrator when adding or editing Data Feed.



Description of the main methods of the [IMTConFeeder](../Configuration-Interfaces/Data-Feeds/IMTConFeeder.md) interface used to create a data feed:
    
    
    //--- data for external connection
       virtual LPCWSTR   Server(void) const=0;                // server address for external connection
       virtual LPCWSTR   Login(void) const=0;                 // login for external connection
       virtual LPCWSTR   Password(void) const=0;              // password for external connection
       //--- additional parameters
       virtual UINT      Mode(void) const=0;                  // operation mode(IMTConFeeder::EnFeedersMode)
       virtual LPCWSTR   Categories(void) const=0;            // news categories
     //--- navigation through symbols for which we receive quotes
       virtual UINT      SymbolTotal(void) const=0;           // total number of symbols whose quotes are received
       virtual LPCWSTR   SymbolNext(const UINT pos) const=0;  // getting symbol name by its number

External connection is used to get quotes and news from provider. Depending on how you connect to the external source, it's necessary to specify connection parameters, such as address, login, password. These parameters can be obtained by calling the methods of the IMTConFeeder interface.

As a result of calling the [Categories](../Configuration-Interfaces/Data-Feeds/IMTConFeeder/Categories.md) method we receive the root news category, set in MetaTrader 5 Administrator when adding or editing Data Feed. Ability to enter news category, when adding Data Feed, can filter out all news of this Data Feed. Upon receiving news their final category will be formed by adding news category itself to the root category. The root category can be empty. In this case Category() will return a string with a zero length.

For example, in Data Feed settings the root category has "MT5Datafeed" value, and the news passed to API has "DJ Newswires\PrimeTass\Real-Time news" category. After receiving this news API will assign to it the final "MT5Datafeed\DJ Newswires\PrimeTass\Real-Time news" category. In this example, the result of Category() call will be the "MT5Datafeed" string.

As noted above, how to use obtained settings - is up to developer. If Data Feed is fully managed by History Server, you need to start external connection using specified settings. If Data Feed works as an independent service, you can skip overriding the call and can set external connections parameters in advanced settings of service, for example, in a special configuration file.

<a id="example-of-data-feed-implementation"></a>
## Example of Data Feed implementation (#example-of-data-feed-implementation)

Examples, given in this article, are complete and will allow developers to quickly implement their own data sources. Let's consider Data Feed, which is fully controlled by History Server. Example is implemented in C++ in Visual Studio 2005/2008. You can download free Express edition from [Microsoft website](https://www.microsoft.com/express/Downloads/).

To create your own project, you can copy the ready implementation from the article. We offer typical ready-to-use solution, on which you can quickly and easily create your own Data Feed. Developers only have to correctly form Data Feed description and implement work with external connections: connection and data processing.

Let's consider organization of typical solution and methods, that should be implemented, in more details.

Data Feed's work is mostly implemented in the CMTDatafeedApp class. It is the main application class, and is inherited from the [IMTGatewaySink](Event-Interface.md) interface. Thus, overriding the virtual methods of the IMTGatewaySink interface, we're getting notifications from API. CMTDatafeedApp encapsulates two main entities: interface of server port API and external connection class.

To correctly form source description the in the Info(MTGatewayInfo& info) method of CMTDatafeedApp class, developers need to form the correct data describing Data Feed.

CDataSource external connection class implements access to external connections. For example, using object of this class, you can connect to data source, obtain quotes and news. CDataSource hides the details of external connection implementation. This kind of API add-on of quotes data, given by provider.

CDataSource works in a separate thread of commands execution. This is done for long pauses in interaction with external connections not to freeze Data Feed application.

Thus, the CMTDatafeedApp class has two interfaces: API and interface of external connection to data source. All CMTDatafeedApp work is reduced to correct initialization of these two interfaces and their management.

Also, to ease logging we've implemented the CLogger class in our project. After initializing object of this class by server port interface it can be conveniently used to add records to API journal. In order for logging to be available anywhere in the program, we've created global ExtLogger object of the CLogger class.

Let's consider described processes in details on the basis of source codes. Almost immediately after start an object of the CMTClient main managing class is created in application:
    
    
    //+------------------------------------------------------------------+
    //| Entry Point                                                      |
    //+------------------------------------------------------------------+
    int wmain(int argc,wchar_t** argv)
      {
       CMTDatafeedApp datafeed;
    //--- display banner
       Banner();
    //--- initialize application
       if(!datafeed.Initialize(argc,argv))
          return(-1);
    //--- main method of application
       datafeed.Run();
    //--- shutting down
       datafeed.Shutdown();
    //--- exit
       return(0);
      }

As you can be seen from the code, the main application function does initializes, starts and shuts down the main class of application. In the initialization method CMTDatafeedApp creates the server port interface of API and the object of external connections:
    
    
    //+------------------------------------------------------------------+
    //| Initialization |
    //+------------------------------------------------------------------+
    bool CMTDatafeedApp::Initialize(int argc,wchar_t** argv)
      {
       MTGatewayInfo info;
       MTAPIRES      ret=MT_RET_OK;
    //--- checking
       if(!argv)
          return(false);
    //--- library initialization
       if(m_apifactory.Initialize()!=MT_RET_OK)
          return(false);
    //--- filling MTGatewayInfo structure
       Info(info);
    //--- creating gateway interface
       ret=m_apifactory.Create(info,&m_gateway,argc,argv);
    //--- if this is the History server receiving information, exist
       if(ret==MT_RET_OK_NONE)
          return(false);
    //--- checking
       if(ret!=MT_RET_OK || m_gateway==NULL)
          return(false);
    //--- initialize logger
       ExtLogger.SetGateway(m_gateway);
    //--- creating data feed object
       if((m_source=new CDataSource())==NULL)
          return(false);
    //--- Successful
       return(true);
      }

In the Run method of CMTDatafeedApp class the thread of external connection is started and API server port is run. After start API server port is ready to receive incoming connections. In case of a successful launch, the application runs in the external connections control loop, until work is complete:
    
    
    //+------------------------------------------------------------------+
    //| Running application                                              |
    //+------------------------------------------------------------------+
    bool CMTDatafeedApp::Run()
      {
       bool started=false;
    //--- checking
       if(!m_gateway || !m_source)
          return(false);
    //--- starting to process external connection
       if(started=m_source->Start(m_gateway))
         {
          //--- starting to receive incoming connections
          started=m_gateway->Start(this)==MT_RET_OK;
         }
    //--- if running, setting the flag of operation of the controlling thread
       if(started)
          InterlockedExchange(&m_workflag,1);
    //--- main loop of controlling the connection
       while(InterlockedExchangeAdd(&m_workflag,0))
         {
          //--- checking external connection
          if(!m_source->Check())
             break;
          //--- delay
          Sleep(SLEEP_TIMEOUT);
         }
    //--- gateway stopping
       m_gateway->Stop();
    //--- completing data feed operation
       m_source->Shutdown();
    //--- Successful
       return(true);
      }

Thus, applications work is distributed across multiple threads. Application is multi-thread This somewhat complicates the architecture, but also allows to significantly enhance performance and reliability. To introduce application's dynamic model let's describe used threads and problems, solved by them, in details:

  * Main application thread \- used to control external connections and is responsible for application initialization and it's correct shutdown.
  * External connection thread \- works in the CDataSource class and is used to control and process data of external connection.
  * Network commands thread pool \- pool is hidden in API and is used to exchange data and to process control commands of connected History Servers. Callbacks of methods, overridden in IMTGatewaySink, from API are also done by one of the threads of this pool. API guarantees the impossibility of calling one method of IMTGatewaySink interface from more than one thread at a time. This means that more that one callback from API from more than one thread is not possible.



Data Feed developers must add code of controlling external connections to the appropriate CDataSource methods. Therefore, let's consider this class in details.

Object of CDataSource class accepts a pointer to the [IMTGatewayAPI](Main-Interface.md) interface. This makes the transmitting of received data to connected History Servers possible.

As noted above, work with external connection is implemented in a separate thread. The main loop of the thread is implemented in the ProcessThread method:
    
    
    //+------------------------------------------------------------------+
    //| External connection thread                                       |
    //+------------------------------------------------------------------+
    void CDataSource::ProcessThread(void)
      {
    //--- loop of controlling external connection
       while(InterlockedExchangeAdd(&m_workflag,0)>0)
         {
          //--- analyzing connection state; if it starts connection, then connection is processed
          if(GetState()==STATE_CONNECTSTART)
             ProcessConnect();
          //--- external connection successfully established, processing the data
          if(GetState()==STATE_CONNECTED)
             ProcessData();
          //--- delay
          Sleep(100);
         }
    //--- shutdown
       Shutdown();
      }

Managing CDataSource class is carried out from the main CMTDatafeedApp application class. The following public methods are used for management:

  * bool Start(IMTGatewayAPI *gateway) \- starting the thread of external connection processing.
  * bool Shutdown() \- shutting down external connection. Calling this method will close external connection and stop the thread of processing.
  * bool Init(const IMTConFeeder *config) \- initialization. After calling this method, the thread of CDataSource class will try to establish connection with parameters specified in the IMTConFeeder interface. Using that interface one can obtain all necessary information, such as: external connection address, login, password, etc.
  * bool Check() \- checking external connection for a hang-up, if the connection is not hanged up, then this method will returns true, otherwise - false.
  * LONG GetState() \- obtaining the state of external connection.
  * LONG SetState(LONG state) \- force setting the new state of connection.



Data Feed developers need to implement their own specific methods of external connection. All details of working with external connections are concentrated in the two methods of CDataSource class:

  * bool ProcessConnect \- in this method you must connect to external data source and return connection result.
  * bool ProcessData() \- in this method implementation you must obtain data from external source and pass them to the server port by means of the IMTGatewayAPI interface. You must return the correct result of these actions.



To get started, you need to copy the "MT5APIGateway.dll" and "MT5APIGateway64.dll" libraries from API application folder to folder with Data Feed executable. 
