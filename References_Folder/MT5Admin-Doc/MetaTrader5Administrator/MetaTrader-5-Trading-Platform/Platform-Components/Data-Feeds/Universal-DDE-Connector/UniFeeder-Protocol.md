[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Data Feeds](../../Data-Feeds.md) / [Universal DDE Connector](../Universal-DDE-Connector.md) / UniFeeder Protocol

[Previous](Filtration-of-Quotes.md) | [Next](../../Gateways.md)

# UniFeeder Protocol

The general features of the UniFeeder protocol are provided below to help you understand its operation principles.

  * The data feed establishes TCP connections with a data source.
  * The data feed reads the data line by line. The "\r\n" sequence serves as a line separator.
  * Authorization:
    * After connection is established, the data feed waits for a login request from the data source. The line containing "Login: " is expected, for example, "Login :\n\r". The "waiting login request" entry appears in the Journal while waiting for the request.
    * After the request is received, the "login request received" entry appears in the Journal, and the data feed sends the line with the login to the data source, for example, "user_test\r\n".
    * The data feed waits for the password request from the data source. The line containing "Password: " is expected. The "login sent [%S], waiting password request" entry appears in the Journal while waiting for the request.
    * After the request is received, the "password request received" entry appears in the Journal, and the data feed sends the line with the password to the data source, for example, "password\r\n".
    * The data feed waits for the notification of successful authorization. The line containing "Access granted" is expected. The "password sent, waiting access confirmation" entry appears in the Journal while waiting for the request.
    * After receiving the notification, the "Login: '%S' successful" entry appears in the Journal.
    * The data feed sends the line containing the symbols, for which it is allowed to send quotes. The line looks as follows "> Symbols:USDRUB,EURUSD,EURRUB\r\n".
    * The data feed switches to the data receipt mode (quotes and news).
  * Data receipt:
    * The data feed reads the data line by line. The "\r\n" serves as a line separator.
    * The lines beginning with ">" or "<" reserved characters are skipped, except for the lines beginning with "< News".
    * If the "< News\r\n" line is received, the data feed switches to news receipt mode:
      * After the "< News\r\n" line, the data feed reads the NewsTopic structure (read MetaTrader 4 API documentation for more details).
      * Next, the data feed reads the news body. The size of the news body is set in bytes in the NewsTopic::len field.
      * After reading the body, the news is sent to the platform, while the data feed continues the data receipt.
    * If the line does not begin with "<" or ">", it is deemed to be a tick line.
      * The tick line format: "<Symbol name> <bid> <ask>\r\n". Example: "USDJPY 1.0106 1.0099\r\n".
      * If bid or ask is less than zero, or bid exceeds ask, the tick is skipped and the "failed to parse tick, invalid bid/ask" entry appears in the Journal.



Below is an example of the network exchange dump. The data sent by the data feed is shown in red:
    
    
    Welcome
    Login: test_user
    Password: test_password
    Access granted
    USDJPY 0 4.0000 19.0000
    GBPUSD 0 8.0000 19.0000
    USDCHF 0 15.0000 16.0000
    USDCHF 0 6.0000 25.0000
    USDJPY 0 6.0000 17.0000
    GBPUSD 0 6.0000 21.0000
    USDCHF 0 7.0000 24.0000
    USDJPY 0 9.0000 14.0000
    GBPUSD 0 9.0000 18.0000
    USDCHF 0 9.0000 22.0000
    USDJPY 0 5.0000 18.0000
    GBPUSD 0 4.0000 23.0000
    USDCHF 0 7.0000 24.0000
    USDJPY 0 7.0000 16.0000
    GBPUSD 0 13.0000 14.0000
