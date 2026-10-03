[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [Gateways](../Gateways.md) / Borsa Istanbul

[Previous](FXCM-PRO.md) | [Next](Interactive-Brokers.md)

<a id="metatrader-5-gateway-to-borsa-istanbul-futures"></a>
# MetaTrader 5 Gateway to Borsa Istanbul Futures (#metatrader-5-gateway-to-borsa-istanbul-futures)

[Borsa İstanbul](https://borsaistanbul.com/) brings together all exchanges operating in the Turkish capital markets under a single roof. Established on the basis of Capital Markets Law no. 6362, Borsa İstanbul is an internal entity under private law. Borsa İstanbul is a self-regulatory entity.

Borsa İstanbul offers the opportunity to invest in various products in an organized, transparent and reliable trading environment to local and international investors with its modern technological capabilities. On all markets of Borsa İstanbul, transactions are conducted electronically, and market information is disseminated on a real-time basis.

Borsa İstanbul markets are organized under five main categories: Equity Market, Emerging Companies Market, Debt Securities Market, Foreign Securities Market and Futures and Options Market.

MetaTrader 5 Gateway to Borsa Istanbul Futures allows futures trading at the Main Board of [Futures and Options Market](https://borsaistanbul.com/en/products-and-markets/markets/futures-and-options-market) at [Borsa Istanbul](https://borsaistanbul.com/):

  * Equity Futures (Main Board)
  * Equity Index Futures (Main Board)
  * Currency Futures (Main Board)
  * Precious Metals Futures (Main Board)
  * Commodity Futures (Main Board)
  * Power Futures (Main Board)



> [Request MetaTrader 5 Gateway to Borsa Istanbul Futures](https://support.metaquotes.net/en/market/product/282)

<a id="preparing-for-the-gateway-launch"></a>
## Preparing for the Gateway Launch (#preparing-for-the-gateway-launch)

Before setting a brokerage company gateway, configure the virtual network channel to be able to connect to Borsa Istanbul servers.

Configuration of a virtual network channel is performed together with Borsa Istanbul technical specialists. To create a virtual channel to the exchange, a broker must request technical requirements and recommendations for connection to the Borsa Istanbul virtual private network (VPN) from the mercantile exchange technical support team. At the next stage the mercantile exchange technical support team will submit to the brokerage company description of the equipment settings on SMX side: tunnel type, data encryption method, data encryption keys etc.

The programmed virtual channel can be created for connection to Borsa Istanbul test environment.

<a id="how-the-gateway-works"></a>
## How the Gateway works (#how-the-gateway-works)

MetaTrader 5 Gateway to Borsa Istanbul Futures is a separate BorsaIstanbulVIOPGateway64.exe module that uses the MetaTrader 5 Gateway API. The gateway operates over 5 FIX channels. One FIX connection is used for passing Reference Data (symbol settings), two more are used for trading and the other two for receiving data on trades performed via other trading systems (Drop Copy). Some symbols are processed on the one and Drop Copy connection, the rest symbols are handled on the other one. Information about what servers process specified symbols is transmitted via the Reference Data channel.

Orders and positions are synchronized over the SOAP service, and quotes are delivered via a TIP channel.

Orders are sent to the MetaTrader 5 Gateway to Borsa Istanbul for processing in accordance with configured [routing rules (#routing)](Borsa-Istanbul.md#routing). Processing of requests depends on the type of the order:

Order Type | Execution  
---|---  
Market Orders | Delivered directly to the exchange as a market order.  
Buy Limit Sell Limit | Delivered directly to the exchange as limit orders.  
Buy Stop Sell Stop | Delivered directly to the exchange as stop orders.  
Buy Stop Limit Sell Stop Limit | Delivered directly to the exchange as stop limit orders.  
Take Profit Stop Loss | Processed on the MetaTrader 5 side. After activation in the MetaTrader 5 terminal, a market order to close a client's position is sent to the exchange.  
Stop Out | Processed on the MetaTrader 5 side. In case a limit order must be removed after a Stop out level has been reached, an appropriate request for its removal is sent to Borsa Istanbul server. In case a position must be closed because of Stop out, a market request to close a client's position is sent to the exchange.  
  
The below diagram shows the interaction of the gateway with the exchange (the exchange time UTC+3 is specified):

![MetaTrader 5 and Gateway interaction scheme](images/borsa_scheme.png)

  * The gateway starts to connect to FIX servers of the exchange at 4:30 . It will try to obtain from the exchange actual files with risk parameters till 22:30. When new files appear, the gateway downloads them and updates symbol settings in MetaTrader 5.
  * Clients' balances are synchronized with the exchange at 9:00by default. This time can be changed using the BalancesSyncTime parameter.
  * The trading session lasts from 9:30 to 18:30.
  * The exchange updates official exchange rates at 15:30. These rates are used to recalculate the value of contracts that are not expressed in Turkish liras: the symbol's tick value is calculated and set based on these rates. New rates are not applied until the end of the trading session (previous rates are used).
  * During the time specified in the [EOD Time (#eod-time)](Borsa-Istanbul.md#eod-time) parameter, the gateway downloads new rates from the exchange and recalculates results of all trades executed during this session using the new rates.
  * Immediately after this, the gateway receives the EOD file from the exchange. Results of all trades executed from 15:30 until the end of the session are recalculated using new currency rates. Update of risk parameters of instruments, as well as of inter-month and inter-contract [spreads](../../Platform-Setup/Spreads.md), calculation of variation margin, delivery (closing of positions of expired futures) and unblocking of accumulated profits are performed based on the EOD file.
  * If PositionsSync parameter is enabled, positions are synchronized at 19:01 (after applying the EOD file).
  * At 22:30, the gateway is disconnected from the exchange's FIX servers.



<a id="settings"></a>
## Configuring the gateway (#settings)

To start working, add [a new gateway configuration](../../Platform-Setup/Gateways.md):

![Gateway settings](images/borsa_common.png)

Set the following parameters on the "Common" tab:

  * ID — unique dealer identifier, on whose behalf the trade requests will be processed. Requests are routed to the gateway according to this identifier.
  * Module — specify BorsaIstanbulVIOPGateway64 and accept the default settings after the module selection.
  * Trading server — IP address and the port of the exchange's first FIX server, where trade requests are processed.
  * Trading login — a login for connection to the first trade server of the exchange. Corresponds to the UserName (553) tag in the FIX protocol.
  * Password — a password for connection to the first trade server of the exchange. Corresponding to the Password tag (554) in FIX protocol. The exchange requires that the password used for connection be changed every 90 days. The gateway automates this process by changing the password in advance, every 70 days, in case of unforeseen issues. To activate this feature, change the password manually once. This action will provide the gateway with the last password change date, from which further tracking will be performed.



  * ID value must be unique in the field of manager logins and gateway identifiers.
  * Connection details are provided by the exchange.

  
---  
  
Now, go to the "Parameters" tab.

![Gateway parameters setup](images/borsa_param.png)

Specify the following parameters values here:

  * FIX Trade SenderCompID — a standard parameter of the FIX messages header used for a data sender identification. This parameter is provided by the exchange as the value of SenderCompID (49).
  * FIX Trade TargetCompID — a standard parameter of the FIX messages header used for trading messages recipient identification. This parameter is provided by the exchange as the value of TargetCompID (56).
  * FIX Trade SenderSubID — FIX messages header standard parameter used for a trading participant (a legal entity) identification. This parameter is provided by the exchange as the value of SenderSubID.
  * FIX Trade Second Address — IP address and the port of the exchange's second FIX server, where trade requests are processed.
  * FIX Trade Second Login — a login for connection to the second trade server of the exchange. Corresponds to the UserName (553) tag in the FIX protocol.
  * FIX Trade Second Password — a password for connection to the second trade server of the exchange. Corresponding to the Password tag (554) in FIX protocol.
  * FIX Trade Second SenderCompID — a standard parameter of the FIX messages header used for a data sender identification. This parameter is provided by the exchange as the value of SenderCompID (49).
  * FIX Trade Second TargetCompID — a standard parameter of the FIX messages header used for trading messages recipient identification. This parameter is provided by the exchange as the value of TargetCompID (56).
  * FIX Trade Second SenderSubID — FIX messages header standard parameter used for a trading participant (a legal entity) identification. This parameter is provided by the exchange as the value of SenderSubID.
  * FIX Drop Copy Address — the IP and port of the first Drop Copy server. Operations performed via other trading systems are processed on this FIX server.
  * FIX Drop Copy Login — login for connection to the first Drop Copy server of the exchange. Corresponds to the UserName (553) tag in the FIX protocol.
  * FIX Drop Copy Password — password for connection to the first Drop Copy server of the exchange. Corresponding to the Password tag (554) in FIX protocol.
  * FIX Drop Copy SenderCompID — a standard parameter for the FIX message header, which is used for identifying a data sender in the Drop Copy service. This parameter is provided by the exchange as the value of SenderCompID (49).
  * FIX Drop Copy TargetCompID — a standard parameter for the FIX message header, which is used for identifying a message recipient in the Drop Copy service. This parameter is provided by the exchange as the value of TargetCompID (56).
  * FIX Drop Copy SenderSubID — a standard parameter for the FIX messages header, which is used for a trading participant (a legal entity) identification in the Drop Copy service. This parameter is provided by the exchange as the value of SenderSubID.
  * FIX Drop Copy Third Address — IP-address and port of the third Drop Copy server. This is the exchange's FIX server which processes operations executed through other trading systems.
  * FIX Drop Copy Third Login — login for connection to the exchange's third Drop Copy server. Corresponds to the UserName tag (553) in the FIX protocol.
  * FIX Drop Copy Third Password — password for connection to the exchange's third Drop Copy server. Corresponds to the Password tag (554) in the FIX protocol.
  * FIX Drop Copy Third SenderCompID — standard FIX message header parameter which is used to identify the trading data sender. This parameter is provided by the exchange as the SenderCompId (49) value.
  * FIX Drop Copy Third TargetCompID — standard FIX message header parameter which is used to identify the recipient of trading messages. This parameter is provided by the exchange as the TargetCompId (56) value.
  * FIX Drop Copy Third SenderSubID — standard FIX message header parameter which is used to identify a trading participant (legal entity). This parameter is provided by the exchange as the SenderSubId value.
  * FIX Drop Copy Fourth * — a set of parameters for the fourth Drop Copy server: Address, Login, Password, SenderCompID, TargetCompID and SenderSubID. They are set similarly to the third server parameters.
  * FIX Drop Copy Fifth * — a set of parameters for the fifth Drop Copy server: Address, Login, Password, SenderCompID, TargetCompID and SenderSubID. They are set similarly to the third server parameters.
  * FIX Drop Copy Sixth * — a set of parameters for the sixth Drop Copy server: Address, Login, Password, SenderCompID, TargetCompID and SenderSubID. They are set similarly to the third server parameters.
  * FIX Reference Data Address — IP address and port of the exchange's FIX server, through which trade symbol settings are transmitted (the Reference Data server).
  * FIX Reference Data Login — login for connection to the Reference Data server. Corresponds to the UserName (553) tag in the FIX protocol.
  * FIX Reference Data Password — password for connection to the Reference Data server. Corresponding to the Password tag (554) in FIX protocol.
  * FIX Reference Data SenderCompID — a standard parameter for the FIX message header, which is used for identifying a data sender in the Reference Data service. This parameter is provided by the exchange as the value of SenderCompID (49).
  * FIX Reference Data TargetCompID — a standard parameter for the FIX message header, which is used for identifying a message recipient in the Reference Data service. This parameter is provided by the exchange as the value of TargetCompID (56).
  * FIX Reference Data SenderSubID — a standard parameter for the FIX messages header, which is used for a trading participant (a legal entity) identification in the Reference Data service. This parameter is provided by the exchange as the value of SenderSubID.


  * FIX Reference Data Detached — by default, when any of the FIX connections is interrupted, the gateway completely disconnects from the exchange to avoid data integrity violation. The settings of trading instruments transmitted through the FIX Reference channel are updated not very often. Therefore, in some cases, the loss of this connection can be disregarded. To prevent the gateway from disconnecting from the exchange upon losing the FIX Reference Data connection, set "FIX Reference Data Detached" to "No".


  * FIX Connect Attempts — the maximum number of attempts to connect to the current IP address of the FIX channel (Trade, Drop Copy, or Reference). The default value is three. After the specified number of unsuccessful attempts, the gateway will try to connect to the next address.


  * FIX Trade SMPLevel — value of tag 21114 in the FIX protocol. Possible values: 'Within' (default) and 'Across'. The value is used along with FIX Trade SMPMethod and FIX Trade SMPID for [Self-Match Prevention Feature](https://borsaistanbul.com/files/self-match-prevention-smp-feature-technical-functionality-principles.pdf), an algorithm that prevents the matching of orders of the same client. Please contact the exchange to find out the required parameter values.
  * FIX Trade SMPMethod — value of tag 21115 in the FIX protocol. Possible values: Aggressive (default), Passive, Both.
  * FIX Trade SMPID — value of tag 21116 in the FIX protocol. If this parameter is not filled, the gateway will not transmit the SMPLevel (21114) and SMPMethod (21115) values.


  * TIP Address — IP address and port of the exchange server, through which quotes are transmitted over the TIP protocol.
  * Nasdaq Identifiers Path — path to the file containing identifiers of instruments in the TIP channel. It is used for the gateway to exchange connection in the middle of the trading session.
  * Nasdaq Identifiers Enabled — enable\disable processing of the file specified in the Nasdaq Identifiers Path parameter. Default is No. At the beginning of the day, the exchange send over the TIP protocol information about symbol identifiers (identifier/symbol name pairs). Further quotes are provided only with an identifier (without a name). To enable the gateway to receive quotes after connecting to Borsa Istanbul in the middle of the trading session, enable this option. The gateway will load the identifiers from the file specified in Nasdaq Identifiers Path.
  * Symbols Path — path for importing the exchange symbols. By default, if this parameter is absent, the gateway imports the exchange's trading symbols to \Preliminary subdirectory with trading ability disabled. A system administrator should manually relocate imported symbols to the proper group and allow trading for them. If this parameter is present, the gateway imports trading symbols following the specified path. The ability to trade the symbols is enabled immediately. Thus, the administrator has no need to additionally configure the symbols. For example, if "BorsaIstanbul" is specified in the parameter, working symbols will be automatically added to the BorsaIstanbul\* subdirectory, and expired symbols will be transferred to BorsaIstanbul\Expired\*.
  * Takas Web Service Address — the address of the server that transmits data for synchronizing client balance positions on the MetaTrader 5 side (the SOAP service).
  * Takas Web Service Login — login for connection to the SOAP service (provide by the Exchange).
  * Takas Web Service Password — password for connection to the SOAP service (provide by the Exchange).
  * Takas Web Service Member Code — trading participant code, which should be specified for connecting to the SOAP service (provide by the Exchange).
  * Genium Risk Parameters Url — the address for downloading files with risk parameters. These files are used for obtaining current settlement prices, for updating risk parameters of instruments, for calculating the variation margin and for updating the inter-month and inter-contract spreads of instruments.
  * Positions Sync — enable\disable synchronization of positions with the SOAP service at the end of the trading session. Enabled by default (set to Yes).
  * Balances Sync — enable\disable synchronization of client balances with the SOAP service at the end of the trading session. Enabled by default (set to Yes).
  * Balances SyncTime — the start time of balance synchronization with SOAP. Synchronization starts at 09:00 by default.
  * Daily Rollover Positions — enable (Yes)\disable (No) rollover operations (charging variation margin) at the end of the trading session. Enabled by default (set to Yes).


  * Settlement Prices File Path — full path to the CSV file with settlement prices. The file must be UTF-8 encoded and prices must be in X,YYY format (for example, 1,234). By default, the path is not specified, and the gateway receives prices from the FIX Reference Data channel or from the 'span' file. If the path is specified, the gateway checks the date when the file was last modified. If the file has been modified on the current day, its contents are read and applied. If the file has not been modified, the gateway will use prices from the FIX Reference Data channel or from the 'span' file. If the file does not contain data for certain instruments, the relevant data will be taken from the FIX Reference Data channel or from the 'span' file.
  * EOD Time — end-of-day time on the exchange. Variation margin operations are performed at this time, and not upon the [receipt of the "EOD span" file (#schedule)](Borsa-Istanbul.md#schedule). The parameter is set as "HH:MM". Valid values are from 18:30 (end of the afternoon session) to 18:59 (beginning of the evening session). The default time is 18:52.


  * Trade Requests Limit — the maximum total number of requests sent to the exchange per second. Default is 0, which means there is no limit.
  * Client Trade Requests Limit — the maximum number of requests per second sent by each separate client to the exchange. Default is 0, which means there is no limit.
  * Quotes Delay — delay of transmitted quotes in seconds. The maximum duration of quotes delay is 20 minutes (1200 seconds). The flow of delayed quotes is neither thinned out, nor changed. A quote is passed to MetaTrader 5 History Server only after the expiration of delay period since the quote has arrived to Gateway API. If the temporary delay parameter is not defined, the quote delay is not used. Changes in depth of market and price statistics are delayed together with the quotes flow.
  * Quotes Tickstats Sample — the minimum frequency of sending price statistics in milliseconds. This parameter allows thinning out updates of price statistics reducing the traffic.
  * Quotes Ticks Sample — the minimum frequency of sending quotes in milliseconds. This parameter allows thinning out updates of quotes reducing the traffic. It is recommended for use on demo servers only.
  * Quotes Books Sample — the minimum frequency of depth of market updates in milliseconds. This parameter allows thinning out updates of the depth of market reducing the traffic. It is recommended for use on demo servers only.
  * Stop Out Allow — allow closing of positions upon reaching [Stop Out (#stopout)](../../Platform-Setup/Groups/Group-Settings.md#stopout). If set to "No" (default), positions opened via the gateway will not be closed automatically, if Stop Out is reached on the trading platform side. If a position is opened with Stop Out Allow = Yes, then closing by Stop Out can occur even if you change the parameter value to "No". It is only guaranteed that the ban to close will be effective for positions opened after changing the parameter value to "No".



Two addresses are supported for each FIX channel: primary and secondary. You can specify them separating by commas. For example: FIX Drop Copy Address = 31.145.34.115:30187,31.145.34.115:10030. If the gateway fails to connect to the first address, it will automatically switch to the second one.

The gateway supports the old and new exchange environments: BISTECH 2 and BIST 3.0, respectively. The parameters below are only used to connect to the old environment. If they are filled, the following parameter groups will be ignored: FIX Drop Copy Third *, FIX Drop Copy Fourth *, FIX Drop Copy Fifth * and FIX Drop Copy Sixth *.

  * FIX Drop Copy Second Address — IP address and port of the second Drop Copy sever. This is the exchange's FIX server which processes operations executed through other trading systems.
  * FIX Drop Copy Second Login — login for connection to the exchange's second Drop Copy server. Corresponds to the UserName tag (553) in the FIX protocol.
  * FIX Drop Copy Second Password — password for connection to the exchange's second Drop Copy server. Corresponds to the Password tag (554) in the FIX protocol.
  * FIX Drop Copy Second SenderCompID — standard FIX message header parameter which is used to identify the trading data sender. This parameter is provided by the exchange as the SenderCompId (49) value.
  * FIX Drop Copy Second TargetCompID — standard FIX message header parameter, which is used to identify the recipient of trading messages. This parameter is provided by the exchange as the TargetCompId (56) value.
  * FIX Drop Copy Second SenderSubID — standard FIX message header parameter which is used to identify a trading participant (legal entity). This parameter is provided by the exchange as the SenderSubId value.



The next stage is to specify the groups of clients, whose requests will be processed via the MetaTrader 5 Gateway to Borsa Istanbul, as well as symbols, by which the gateway processes trading operations and broadcasts quotes.

![Configuring groups and symbols](images/borsa_groups_symbols.png)

Make sure to enable the "Allow importing symbol settings" option. The gateway imports symbols from the exchange to the MetaTrader 5 platform in accordance with the [Symbols Path (#symbolspath)](Borsa-Istanbul.md#symbolspath) parameter and further controls parameters of these symbols.

> The gateway supports conversion of symbols and quotes. For details, please view the [Symbol and Price Translation](../../Platform-Setup/Gateways/Symbol-and-Price-Translation.md) section.

<a id="groups-configuration-and-using-profitloss-for-the-current-trading-session"></a>
## Groups Configuration and Using Profit/Loss for the Current Trading Session (#groups-configuration-and-using-profitloss-for-the-current-trading-session)

According to the exchange rules, profit obtained during a trading day cannot be used before clearing is performed. In fact, only clearing determines the financial results of all transactions during the day. The profit received by a client during the current trading session is accumulated during the trading session and released only after the clearing becoming available for use by the client for further trade.

In order to avoid a situation in which a client who suffered losses will try to continue trading, fixed loss is withdrawn immediately.

In this regard, the following parameters should be specified in "Profit/loss in free margin" block of Margin tab in the settings of the group that will operate at Borsa Istanbul:

![Group configuration](images/borsa_margin.png)

All financial accounting on Borsa Istanbul is done in Turkish liras. Thus, Turkish liras (TRY) should be specified as deposit currency in the group settings:

![Group configuration](images/borsa_group_common.png)

<a id="routing"></a>
## Configuring Trade Requests Routing (#routing)

Configure the routing to let the clients requests to be transmitted to the Borsa Istanbul Futures gateway. To do this, add a routing rule to the relevant [MetaTrader 5 Administrator](../../Platform-Setup/Routing.md) section.

Select "Process to dealers" as an action in common settings. Assign this routing rule for all requests and orders. In additional conditions, indicate groups of clients, whose requests will be passed to the gateway.

In the screenshots below all orders created by users in the real\borsa\* groups by symbols from the BorsaInstanbul\* section will be sent to the gateway for processing.

![Configuring Trade Requests Routing](images/borsa_routing.png)

<a id="configuring-trading-accounts"></a>
## Configuring Trading Accounts (#configuring-trading-accounts)

Each client on MetaTrader 5 side should be provided with a corresponding separate trading account on the exchange. After an account is opened at the exchange, it should be connected with the account within the platform. Open the appropriate client account and move to Account tab:

![Configuring Trading Accounts](images/borsa_account.png)

A new entry should be added in "Trade accounts" section. Select MetaTrader 5 Gateway to Borsa Istanbul in Gateway ID field. Specify the Borsa Istanbul client account in "Account" field.

<a id="gateway-launch"></a>
## Gateway Launch (#gateway-launch)

After the application of all settings described above, your gateway is almost ready to go. It will connect to Borsa Istanbul server.

Borsa Istanbul submits a default password for the first connection (specified in the [Trading Password (#password)](Borsa-Istanbul.md#password) field). Borsa Istanbul security policy requires the password to be changed right after the first connection. The gateway automatically generates and installs the new password. You can [change the password (#change-password)](Borsa-Istanbul.md#change-password) later.

The password should meet Borsa Istanbul safety requirements:

  * the password should consist of 8 characters;
  * the password should contain 3 types of symbols: lowercase Latin characters (a-z), upper case ones (A-Z), numbers (0-9);
  * the password must be different from the previous ones (last 6 used passwords are checked).



The following entries appear in the gateway journal when the password is changed automatically:

12:23:48 Gateway new password has generated due to previous logon response  
---  
  
The following entry means that the gateway has successfully connected to Borsa Istanbul and is now ready for operation:

12:24:19 Gateway synchronized with Borsa Istanbul exchange  
---  
  
In case of connection failure, the entries concerning the failure reasons appear in the gateway journal.

New symbols are imported after the first connection. As noted above, after adding new symbols, trading should be enabled for them. After that the MetaTrader 5 platform main trade server must be restarted. These actions should be performed only during the gateway first launch.

After the main trading server is restarted, the gateway installation and configuration is complete. Traders can perform transactions on Borsa Istanbul using their MetaTrader 5 client terminal.

<a id="updating-the-symbols-settings"></a>
## Updating the Symbols Settings (#updating-the-symbols-settings)

The gateway automatically updates the symbols settings during its operation, if necessary. Appropriate entries appear in the journal in that case:

12:25:36 SymbolsBase symbol 'F_EURUSD1213S0' config updated  
---  
  
<a id="change-password"></a>
## Changing the Password (#change-password)

In case you need to change the password used by the gateway for connection to Borsa Istanbul server, simply specify the new password in Trading password field. The password must comply with [security requirements (#passwod-security)](Borsa-Istanbul.md#passwod-security). Once the settings are saved, the password at Borsa Istanbul server will be changed automatically.

12:25:48 Gateway password has been changed manually  
---
