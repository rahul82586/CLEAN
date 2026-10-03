[🏠 Document Start](../README.md) / [MetaTrader 5 Trading Platform](../MetaTrader-5-Trading-Platform.md) / Additional Features

[Previous](Technical-Support.md)

<a id="additional-features"></a>
# Additional Features (#additional-features)

This section describes additional features of the components of the MetaTrader 5 trading platform:

  * [URL Schemes (#scheme)](Additional-Features.md#scheme)
  * [Marketing Campaigns (#lead)](Additional-Features.md#lead)



<a id="scheme"></a>
## URL Schemes (#scheme)

Mobile terminals [MetaTrader 5 for iPhone](https://download.mql5.com/cdn/mobile/mt5/ios?hl=ru&utm_campaign=download&utm_source=metatrader5.help "iPhone") and [MetaTrader 5 for Android](https://download.mql5.com/cdn/mobile/mt5/android?hl=ru&utm_campaign=download&utm_source=metatrader5.help "Android")support the Deep Linking technology. This technology allows using links that bring users to a specified location within a mobile app.

For example, quick account connection links can be added to registration emails and to the trader's room on the website. A click on this link opens a trader's mobile terminal with the selected account connection section, in which the account number and server are automatically specified. The trader will only need to enter a password.

Launch of the application and navigation to the selected section is implemented through links starting with metatrader5://... . The part of link before "://" is called [a URL scheme](https://en.wikipedia.org/wiki/URL). 

> The metatrader5 URL scheme is registered in the operating system of the mobile device during terminal installation. If the terminal is not installed, the links will not open.

The general scheme of links:

metatrader5://path?par1=val1&...&parN=valN  
---  
  
where:

  * 'path' is the destination section of the application
  * par is the list of parameters



<a id="connection-to-a-specified-account-on-the-server"></a>
### Connection to a specified account on the server (#connection-to-a-specified-account-on-the-server)

The link should contain the application section, to which you want to link your traders, as well as the 'login' and 'server' parameters containing the account number and the name of the server to connect to. Example:

metatrader5://account?login=123456&server=MetaQuotes-Demo  
---  
  
Upon a click on such a link, the MetaTrader 5 app starts and tries to connect to the specified account. If the account already exists in the terminal and its password has been saved, connection is performed successfully. Otherwise, the account connection form is shown with the account and server already specified, and a user is prompted to enter the password. A server name should exactly match the name in the White Label.

  * If the server name is not specified, the server of the current account or of the first account from the list will be used.
  * If the account number is not specified, and the server name is specified, any account from the specified server will be selected. If there are no such accounts, the scheme will not be executed.
  * If both the account and the server are not specified, the current account or the first account from the list will be used.



<a id="link-to-a-specified-section"></a>
### Link to a specified section (#link-to-a-specified-section)

In order to forward users to the specified section, specify the appropriate 'path' value in the link:

metatrader5://<path>?login=123456&server=MetaQuotes-Demo  
---  
  
After <path>, you can specify the account number and the server name, to which the terminal should connect before opening the section. If the account or server is not specified, the connection rules described above apply.

  * account — no specific section will be opened, it is used for connection to a specified account and server.
  * marketwatch — quotes. The example contains the additional 'symbols' parameter, in which financial instruments to be displayed in the window are specified.



metatrader5://marketwatch?server=MetaQuotes-Demo&symbols=USDRUB,EURRUB,GOLD,XAUUSD,%23DIS,%23IBM  
---  
  
  * chart/symbol/period is a chart with the specified symbol and timeframe, e.g.:



metatrader5://chart/XAUUSD/H1?server=MetaQuotes-Demo  
---  
  
  * trade — Trade tab, the list of open positions and orders, e.g.:



metatrader5://trade?server=MetaQuotes-Demo  
---  
  
  * trade/symbol — a trade dialog, from which a trading operation on the specified symbol can be performed, e.g.:



metatrader5://trade/SILVER?server=MetaQuotes-Demo&login=1145990  
---  
  
> Illegal characters in URI links must be encoded. For example, the #GOOG must be specified as %23GOOG. Names of financial instruments are case sensitive.

<a id="extra-parameters"></a>
### Extra parameters (#extra-parameters)

It is possible to specify additional parameters for each deep linked section:

  * 'login' and 'server' can be used for connection with the specified account number and server name.
  * symbols — one or more symbols separated by commas, which should be added to the Quotes section after connection to an account defined by the 'login' and 'server' parameters. Illegal characters in URI links must be encoded. For example, the #GOOG must be specified as %23GOOG. Names of financial instruments are case sensitive. Symbols passed do not replace those already displayed in the "Quotes" section, they are added in the current list.


  * account_type — run the demo or real account opening wizard on the first application start. 1 is used for demo accounts and 2 for real ones. To use this feature, you should correctly specify [account allocation settings](Platform-Setup/Accounts/Account-Allocation-Settings.md). If the required group for opening an account is not found, the wizard will not run.



> Further information is provided in the article "[Deep Linking to MetaTrader mobile terminals and to their selected parts](https://support.metaquotes.net/en/articles/433)"

<a id="lead"></a>
## Marketing Campaigns (#lead)

The client record contains two special fields in the trading platform: [Lead Source (#leadsource)](Platform-Setup/Accounts/Editing-Account.md#leadsource) and [Lead Campaign (#leadsource)](Platform-Setup/Accounts/Editing-Account.md#leadsource). They are used for marketing campaigns allowing you to track where a client came from. To receive the data, add the following labels to the client or mobile platform download link:

https://download.mql5.com/cdn/web/metaquotes.ltd/mt5/mt5setup.exe?utm_source=YourWebsite&utm_campaign=YourCampaign  
https://download.mql5.com/cdn/mobile/mt5/ios?server=ABC-Demo,ABC-Real&utm_source=YourWebsite&utm_campaign=YourCampaign  
https://download.mql5.com/cdn/mobile/mt5/android?server=ABC-Demo,ABC-Real&utm_source=YourWebsite&utm_campaign=YourCampaign  
---  
  
where YourCampaign is a campaign name, while YourWebsite is a website the link has been placed at. In the 'server' parameter of the mobile platform links, enter the list of your servers to be shown to traders when they open an account.

When opening a demo account and connecting to any trading account via the terminal downloaded using such a link, utm_source and utm_campaign values are set in a client record at the server side. If the fields are already filled, the label values are not overwritten when re-connecting to the account (even if the terminal used for connection was downloaded by a link containing other labels).

> Lead Source and Lead Campaign data from terminal download links can be written to created accounts only if the broker has a [Finteza license](Platform-Setup/Integrations/Finteza-Analytics.md).
