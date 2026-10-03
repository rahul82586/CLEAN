[🏠 Document Start](../README.md) / [Gateway API](README.md) / Development and Debugging of Gateways

[Previous](Trade-Operations-in.md) | [Next](Symbol-and-Price-Translation.md)

<a id="developing-and-debugging-gateways"></a>
# Developing and Debugging Gateways (#developing-and-debugging-gateways)

One of the major advantages of MetaTrader 5 is its ability of complete integration with other trading systems. MetaTrader 5 integration is performed using the special library - Gateway API.

Using Gateway API, application developers can easily create their source of quotes and news or a gateway to an external trading system.

The section thoroughly describes basic principles of developing and debugging gateways, as well as the working example of "SampleGateway" in C++. Development of data feeds using Gateway API is described in details in the section ["Developing Data Feeds"](Development-of-Data-Feeds.md).

<a id="gateways-operation-principles-in-metatrader-5"></a>
## Gateways Operation Principles in MetaTrader 5 (#gateways-operation-principles-in-metatrader-5)

Gateways are executable files (*.exe) launched as separate processes. All gateways modules are reentrant. This means that several gateways can be created using one gateway *.exe module.

The main difference of gateways from data feeds is the ability to perform trading operations on the part of MetaTrader 5 platform in an external trading system. Besides, gateways allow to transfer quotes and news to MetaTrader 5 platform, similar to data feeds.

Any gateway may be launched automatically by a history server or work remotely. To allow a history server to launch a gateway, its executable file must be copied to gateway\<gateway name> subdirectory of the history server directory (for example, gateway\SampleGateway). This directory is the working directory of the gateway. All gateway data, operation logs, temporary parameters, etc. will be stored here. The value corresponding to a gateway name should be used as a gateway module, while performing settings in the administrator terminal.

To let the gateway work remotely, it must be launched with correct [command line parameters (#param)](Exported-Functions/MTGatewayCreateLocal.md#param). ["Remote Gateway"](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_gateways/gateway_service) value should be used as a gateway module, while setting up the gateway in the administrator terminal. This mode is also used for debugging gateways during their development.

After it has been launched, the gateway opens the server port to receive connections of MT5 platform distributed components. Components connection process is strictly defined and described in "[Interaction of the Platform and Gateway API](Interaction-of-the-Platform-and.md)".

Connection of a history server to the gateway is the first one to be established. It is used to deliver the appropriate parameters to the gateway and getting a stream of quotes and operation logs from it.

Connection of the main trading server to the gateway is the second one to be established. It is used to deliver the platform settings, trading symbols, groups and trading parameters to the gateway. Connection of other trading servers is established only after the main trading server has been connected. Any connection of a trading server (the main or secondary one) is used by the gateway to perform trading operations. After the connection to the main trading server has been established, the gateway is ready for operation with MetaTrader 5 platform.

After the gateway has been completely synchronized with MT5 platform, it can start performing its basic functions - transferring trading symbols, quotes, trading requests, etc. Connection to an external trading system must be established for that. Various exchanges, ECNs, etc. can serve as a trading system.

![How the Gateway Works](images/sample_gateway_scheme.png)

<a id="description-of-metatrader-5-gateway-api-for-working-with-the-gateway"></a>
## Description of MetaTrader 5 Gateway API for Working with the Gateway (#description-of-metatrader-5-gateway-api-for-working-with-the-gateway)

In this article we consider only the features of interaction with Gateway API when creating gateways. Development of data feeds has been described in a [separate section](Development-of-Data-Feeds.md).

After initializing the application and all Gateway API interfaces, it starts accepting incoming connections of MetaTrader 5 platform servers. After connecting the history and the main trading server, the gateway application is notified of the successful initial synchronization with MetaTrader 5 platform. The notification is performed by calling [IMTGatewayAPISink::OnGatewayStart](Event-Interface/OnGatewayStart.md) interface method.

This call allows the application to call data processing methods - trading symbols synchronization with an external system, submission of quote data, handling clients' trading requests, synchronization of an external system quotes with the ones in MT5, etc.

Symbols are imported to MetaTrader 5 platform during the initial synchronization or when updating data on them. IMTGatewayAPI interface methods are used for importing trading symbols to Gateway API:

  * [SymbolCreate](Main-Interface/Configuration-Databases/Symbols/SymbolCreate.md) \- creating a trading symbol settings interface.
  * [SymbolAddPreliminary](Main-Interface/Configuration-Databases/Symbols/SymbolAddPreliminary.md) \- synchronous dispatch of a trading symbol settings to MetaTrader 5 platform. All newly added trading symbols are put to the "\Preliminary" symbols subgroup with trading function being disabled. To perform trading operations with the symbol, an administrator should relocate it to the necessary group and allow trading.



If the symbol is already present in MetaTrader 5 platform, calling the method for adding a trading symbol will update parameters of the existing symbol without changing the path in the group. The filled copy of IMTConSymbol interface created as a result of calling [IMTGatewatAPI::SymbolCreate](Main-Interface/Configuration-Databases/Symbols/SymbolCreate.md) is submitted to this method as a parameter.

The gateway performs trading operations as a dealer connecting to the trading requests queue, picking a request for processing and confirming by processing result. The main difference of Gateway API from a conventional dealer is that all trading servers are connected to Gateway API and a unified requests queue is generated from requests queues belonging to each definite server. To manage the requests queue, IMTGatewayAPI interface methods are used in Gateway API:

  * [DealerStart](Main-Interface/Processing-Trade-Requests/DealerStart.md) \- connecting the gateway to the trading platform as a dealer. Using flags parameter allows to connect the queue with automatic picking of incoming trading requests and get additional request data concerning a client, an order, a position and a trading account. As the use of additional request data reduces MetaTrader 5 productivity, it should be applied only in exceptional cases.
  * [DealerStop](Main-Interface/Processing-Trade-Requests/DealerStop.md) \- disconnecting the gateway from the requests queue. After disconnecting from the requests queue as a dealer, the gateway application no longer gets the queue updates.
  * [DealerLockAsync](Main-Interface/Processing-Trade-Requests/DealerLockAsync.md) \- picking a request from the requests queue by ID. ID of the request that should be picked is submitted to this method as a parameter. This value can be obtained by [IMTRequest::ID](../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-ID.md) method. The request that has been picked by successful execution of this method, returns in [IMTGatewaySink::OnDealerLock](Event-Interface/OnDealerLock.md) method.
  * [DealerAnswerAsync](Main-Interface/Processing-Trade-Requests/DealerAnswerAsync.md) \- confirmation of the request that has been previously picked from the queue. The pointer to IMTConfirm request confirmation object containing the request ID, confirmation code, etc. is submitted to this method as a parameter.



Notification of the application of the results of requests and confirmations processing is performed by calling virtual IMTGatewaySink [IMTGatewaySink](Event-Interface.md) methods:

  * [OnDealerLock](Event-Interface/OnDealerLock.md) \- the gateway application notification on the result of picking a request for processing. If a request is picked successfully, MT_RET_OK value will be transferred in retcode value, otherwise - an error code. A trading request description is transmitted in request parameter.
  * [OnDealerAnswer](Event-Interface/OnDealerAnswer.md) \- the gateway application notification of the request confirmation processing result. If the trading request confirmation is processed successfully, MT_RET_OK value will be transferred in retcode value, otherwise - an error code. A trading request confirmation description is transmitted in 'confirm' parameter.
  * [HookGatewayAccountRequest](Event-Interface/HookGatewayAccountRequest.md) \- the hook for synchronizing MetaTrader 5 client's trading data with an external trading system. The hook is called when clicking "Synchronize" at "Account" tab of MetaTrader 5 Administrator, as well as when calling IMTAdminAPI::UserExternalSync and IMTManagerAPI::UserExternalSync methods from MetaTrader 5 Manager API. To synchronize the trading data, pass it to the platform using the [IMTGatewayAPI::GatewayAccountAnswer](Main-Interface/Synchronizing-Trading-Data/GatewayAccountAnswer.md) method.
  * [HookGatewayPositionsRequest](Event-Interface/HookGatewayPositionsRequest.md) \- the hook for receiving states of trading accounts used by the gateway to operate in an external system. The hook is called when clicking "Request" on "Positions" tab of the gateway in MetaTrader 5 Administrator. Set the [MTGatewayInfo::GATEWAY_MODE_POSITIONS](../Structures/MTGatewayInfo.md) flag during the gateway initialization to inform the platform of the possibility to request the states of positions. The states of positions are sent to the platform using the [IMTGatewayAPI::GatewayPositionsAnswer](Main-Interface/Controlling-Positions-in-External-System/GatewayPositionsAnswer.md) method.



  * The account in an external trading system should be specified in the account settings ("Account" tab) to request a trading data from that system.
  * After receiving a request for the account trading data synchronization or all accounts' position states, the gateway is to gather these data (for example, by sending a request to an external system) and pass them to MetaTrader 5 within 10 seconds (request lifetime).

  
---  
  
<a id="representation"></a>
## Gateway presentation to users: logo and description (#representation)

MetaTrader 5 supports the loading of the gateway logo and description from resources. Use this option to present your product in the [gateway showcase in MetaTrader 5 Administrator](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_gateways), as well as to provide documentation on the spot.

![Gateway presentation in MetaTrader 5 Administrator](images/gateway_showcase.png)

Add resources with the "DESCRIPTION" type and with the following IDs to your project:

  * 1000 — module description in free form, in UTF-8 format. Use an HTML document without classes and style, only with simple tags: h3, p, ul, ol, b, i. Standard Administrator terminal styles will be applied to the description and it will naturally fit into the interface.
  * 1001 — square logo for the showcase.
  * 1002 — square logo for high-resolution monitors.
  * 1003 — rectangle logo for the list of gateways and the details page.
  * 1004 — rectangle logo for high-resolution monitors.



An example of a .RC project file block:
    
    
    1000 DESCRIPTION "res\\description.html"
    1001 DESCRIPTION "res\\200x200.png"
    1002 DESCRIPTION "res\\400x400.png"
    1003 DESCRIPTION "res\\360x100.png"
    1004 DESCRIPTION "res\\720x200.png"

When loading the gateway module, the history server will pass this data to the main server, from which the information will be displayed in MetaTrader 5 Administrator.

<a id="processing-of-trading-requests-by-the-gateway"></a>
## Processing of Trading Requests by the Gateway (#processing-of-trading-requests-by-the-gateway)

There are two ways to process clients' market requests by the gateway. They can be conventionally called synchronous and asynchronous ones. They have similar procedures of getting a request by a server, its verification and routing in a requests queue. Vital differences begin at the point of processing a request.

During the synchronous processing of trading requests the gateway processes a customer's request, executes necessary operations (for example, transfers the request to an external system) and returns the result of its processing ([IMTConfirm](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTConfirm.md) request confirmation) to MT5 platform within the request lifetime (3 minutes). All necessary data (including the order tick in an external system, price and volume, etc.) has already been filled in confirmation of the request. Therefore, the client terminal gets data on a specific result of a request execution together with confirmation of the request execution.

The main limitations of this mechanism are:

  * Time of requests execution in an external trading system - an external system may not guarantee request execution time suitable for MetaTrader 5.
  * External trading system architecture - it is difficult to clearly associate the requests with their processing results. For example, asynchronous notification of the operations results, the ability to change orders and deals status from an external system, partial execution, etc.
  * Trading request setting delay - an objective need to provide a trader with the possibility to set the maximum number of requests in the minimum amount of time.



Considering these limitations, we can say that this mechanism is suitable for trading systems of market-maker markets having high (almost 100%) liquidity and guaranteed execution time suitable for MetaTrader 5.

If one of these conditions is violated (for example, there are partial executions for exchanges and ECNs with undetermined market order execution time and the operation of a trading system is strictly asynchronous), the gateway sends only synchronous confirmation of transferring a trading request to an external trading system. All other actions are determined only by the system productivity.

Notification of MetaTrader 5 platform is performed asynchronously via a stream of trading executions using [IMTExecution](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTExecution.md) interface. This mode is an asynchronous way to process trading requests. The mechanism is optimized for order-driven trading systems - exchanges and ECNs having high demands for productivity and unguaranteed execution time.

In the example of the gateway considered in this article we describe the operation of the gateway only in synchronous mode.

<a id="the-gateway-structure"></a>
## The Gateway Structure (#the-gateway-structure)

From a technical point of view, the main task of the gateway is to arrange data exchange between two different trading systems: MetaTrader 5 and an external one. Each system submits its own interaction interface. Interaction with MetaTrader 5 trading platform is located in two Gateway API interfaces: [IMTGatewayAPI](Main-Interface.md) and [IMTGatewayAPISink](Event-Interface.md). Interaction with an external system is arranged using API submitted by an external system provider.

Basic application class (CMTGatewayApp in our case) is an entry point of the gateway application. It implements launch/stop operations of the application and all of its major work. The class is inherited from [IMTGatewaySink](Event-Interface.md) interface. Its objectives are initialization, connection to/disconnection from Gateway API, getting notifications from MT5 platform about various events taking place in it and submitting them to the gateway class (CGateway in our case).

The gateway class implements its business logic and provides interaction of MT5 platform with an external trading system. In fact, the class assigns implementation of the gateway business logic to its subclasses.

To provide interaction of the gateway with MetaTrader 5 platform, the gateway class refers to [IMTGatewayAPI](Main-Interface.md) interface. To provide interaction of the gateway with an external trading system, the gateway class refers to the interface of the interaction with an external trading system (CExchangeAPI in our case).

To process MetaTrader 5 event notifications concerning trading requests (for example, picking a trading request from the requests queue, result of request confirmation by MT5 platform), the gateway class refers to trading dispatcher class (CTradeDispatcher in the example). The objectives of this class are as follows:

  * receiving, analyzing and processing of clients' trading requests;
  * transferring trading requests to an external trading system;
  * generation of trading requests and trading executions confirmations;
  * processing of external trading system responses to trading requests.



The interface class of interaction with an external trading system implements two basic functions: storing data on trading symbols and logic of processing and data exchange between MT5 platform and an external trading system. This data includes trading symbols settings, quotes data, trading requests etc. The class assigns these functions to its subclasses - the class of available trading symbols base (CExchangeSymbols in the example) and the class of the context of connection to an external trading system (CExchangeContext in the example).

The class of available trading symbols base is used for storing data on trading symbols and synchronization of trading symbols settings with the ones in MetaTrader 5 platform. This class provides adding, changing, deleting, searching available trading symbols and processing all transactions received from an external trading system and related to the trading symbols. Such transactions are, for example, getting trading symbols settings, quotes data, responses to trading requests from an external trading system etc.

Let's consider the process of data exchange between the gateway and an external trading system. Generally, the data exchange occurs in several stages:

  * Data conversion from MetaTrader 5 platform format to an external trading system one (and vice versa);
  * Data package generation/unpacking according to the established protocol of data exchange with external trading system;
  * Exchanging data packages with an external trading system server.



Data exchange between the gateway and an external system is performed in the external connection context class. Generally, the gateway may have several contexts of connection to an external trading system. This class is designed to receive/send data packages between an external trading system and the gateway. Data packages are generated according to the exchange protocol (CExchangeProtocol class in our case), submitted by an external system provider.

The connection context class refers to a special class providing an appropriate functionality (CExchangeSocket in our case) to physically connect to an external trading system server and receive/send data packages. Its implementation is fully determined by the type of an external connection delivered by an external system provider.

<a id="samplegateway"></a>
## SampleGateway (#samplegateway)

Ready-made working example will allow programmers to quickly and efficiently implement their own applications for integration with MetaTrader 5 based on Gateway API. To achieve this, we have developed the example of SampleGateway that may serve as a template when developing a custom application.

SampleGateway (similar to SampleExchange external trading system described below) is a 32/64-bit application developed in C++ in Microsoft Visual Studio 2005/2008 environment. Free Express versions of MS Visual Studio can be [downloaded from Microsoft website](https://www.microsoft.com/express/Downloads/).

Simplified gateway module has been implemented in SampleGateway. The gateway connects to MetaTrader 5 via Gateway API. After the full synchronization with the platform, the gateway initiates connection to SampleExchange external trading system (described below) via the appropriate interface. Further on, the gateway receives the settings of all trading symbols available in an external trading system.

Four trading symbols with various orders execution modes are available to be displayed in an external trading system:

  * "EURUSD.TEST" having request execution mode;
  * "GBPUSD.TEST" having instant execution mode;
  * "USDCHF.TEST" having market execution mode;
  * "MQ-FUT" having exchange execution mode.



After the gateway gets all symbols, connection of the gateway and an external trading system is deemed to be synchronized. Since that moment, the gateway starts getting quotes data on all available trading symbols from an external trading system. Besides, the gateway connects to the trading requests queue and starts processing them.

> SampleGateway is a demo gateway interacting only with SampleExchange external trading system.

Let us have a more detailed look at SampleGateway structure including the source code.

<a id="samplegateway-initialization-and-launch"></a>
## SampleGateway Initialization and Launch (#samplegateway-initialization-and-launch)

We will start from implementation of CMTGatewayApp application basic class. As it has already been noted, it is inherited from IMTGatewaySink interface. The first thing to do is to initialize Gateway API factory classes using [CMTGatewayAPIFactory::Initialize](CMTGatewayAPIFactory/Initialize.md) method and create a copy of Gateway API using [CMTGatewayAPIFactory::Create](CMTGatewayAPIFactory/Create.md) method:
    
    
    //--- initialize Gateway API library
       if(m_api_factory.Initialize()!=MT_RET_OK)
          return(false);
    //--- generate description
       Info(info);
    //--- create Gateway API instance
       res=m_api_factory.Create(info,&m_api_gateway,argc,argv);

The first parameter of [CMTGatewayAPIFactory::Create](CMTGatewayAPIFactory/Create.md) method receives description of the gateway module as the structure of [MTGatewayInfo](../Structures/MTGatewayInfo.md). This structure must first be filled This is performed in CMTGatewayApp::Info: method in our case:
    
    
    void CMTGatewayApp::Info(MTGatewayInfo &info)
      {
    //--- generate description
       ZeroMemory(&info,sizeof(info));
    //--- data
       info.version    =ProgramBuild;
       info.version_api=MTGatewayAPIVersion;
       CMTStr::Copy(info.name_default,      _countof(info.name_default),ProgramName);
       CMTStr::Copy(info.copyright,         _countof(info.copyright),         L"Copyright 2001-2016, MetaQuotes Software Corp.");
       CMTStr::Copy(info.build_date,        _countof(info.build_date),        ProgramBuildDate);
       CMTStr::Copy(info.build_api_date,    _countof(info.build_api_date),    MTGatewayAPIDate);
       CMTStr::Copy(info.server_default,    _countof(info.server_default),    L"127.0.0.1");
       CMTStr::Copy(info.login_default,     _countof(info.login_default),     L"default");
       CMTStr::Copy(info.password_default,  _countof(info.password_default),  L"default");
       CMTStr::Copy(info.module_id,         _countof(info.module_id),         L"gatewayid");
       info.mode  =MTGatewayInfo::GATEWAY_MODE_QUOTES|MTGatewayInfo::GATEWAY_MODE_POSITIONS;
       info.fields=MTGatewayInfo::GATEWAY_FIELD_ALL;
       CMTStr::Copy(info.description,       _countof(info.description)-1,ProgramDescription);
      }

The gateway life cycle is implemented in CMTGatewayApp::Run method: launch of Gateway API server port, the gateway running cycle and turning Gateway API server port off after completing the operation:
    
    
    bool CMTGatewayApp::Run()
      {
    //--- ...
    //--- start Gateway API
       if(m_api_gateway->Start(this)!=MT_RET_OK)
         {
          ExtLogger.Out(MTLogErr,L"MTGatewayApp: failed to start MetaTrader 5 Gateway API");
          return(false);
         }
    //--- set working flag
       Working(1);
    //---- main loop of check
       while(Working())
         {
          //--- check gateway state
          m_gateway->Check();
          //--- sleep
          Sleep(TIMEOUT_CHECK_STATE);
         }
    //--- stop Gateway API
       m_api_gateway->Stop();
    //--- ...
      }

[IMTGatewayAPI::Start](Main-Interface/Server/Start.md) method called in this code launches Gateway API server port. After that, the application flow is transferred to a working state using Working(1) method. Method [IMTGatewayAPI::Stop](Main-Interface/Server/Stop.md) is used to turn Gateway API server port off.

<a id="samplegateway-interaction-with-an-external-trading-system"></a>
## SampleGateway Interaction with an External Trading System (#samplegateway-interaction-with-an-external-trading-system)

In the above example m_gateway is a pointer to CGateway class. According to the gateway and external connection states, calling m_gateway->Check method manages application flows - the flows of transactions processing and data exchange with an external trading system:
    
    
    void CGateway::Check(void)
      {
    //--- check
       if(!m_api_exchange)
          return;
    //--- exit if Gateway API is not ready for work
       if(StatusGateway()<=STATUS_API_CONFIGURED)
          return;
    //--- API is ready for work, check connection to external trading system
       if(StatusExchange()>=STATUS_CONNECTED)
         {
          //--- check connection to external trading system
          if(!m_api_exchange->Check())
            {
             //--- external trading system haven't responded during timeout
             ExtLogger.Out(MTLogErr,L"exchange timed out");
             StatusExchange(STATUS_DISCONNECTED);
             return;
            }
         }
    //--- analyze state, start connection in the check thread,
    //--- it is safe, because external trading system API is operating asynchronously
       if(StatusExchange()<=STATUS_CONNECTING)
          Connect();
      }

CGateway::Connect method calling is asynchronous one. It initializes the interface of the interaction with an external trading system and the launch of its workflow. Let us consider the interface of interaction with an external trading system in details.

The interface of interaction with an external trading system has been implemented in CExchangeAPI class. Processing of the data obtained in connection contexts is arranged in a separate flow. This allows to improve the performance of the gateway application, separate the process of the network input/output and processing the data obtained from an external trading system.

Processing of accumulated transactions received from an external trading system is performed in the workflow of the interface for interaction with CExchangeAPI external trading system:
    
    
    void CExchangeAPI::ProcessThread(void)
     
      {
       bool trans_applied=false;
    //--- loop of data processing
       while(InterlockedExchangeAdd(&m_thread_workflag,0)>0)
         {
          //--- process received data
          m_exchange_context.TransApply(m_symbols,trans_applied);
          //--- sleep if there are no transactions
          if(!trans_applied)
             Sleep(TRANS_WAIT_TIME);
         }
      }

<a id="samplegateway-connection-to-an-external-trading-system"></a>
## SampleGateway Connection to an External Trading System (#samplegateway-connection-to-an-external-trading-system)

CExchangeContext is the context class of the external connection in this example. As noted above, the gateway may have several connection contexts according to the number of various connections to an external trading system. Only one external connection and, as a result, one context are used in SampleGateway application.

One more flow (connection context workflow) is launched during this class initialization. The main objective of the connection context class is a network data packages exchanges between the gateway and an external system in the connection context workflow.

Let us consider the workflow of an external connection context class:
    
    
    void CExchangeContext::ProcessThread(void)
      {
    //--- ...
    //--- initialize connection
       if(!m_socket->Connect(m_address,m_port))
          return;
    //--- flags of data processing
       bool data_send=false,data_receive=false;
    //--- loop of managing external connection
       while(InterlockedExchangeAdd(&m_thread_workflag,0)>0)
         {
          //--- receive sent data
          if(!ReceiveCheck(data_receive))
             break;
          //--- process data for sending
          if(!SendCheck(data_send))
             break;
          //--- if there was no data exchange, then sleep
          if(!data_send && !data_receive)
             Sleep(THREAD_SLEEP);
         }
    //--- close socket
       m_socket->Close();
    //--- ...
      }

The attempt to connect to an external trading system is made in this flow by calling m_socket->Connect method. Here m_socket is a pointer to CExchangeSocket class object implementing the functions of physical connection to/disconnection from an external trading system server, as well as data exchange with it.

Packages exchange between the gateway and an external trading system is implemented in ReceiveCheck and SendCheck methods of a basic cycle of that flow.

We will examine the code of the external connection context workflow.

After receiving the data packages, the context class unpacks a data packet using the data exchange protocol class. Depending on the data package type, it adds an appropriate transaction for processing by the class of the interface for interaction with CExchangeAPI external system. Let us display the implementation of the quotes data package processing method, in which a transaction with quotes data is added to m_trans_ticks ticks transactions array:
    
    
    bool CExchangeContext::OnMessageTick(const ExchangeMsgTick &msg)
      {
       bool res=false;
    //--- lock
       m_trans_sync.Lock();
    //--- add tick transaction for processing
       res=m_trans_ticks.Add(&msg.tick);
    //--- unlock
       m_trans_sync.Unlock();
    //--- return result
       return(res);
      }

Direct processing of obtained data is not included into the connection context class function. As mentioned above, it is performed in CExchangeAPI class flow in CExchangeContext::TransApply method:
    
    
    bool CExchangeContext::TransApply(CExchangeSymbols &symbols,bool &trans_applied)
      {
       bool res=false;
    //--- results of processing transactions
       bool symbols_applied=false,ticks_applied=false,books_applied=false,orders_applied=false,deals_applied=false;
    //--- clear arrays
       m_trans_symbols_tmp.Clear();
       m_trans_ticks_tmp.Clear();
       m_trans_books_tmp.Clear();
       m_trans_orders_tmp.Clear();
       m_trans_deals_tmp.Clear();
    //--- lock
       m_trans_sync.Lock();
    //--- get contents of arrays
       m_trans_symbols.Swap(m_trans_symbols_tmp);
       m_trans_ticks.Swap(m_trans_ticks_tmp);
       m_trans_books.Swap(m_trans_books_tmp);
       m_trans_orders.Swap(m_trans_orders_tmp);
       m_trans_deals.Swap(m_trans_deals_tmp);
    //--- unlock
       m_trans_sync.Unlock();
    //--- process received transactions
       res=TransApplySymbols(symbols,m_trans_symbols_tmp,symbols_applied);
       res=res && TransApplyTicks(symbols,m_trans_ticks_tmp,ticks_applied);
       res=res && TransApplyBooks(symbols,m_trans_books_tmp,books_applied);
       res=res && TransApplyOrders(symbols,m_trans_orders_tmp,orders_applied);
       res=res && TransApplyDeals(symbols,m_trans_deals_tmp,deals_applied);
    //--- flag of data availability
       trans_applied=symbols_applied || ticks_applied || books_applied || orders_applied || deals_applied;
    //--- return result
       return(res);
      }

Five types of transactions are processed here:

  * transactions with trading symbols settings in CExchangeContext::TransApplySymbols method;
  * transactions with quote data in CExchangeContext::TransApplyTicks method;
  * transactions with trading orders in CExchangeContext::TransApplyOrders method;
  * transactions with performed deals in CExchangeContext::TransApplyDeals method;
  * transactions with the current state of depth of market in CExchangeContext::TransApplyBooks method.



<a id="processing-of-samplegateway-transactions-using-available-trading-symbols-base-class"></a>
## Processing of SampleGateway Transactions Using Available Trading Symbols Base Class (#processing-of-samplegateway-transactions-using-available-trading-symbols-base-class)

The interface class for interaction with CExchangeAPI external trading system directs CExchangeSymbols available trading symbols base class to process all transactions. We will examine the processing of data transactions on the example of transaction with quote data:
    
    
    bool CExchangeSymbols::OnSymbolTickApply(const ExchangeTick &exchange_tick)
      {
    //--- ...
    //--- import tick
       MTTick gateway_tick={0};
    //--- import symbol
       CMTStr::Copy(gateway_tick.symbol,_countof(gateway_tick.symbol),exchange_tick.symbol);
    //--- import price source
       CMTStr::Copy(gateway_tick.bank,_countof(gateway_tick.bank),exchange_tick.bank);
    //--- import bid price
       gateway_tick.bid   =exchange_tick.bid;
    //--- import ask price
       gateway_tick.ask   =exchange_tick.ask;
    //--- import last price
       gateway_tick.last  =exchange_tick.last;
    //--- import last deal volume
       gateway_tick.volume=exchange_tick.volume;
    //--- import datetime
       gateway_tick.datetime=exchange_tick.datetime;
    //--- send to Gateway API
       return(m_gateway.GatewayTickSend(gateway_tick));
      }

In this case the quote data is converted from an external trading system (ExchangeTick) in MetaTrader 5 ([MTTick](../Structures/MTTick.md)) platform format and sent to a history server. Sending is implemented in CExchangeSymbols::OnSymbolTickApply method.

Similar processing has been implemented for other exchange data - trading symbols settings, trading orders, etc. Simplified processing of data transaction has been implemented in SampleGateway. Developers need to add their implementation to the mentioned methods for processing data transactions in the real gateway application.

<a id="trading-requests-processing-in-samplegateway"></a>
## Trading Requests Processing in SampleGateway (#trading-requests-processing-in-samplegateway)

Now, let us consider the trading interaction between the gateway, MetaTrader 5 platform and an external trading system.

As mentioned above, external connection of the gateway gets into STATUS_SYNCHRONIZED state after it receives all trading symbols from an external trading system. The stage of trading interaction comes after that. To achieve it, the gateway must connect to MetaTrader 5 trading requests queue using [IMTGatewayAPI::DealerStart](Main-Interface/Processing-Trade-Requests/DealerStart.md) method.

In SampleGateway this has been implemented in establishing CGateway::StatusExchange gateway external connection status method:
    
    
    LONG CGateway::StatusExchange(const LONG status)
      {
    //--- ...
       if(status==STATUS_SYNCHRONIZED)
         {
          //--- connect to the request queue
          m_api_gateway->DealerStart(IMTGatewayAPI::DEALER_FLAG_AUTOLOCK);
         }
    //--- ...
      }

After the gateway has connected to the queue of trading requests, they are picked by Gateway API and transferred to the gateway. At the same time Gateway API calls CMTGatewayApp::OnDealerLock notification method. The basic class of the application transfers a trading request to the gateway class, while this class, in its turn, transfers it to the trading dispatcher class.

The trading dispatcher has been implemented in CTradeDispatcher class of SampleGateway. The main function of the class is processing trading requests received from MetaTrader 5 platform, their confirmation and sending to an external trading system.

Trading requests processing has been implemented in CTradeDispatcher::GatewayProcess trading dispatcher class method. As SampleGateway is a simplified gateway sample, trading requests processing has been implemented only for demonstration purposes in this application.

After the gateway gets a trading request, the presence of a trade instrument, for which the request ([IMTRequest](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md)) has arrived, is checked. Possibility of automatic confirmation is also checked. If the automatic confirmation is impossible, the request is sent to an external trading system in GatewayExecuteExchange method. 
    
    
    void CTradeDispatcher::GatewayProcess(const IMTRequest *request)
      {
    //--- ...
    //--- symbol
       ExchangeSymbol symbol={0};
    //--- check the presence of a symbol a request is assigned to
       if(!m_api_exchange->SymbolGet(request->Symbol(),symbol))
         {
          ExtLogger.Out(MTLogErr,L"symbol %s not found",request->Symbol());
          //--- send request error
          SendRequestConfirm(MT_RET_REQUEST_ERROR,request);
          return;
         }
    //--- check if a request can be confirmed automatically
       if(GatewayProcessAuto(request))
         {
          //--- confirm request
          SendRequestConfirm(MT_RET_REQUEST_DONE,request);
          return;
         }
    //--- execute request at an exchange
       if(!GatewayExecuteExchange(request))
         {
          //--- unable to send request to external system, send request error
          SendRequestConfirm(MT_RET_REQUEST_ERROR,request);
         }
      }

In GatewayExecuteExchange method, the request is converted in external trading system format (ExchangeOrder) and sent to it in m_api_exchange->SendOrder method:
    
    
    bool CTradeDispatcher::GatewayExecuteExchange(const IMTRequest *request)
      {
    //--- check
       if(!m_api_exchange)
          return(false);
    //--- send order
       ExchangeOrder exchange_order={0};
    //--- order action type
       UINT request_action=request->Action();
    //--- enter the type of operation
       GetOrderActionByRequestAction(request_action,exchange_order.order_action);
    //--- order ticket
       exchange_order.order_mt_id=request->Order();
    //--- order id in external system
       exchange_order.request_mt_id=request->ID();
    //--- symbol
       CMTStr::Copy(exchange_order.symbol,_countof(exchange_order.symbol),request->Symbol());
    //--- client's login
       exchange_order.login=request->Login();
    //--- order type
       exchange_order.type_order=request->Type();
    //--- expiration type
       exchange_order.type_time=request->TypeTime();
    //--- action
       exchange_order.action=request_action;
    //--- price
       exchange_order.price_order=request->PriceOrder();
    //--- Stop Loss level
       exchange_order.price_SL=request->PriceSL();
    //--- Take Profit level
       exchange_order.price_TP=request->PriceTP();
    //--- volume
       exchange_order.volume=UINT64(SMTMath::VolumeToDouble(request->Volume()));
    //--- expiration time
       exchange_order.expiration_time=request->TimeExpiration();
    //--- if Take Profit activation order arrived
       if(exchange_order.action==IMTRequest::TA_ACTIVATE_TP)
         {
          //--- send pending order
          exchange_order.action=IMTRequest::TA_PENDING;
          //--- order expires in 5 seconds
          exchange_order.expiration_time=GetExchangeTime()+MT_ORDER_ACTIVATION_TIMEOUT;
         }
    //--- if Stop Loss or Stop order activation order arrived
       if(exchange_order.action==IMTRequest::TA_ACTIVATE_SL || exchange_order.action==IMTRequest::TA_ACTIVATE)
         {
          //---  order activated on MT side
          if(exchange_order.action==IMTRequest::TA_ACTIVATE)
             exchange_order.order_custom_data=MT_ORDER_ACTIVATION_FLAG;
          //--- send market order
          exchange_order.action=IMTRequest::TA_EXCHANGE;
          //--- reset order price
          exchange_order.price_order=0;
          //--- order expires in 5 seconds
          exchange_order.expiration_time=GetExchangeTime()+MT_ORDER_ACTIVATION_TIMEOUT;
         }
    //--- if Stop Limit order activation order arrived
       if(exchange_order.action==IMTRequest::TA_ACTIVATE_STOPLIMIT)
         {
          //--- send pending order
          exchange_order.action=IMTRequest::TA_PENDING;
          //--- set order activation price
          exchange_order.price_order=request->PriceTrigger();
         }
    //--- send order to exchange
       return(m_api_exchange->SendOrder(exchange_order));
      }

On arrival of trading transaction from an external trading system, it is processed in CTradeDispatcher::OnExchangeOrderTrans trading dispatcher class method:
    
    
    bool CTradeDispatcher::OnExchangeOrderTrans(const ExchangeOrder &exchange_order,const ExchangeSymbol &symbol)
      {
       bool res=true;
    //--- analyze order state
       switch(exchange_order.order_state)
         {
          case ExchangeOrder::ORDER_STATE_CONFIRMED:
            {
             //--- send confirmation only
             res=res && SendOrderConfirm(exchange_order);
             break;
            }
          case ExchangeOrder::ORDER_STATE_REQUEST_PLACED:
          case ExchangeOrder::ORDER_STATE_REQUEST_MODIFY:
          case ExchangeOrder::ORDER_STATE_REQUEST_CANCEL:
            {
             //--- send confirmation and execution
             res=res && SendOrderConfirm(exchange_order);
             res=res && SendOrderExecution(exchange_order);
             break;
            }
          case ExchangeOrder::ORDER_STATE_NEW:
          case ExchangeOrder::ORDER_STATE_MODIFY:
          case ExchangeOrder::ORDER_STATE_CANCEL:
          case ExchangeOrder::ORDER_STATE_REJECT_NEW:
          case ExchangeOrder::ORDER_STATE_REJECT_MODIFY:
          case ExchangeOrder::ORDER_STATE_REJECT_CANCEL:
            {
             //--- send execution only
             res=res && SendOrderExecution(exchange_order);
             break;
            }
          default:
            {
             res=false;
            }
         }
       return(res);
      }

When processing such type of transactions, the state of an arrived order is analyzed in CTradeDispatcher::OnExchangeOrderTrans method. Depending on the analysis results, confirmation of trade requests ([IMTConfirm](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTConfirm.md)) or result of trade orders execution ([IMTExecution](../Database-Interfaces/Trade/Trade-Requests/Requests-IMTExecution.md)) is sent to MetaTrader 5 platform..

The trade request is confirmed in [IMTGatewayAPI::DealerAnswerAsync](Main-Interface/Processing-Trade-Requests/DealerAnswerAsync.md) method. It has been shown in CTradeDispatcher::SendRequestConfirm trading dispatcher method:
    
    
    bool CTradeDispatcher::SendRequestConfirm(const ExchangeOrder &exchange_order)
      {
    //--- ...
       res=m_confirm_exchange->Clear()==MT_RET_OK;
       res=res && (m_confirm_exchange->ID((UINT)exchange_order.external_id)==MT_RET_OK);
       res=res && (m_confirm_exchange->Volume(exchange_order.volume)==MT_RET_OK);
       res=res && (m_confirm_exchange->Price(exchange_order.price_order)==MT_RET_OK);
       res=res && (m_confirm_exchange->TickBid(exchange_order.price_tick_bid)==MT_RET_OK);
       res=res && (m_confirm_exchange->TickAsk(exchange_order.price_tick_ask)==MT_RET_OK);
       res=res && (m_confirm_exchange->Retcode(exchange_order.result)==MT_RET_OK);
    //--- send confirmation to MT5
       res=res && (m_api_gateway->DealerAnswerAsync(m_confirm_exchange)==MT_RET_OK);
    //--- return result
       return(res);
      }

Results of trade orders' execution are sent in [IMTGatewayAPI::DealerAnswerAsync](Main-Interface/Processing-Trade-Requests/DealerAnswerAsync.md) method. It has been shown in CTradeDispatcher::SendOrderConfirm method:
    
    
    bool CTradeDispatcher::SendOrderConfirm(const ExchangeOrder &exchange_order)
      {
    //--- ...   
    //--- set confirmation data
       res=m_confirm_exchange->Clear()==MT_RET_OK;
       res=res && (m_confirm_exchange->ID((UINT)exchange_order.request_mt_id)==MT_RET_OK);
       CMTStr::FormatStr(str,L"%I64u",exchange_order.order_exchange_id);
       res=res && (m_confirm_exchange->OrderID(str)==MT_RET_OK);
       res=res && (m_confirm_exchange->Volume(SMTMath::VolumeToInt(double(exchange_order.volume)))==MT_RET_OK);
       res=res && (m_confirm_exchange->Price(exchange_order.price_order)==MT_RET_OK);
       res=res && (m_confirm_exchange->TickBid(exchange_order.price_tick_bid)==MT_RET_OK);
       res=res && (m_confirm_exchange->TickAsk(exchange_order.price_tick_ask)==MT_RET_OK);
       res=res && (m_confirm_exchange->Retcode(exchange_order.result)==MT_RET_OK);
    //--- send confirmation to MT5
       if(res && m_api_gateway->DealerAnswerAsync(m_confirm_exchange)!=MT_RET_OK)
         {
          ExtLogger.Out(MTLogErr,L"'%I64u': request #%I64u failed to send confirm %s (%d)",
                        exchange_order.login,
                        exchange_order.order_exchange_id,
                        m_confirm_exchange->Print(str),
                        res);
          res=false;
         }
       else
          LogAnswerExchange(exchange_order,m_confirm_exchange);
    //--- return result
       return(res);
      }

<a id="samplegateway-trading-data-synchronization"></a>
## SampleGateway Trading Data Synchronization (#samplegateway-trading-data-synchronization)

If [an account in an external trading system (#trade-accounts)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/account_edit#trade-accounts) is specified for a trade account, then the [IMTGatewaySink::HookGatewayAccountRequest](Event-Interface/HookGatewayAccountRequest.md) hook is called when clicking "Synchronize" at "Account" tab of MetaTrader 5 Administrator, as well as when calling IMTAdminAPI::UserExternalSync and IMTManagerAPI::UserExternalSync methods from MetaTrader 5 Manager API. In SampleGateway, the request for client's trading data is passed to the gateway class.
    
    
    MTAPIRES CMTGatewayApp::HookGatewayAccountRequest(UINT64 login,LPCWSTR account_id)
      {
       MTAPIRES res=MT_RET_ERROR;
    //--- notify gateway
       if(m_gateway)
          res=m_gateway->HookGatewayAccountRequest(login,account_id);
    //--- return result
       return(res);
      }

The gateway sends an account trading data request to the external trading system using the m_api_exchange->SendAccountDataRequest method with a specified login.
    
    
    MTAPIRES CGateway::HookGatewayAccountRequest(UINT64 login,LPCWSTR account_id)
      {
       bool res;
    //--- request account data from exchange
       res=m_api_exchange->SendAccountDataRequest(login);
    //--- return result
       return(res?MT_RET_OK:MT_RET_ERROR);
      }

If the MTGatewayInfo::GATEWAY_MODE_POSITIONS flag has been specified in [MTGatewayInfo::mode](../Structures/MTGatewayInfo.md) when creating a GatewayAPI instance, the tab allowing you to request the [list of positions in an external system](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_gateways/gateway_positions) becomes available in the gateway page of the MetaTrader 5 Administrator. The [IMTGatewaySink::HookGatewayPositionsRequest](Event-Interface/HookGatewayPositionsRequest.md) hook is called during the request. In SampleGateway, the request for positions is passed to the gateway class.
    
    
    MTAPIRES CMTGatewayApp::HookGatewayPositionsRequest()
      {
       MTAPIRES res=MT_RET_ERROR;
    //--- notify gateway
       if(m_gateway)
          res=m_gateway->HookGatewayPositionsRequest();
    //--- return result
       return(res);
      }

In order to receive the list of all positions, the gateway sends a trading data request to the external trading system using the m_api_exchange->SendAccountDataRequest method with no login specified.
    
    
    MTAPIRES CGateway::HookGatewayPositionsRequest()
      {
       ExchangePositionsArray positions_exchange;
       IMTPositionArray   *positions_gateway=NULL;
       MTAPIRES            res              =MT_RET_OK;
    //--- get exchange positions
       if(!m_api_exchange->SendAccountDataRequest(0))
          res=MT_RET_ERROR;
    //--- return result
       return(res);
      }

When data from the external system arrive, they are processed using the CGateway::OnExchangeAccountDataReceived method.
    
    
    bool CGateway::OnExchangeAccountDataReceived(const ExchangeAccountData &account_data)
      {
       IMTUser            *user_gateway     =NULL;
       IMTAccount         *account_gateway  =NULL;
       IMTOrderArray      *orders_gateway   =NULL;
       IMTPositionArray   *positions_gateway=NULL;
       MTAPIRES            res              =MT_RET_OK;
    //--- create user interface
       user_gateway=m_api_gateway->UserCreate();
    //--- create account interface
       account_gateway=m_api_gateway->UserCreateAccount();
    //--- create positions array interface
       positions_gateway=m_api_gateway->GatewayPositionArrayCreate();
    //--- create orders array interface
       orders_gateway=m_api_gateway->GatewayOrderArrayCreate();
    //--- check interfaces
       if(!user_gateway || !account_gateway || !orders_gateway || !positions_gateway)
          res=MT_RET_ERR_MEM;
    //--- if login is specified 
       if(account_data.login>0)
         {
          //--- request user data 
          res=m_api_gateway->UserGet(account_data.login,user_gateway);
          //--- set account balance
          if(res==MT_RET_OK)
             res=account_gateway->Balance(account_data.balance);
         }
    //--- convert orders
       if(res==MT_RET_OK && account_data.orders.Total()>0)
          res=ConvertOrders(account_data.orders,orders_gateway);
    //--- convert positions
       if(res==MT_RET_OK && account_data.positions.Total()>0)
         {
          res=ConvertPositions(account_data.positions,positions_gateway);
         }
    //--- answer with data
       if(res==MT_RET_OK)
         {
          //--- if login is specified, answer in HookGatewayAccountRequest
          if(account_data.login)
             res=m_api_gateway->GatewayAccountAnswer(res,m_api_gateway->TimeCurrent(),user_gateway,account_gateway,orders_gateway,positions_gateway);
          else 
            {
             //--- answer in HookGatewayPositionsRequest
             res=m_api_gateway->GatewayPositionsAnswer(res,m_api_gateway->TimeCurrent(),positions_gateway);
            }
         }
    //--- release interfaces
       if(user_gateway)
          user_gateway->Release();
       if(account_gateway)  
          account_gateway->Release();
       if(orders_gateway)
          orders_gateway->Release();
       if(positions_gateway)
          positions_gateway->Release();
    //--- return result
       return(res==MT_RET_OK || res==MT_RET_OK_NONE);
      }

The interfaces of a user, a trade account, a list of orders and positions are created here. If a trading login is specified, its balance is displayed in the external system. The list of orders and positions is converted into MetaTrader 5 format. After that, the gateway responds to an initial hook using [IMTGatewayAPI::GatewayAccountAnswer](Main-Interface/Synchronizing-Trading-Data/GatewayAccountAnswer.md) or [IMTGatewayAPI::GatewayPositionsAnswer](Main-Interface/Controlling-Positions-in-External-System/GatewayPositionsAnswer.md) method and releases the created interfaces.

Orders are converted using the CGateway::ConvertOrders method
    
    
    MTAPIRES CGateway::ConvertOrders(const ExchangeOrdersArray &exchange_orders,IMTOrderArray *gateway_orders) const
      {
       IMTOrder      *gateway_order=NULL;
       ExchangeSymbol exchange_symbol;
       CMTStr32       str;
       MTAPIRES       res          =MT_RET_OK;
    //--- check
       if(!m_api_gateway || !gateway_orders)
          return(false);
    //--- go through all orders
       for(UINT i=0;i<exchange_orders.Total() && res==MT_RET_OK;i++)
         {
          //--- skip empty orders
          if(exchange_orders[i].volume==0)
             continue;
          //--- get Gateway API order interface
          if((gateway_order=m_api_gateway->OrderCreate())!=NULL)
            {
             //--- set order ticket
             res=gateway_order->OrderSet(exchange_orders[i].order_mt_id);
             //--- format order external id
             str.Format(L"%I64u",exchange_orders[i].order_exchange_id);
             //--- set order external id
             if(res==MT_RET_OK)
                res=gateway_order->ExternalID(str.Str());
             //--- set order symbol
             if(res==MT_RET_OK)
                res=gateway_order->Symbol(exchange_orders[i].symbol);
             //--- set order volume
             if(res==MT_RET_OK)
                res=gateway_order->VolumeInitial(SMTMath::VolumeToInt((double)exchange_orders[i].volume));
             if(res==MT_RET_OK)
                res=gateway_order->VolumeCurrent(SMTMath::VolumeToInt((double)exchange_orders[i].volume));
             //--- set order prices
             if(res==MT_RET_OK)
                res=gateway_order->PriceOrder(exchange_orders[i].price_order);
             if(res==MT_RET_OK)
                res=gateway_order->PriceSL(exchange_orders[i].price_SL);
             if(res==MT_RET_OK)
                res=gateway_order->PriceTP(exchange_orders[i].price_TP);
             //--- set order type
             if(res==MT_RET_OK)
                res=gateway_order->Type(exchange_orders[i].type_order);
             //--- set order expiration type and time
             if(res==MT_RET_OK)
                res=gateway_order->TypeTime(exchange_orders[i].type_time);
             if(res==MT_RET_OK)
                res=gateway_order->TimeExpiration(exchange_orders[i].expiration_time);
             //--- set activation flags for exchange execution
             if(res==MT_RET_OK && m_api_exchange->SymbolGet(exchange_orders[i].symbol,exchange_symbol) && exchange_symbol.exec_mode==ExchangeSymbol::EXECUTION_EXCHANGE)
                res=gateway_order->ActivationFlags(IMTOrder::ACTIV_FLAGS_NO_EXPIRATION|IMTOrder::ACTIV_FLAGS_NO_LIMIT);
             //--- put login to comment
             str.Format(L"%I64u",exchange_orders[i].login);
             if(res==MT_RET_OK)
                res=gateway_order->Comment(str.Str());
             //--- set order setup time
             if(res==MT_RET_OK)
                res=gateway_order->TimeSetup(m_api_gateway->TimeCurrent());
             //--- add order to array
             if(res==MT_RET_OK)
                res=gateway_orders->Add(gateway_order);
             else
                gateway_order->Release();
            }
          else
             res=MT_RET_ERR_MEM;
         }
    //--- return result
       return(res);
      }

A MetaTrader 5 order is created for each external trading system's one by filling its ticket, external system ID, symbol, initial and current volume, prices, type, expiration time and type, adding time, activation flags and comment. Then, the order is added to the list.

Positions are converted using the CGateway::ConvertPositions method.
    
    
    MTAPIRES CGateway::ConvertPositions(const ExchangePositionsArray &exchange_positions,IMTPositionArray *gateway_positions) const
      {
       IMTPosition   *gateway_position=NULL;
       MTAPIRES       res             =MT_RET_OK;
    //--- check
       if(!m_api_gateway || !gateway_positions)
          return(false);
    //--- go through all positions
       for(UINT i=0;i<exchange_positions.Total() && res==MT_RET_OK;i++)
         {
          //--- skip empty positions
          if(exchange_positions[i].volume==0)
             continue;
          //--- get Gateway API position interface
          if((gateway_position=m_api_gateway->PositionCreate())!=NULL)
            {
             //--- set position symbol
             if(res==MT_RET_OK)
                res=gateway_position->Symbol(exchange_positions[i].symbol);
             //--- set position volume
             if(res==MT_RET_OK)
                gateway_position->Volume(SMTMath::VolumeToInt((double)abs(exchange_positions[i].volume)));
             //--- set position action
             if(res==MT_RET_OK)
               {
                if(exchange_positions[i].volume>0)
                   res=gateway_position->Action(IMTPosition::POSITION_BUY);
                else
                   res=gateway_position->Action(IMTPosition::POSITION_SELL);
               }
             //--- set position open price
             if(res==MT_RET_OK)
                res=gateway_position->PriceOpen(exchange_positions[i].price);
             //--- write login to the comment
             if(res==MT_RET_OK)
               {
                CMTStr32 comment;
                comment.Format(L"%I64u",exchange_positions[i].login);
                res=gateway_position->Comment(comment.Str());
               }
             //--- set digits amount
             if(res==MT_RET_OK)
                res=gateway_position->Digits(exchange_positions[i].digits);
             //--- add position to array
             if(res==MT_RET_OK)
                res=gateway_positions->Add(gateway_position);
             else
                gateway_position->Release();
            }
          else
             res=MT_RET_ERR_MEM;
         }
    //--- return result
       return(res);
      }

A MetaTrader 5 position is created for each external trading system's one by filling its symbol, volume, direction, Open price, accuracy and comment. Then, the position is added to the list.

Some data may be lost when synchronizing orders and positions in the MetaTrader 5 platform, for example orders or take profit and stop loss prices not passed to the external system if they are not stored in the external system or not filled by the gateway.  
---  
  
<a id="samplegateway-launch-and-setup"></a>
## SampleGateway Launch and Setup (#samplegateway-launch-and-setup)

To run the gateway sample, compile SampleGateway project and copy the obtained executable file (SampleGateway.exe or SampleGateway64.exe) to gateway\SampleGateway subdirectory of a history server working directory.

After SampleGateway application has been compiled and copied, it is time to configure the gateway. To do this, you should create the gateway configuration and set its parameters. Gateways configuration has been thoroughly described in ["Configuration of Gateways"](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_gateways/gateways_config) section. Gateway configuration includes adding a gateway and trading requests routing setup.

The gateway configuration is performed in the "Gateways" section of MetaTrader 5 Administrator.

![Gateway Setup](images/sample_gateway_common.png)

The following parameters on the "Common" tab must be set:

  * Module \- "SampleGateway" or "SampleGateway64" (according to the necessary bit count of the compiled SampleGateway), if the gateway is to be launched automatically (by a history server). In case a gateway is a remote one, "Remote Gateway" value should be used as a gateway module.
  * ID \- unique dealer identifier, on whose behalf the trading requests will be processed. Requests are routed to the gateway according to this identifier. The value "11" is shown in the provided example.
  * Trading server \- an external trading system server address in "ip:port" format. The default value in SampleGateway is "127.0.0.1:16838".
  * Trading login \- a user ID in an external trading system.
  * Trading password \- a user password in an external trading system.



User ID and password are used only for demonstration purposes in SampleGateway and SampleExchange. Therefore, "Trading login" and "Trading password" fields values may be left blank for this example. In an actual gateway these fields should be filled with the values provided by an external trading system provider.

The clients groups mask must be specified on the "Groups" tab. The gateway will receive trading requests from the clients included into the set groups list.

The mask of trading symbols available to the gateway must be specified on the "Symbols" tab. The gateway will translate quotes and perform trade operations for these symbols. Also, the settings will be automatically updated for them in case of symbols automatic importing Automatic symbols importing must be additionally allowed by enabling "Allow importing symbol settings" option.

![Configuring the symbols](images/sample_gateway_symbols.png)

Trading requests routing should be configured to allow trading requests from the client terminals to start getting to SampleGateway.

Open "Routing" section in the administrator terminal. A new routing rule should be added for SampleGateway. "Process to dealers" value should be set in "Perform action" field on the "Common" tab to allow clients' trading requests to be sent for processing to SampleGateway. Trading instruments mask must be specified in additional conditions ("Where conditions are").

In this example, all trading symbols have been moved to the new "SampleExchange" group from SampleExchange after the initial import. Therefore, "SampleExchange\*" value is specified for "Symbols" condition:

![Configuring routing](images/sample_gateway_routing_common.png)

SampleGateway should be added on "Dealers" tab:

![Configuring routing](images/sample_gateway_routing_dealers.png)

<a id="samplegateway-debugging"></a>
## SampleGateway Debugging (#samplegateway-debugging)

Correct command line corresponding to the gateway parameters should be generated to start debugging. Then the gateway application with the generated command line should be launched using a debugger. The application launch command line is generated based on the gateway settings.

SampleGateway should be created/used to start debugging in the "Gateways" section of the administrator terminal settings. "Remote Gateway" module should be used as the gateway module. Default gateway parameters downloading should be avoided:

![Remote Gateway](images/sample_gateway_remote.png)

When using "Remote Gateway" module, a history server does not launch the gateway process and initiates connection to the address specified in "Gateway server" field. The login and the password specified in "Gateway login" and "Gateway Password" fields are used during the process. Trading servers will also connect to Gateway API server port according to Gateway server, Gateway login and Gateway Password settings.

Parameters with the values equivalent to the settings of the gateway using "Remote Gateway" module should be used in the gateway launch command line:

  * /name: debugged gateway name. This name is used by Gateway API for different purposes. For example, the working directory of the gateway will be created using its name. It is "Sample Gateway" in our case.
  * /address: the gateway server port address, specified in "Gateway server" field at SampleGateway setup stage.
  * /login: login for connecting history and trade servers to SampleGateway, specified in "Gateway login" field.
  * /password: password for connecting history and trade servers to SampleGateway, specified in "Gateway password" field.



After all values have been specified, we will get the resulting parameters line of the gateway application launch:

"/name:Sample Gateway" "/address:127.0.0.1:16641" "/login:100" "/password:default"  
---  
  
Obtained application launch parameter line should be specified in Visual Studio in "Configuration Properties\Debugging" section of the project properties:

![Configuring debugging](images/sample_gateway_debug.png)

To start debugging, you should launch the gateway application using the already configured debugger and allow the gateway operation in MetaTrader 5 Administrator.

When debugging, it should be considered that history and trading servers will connect the gateway application according to the settings specified on "Timeouts" tab of the gateway settings. Reconnection [timeouts](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_gateways/gateways_config) values can be reduced to accelerate the platform servers connection to the gateway application.

<a id="sampleexchange-external-trading-system"></a>
## SampleExchange External Trading System (#sampleexchange-external-trading-system)

SampleExchange application emulating an external trading system operation has been developed to demonstrate SampleGateway trading mechanisms.

The basic functions of SampleExchange are:

  * accepting the client connection of SampleGateway (the application is a demo one and designed to accept only one connection);
  * submitting the settings of trading symbols to SampleGateway;
  * submitting the quote data to SampleGateway;
  * accepting trading requests from SampleGateway and their processing;
  * sending trade requests responses to SampleGateway.



Connection of SampleGateway SampleExchange external trading system has been implemented via sockets.

To launch SampleExchange, you should build SampleExchange project and launch the obtained SampleExchange.exe or SampleExchange64.exe file (depending on the built project bit count). The application is a console-based one accepting command line parameters at the input. The list of available parameters is shown during the application launch with "/?" command line parameter.

The address and the port, at which SampleExchange will wait for the gateway incoming connections, can be explicitly specified using /address:ip:port parameter. The default value is "127.0.0.1:16838".

After SampleExchange has been launched, it will wait for SampleGateway client connection. After the connection has been established, SampleExchange sends the settings of trading symbols to the gateway. After all the symbols have been sent, connection of the gateway and an external trading system is deemed to be synchronized From now on an external system starts sending quote data to the gateway and waits for trading requests from it.

All trading requests are transferred to SampleExchange external trading system by SampleGateway, regardless of their execution mode by a trading symbol.

SampleExchange accepts a trading request and generates a response to it. Bid and ask prices for a symbol, as well as a request processing result are specified in a response. Then it is sent to the gateway. The gateway converts the data from an external trading system format to MetaTrader 5 format and sends a response to a trading request to a client.

Exit SampleExchange application by pressing <Esc>.

Interaction of SampleGateway and SampleExchange external trading system can be observed in the gateway logs:

2012.06.05 08:27:15 GatewayAPI server started on 127.0.0.1:16641  
2012.06.05 08:27:25 127.0.0.1 '100': login (Trade Server build 630)  
2012.06.05 08:27:25 Trade '100': request all executions (received last execution ID with value=0)  
2012.06.05 08:27:25 GatewayAPI '100': try to connect as Main Server while History Server is not connected, waiting for History Server connection  
2012.06.05 08:27:25 127.0.0.1 '100': logout  
2012.06.05 08:27:26 127.0.0.1 '100': login (History Server build 630)  
2012.06.05 08:27:26 127.0.0.1 '100': login (Trade Server build 630)  
2012.06.05 08:27:26 Trade '100': request all executions (received last execution ID with value=0)  
2012.06.05 08:27:26 Gateway 'Sample Gateway' initialized  
2012.06.05 08:27:26 Gateway connecting to exchange server (127.0.0.1:16838)  
2012.06.05 08:27:26 Gateway connected to 127.0.0.1:16838  
2012.06.05 08:27:26 Gateway login successful  
2012.06.05 08:27:26 Gateway synchronized with exchange  
2012.06.05 08:28:48 Gateway '1001': request #13484772 received (prices for EURUSD.TEST 3.00)  
2012.06.05 08:28:48 Trade '100': request #13484772 performed on gateway in 125 ms  
2012.06.05 08:28:48 Gateway '1001': request #13484772 answered - Done  
2012.06.05 08:28:55 Gateway '1001': request #13484773 received (prices for EURUSD.TEST 3.00)  
2012.06.05 08:28:55 Trade '100': request #13484773 performed on gateway in 124 ms  
2012.06.05 08:28:55 Gateway '1001': request #13484773 answered - Done  
2012.06.05 08:28:59 Gateway '1001': request #13484774 received (#112 market buy 3.00 USDCHF.TEST)  
2012.06.05 08:28:59 Trade '100': request #13484774 performed on gateway in 110 ms  
2012.06.05 08:28:59 Gateway '1001': request #13484774 answered - Done  
2012.06.05 08:29:02 Gateway '1001': request #13484775 received (#113 exchange sell 3.00 USDJPY.TEST at market)  
2012.06.05 08:29:02 Trade '100': request #13484775 performed on gateway in 109 ms  
2012.06.05 08:29:02 Gateway '1001': request #13484775 answered - Done  
---
