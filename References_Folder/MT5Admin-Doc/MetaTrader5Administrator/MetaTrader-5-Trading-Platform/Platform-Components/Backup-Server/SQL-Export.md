[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [Backup Server](../Backup-Server.md) / SQL Export

[Previous](Restoring-Server.md) | [Next](SQL-Export/Installation-and-Setup-of-MySQL.md)

# SQL Export

The MetaTrader 5 trading platform provides standard options for the real-time data export to MySQL, Microsoft SQL Server, FireBird, Oracle, MariaDB and PostgreSQL databases. This option enables the quick and easy deployment of data export to an external DBMS for using the platform data in any popular programming language and third-party applications. Thus, it is possible to create an intermediate layer between a trade server and broker's program services that regularly access trading data. This reduces the load on the trade server when it receives the current trading data.

The export function is enabled by simple specification of [settings for connection to DBMS (#sql)](../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#sql) via MetaTrader 5 Administrator. After that, the backup server will immediately perform an initial synchronization of data from the DBMS. Further, new data will be exported to the DBMS in real time. The following data is exported:

  * Information about clients (general information and trading status)
  * Current active orders and positions
  * The history of orders and deals
  * Current prices
  * Virtually all settings of the trading platform (except for the working time, synchronization and spreads)



The description of installation and setup of popular databases is provided in appropriate subsections:

  * [MySQL Server 5.7](SQL-Export/Installation-and-Setup-of-MySQL.md) (supported versions: 5.1, 5.5, 5.6, 5.7, 8.0, 8.1)
  * [MariaDB 10.2](SQL-Export/Installation-and-Setup-of-MariaDB.md) (all version supported)
  * [Microsoft SQL Express 2012](SQL-Export/Installation-and-Setup-of-MS-SQL.md) (supported versions: 2005, 2008, 2008 R2, 2012, 2014, 2016, 2017, 2019, 2022)
  * [Oracle Database Express Edition 11g](SQL-Export/Installation-and-Setup-of-Oracle.md) (supported versions: 11g/11g Express Edition, 12c, 18c, 19c, 21c, 23ai)
  * [PostgreSQL](SQL-Export/Installation-and-Setup-of-PostgreSQL.md) (supported versions: 8.4 — 17)



## Operation Principle

Export mechanism has been implemented on the side of backup servers replicating data from the trade servers.

Below are the general steps of synchronization in a backup server:

  * The backup server connects to the appropriate trade server and is synchronized with it.
  * After synchronization with the trade server is successfully complete, the backup server synchronizes an external DBMS.
  * The backup server applies changes to its databases and the external DBMS via transactions from the trade server.



The backup server performs initial synchronization based on time stamps (Timestamp field in the tables) during each connection to DBMS:

  * All logs with different time stamps in the external DBMS are replaced with backup server logs.
  * All entries that are absent at the backup server are removed from the external DBMS.



> A time stamp is used for checking the identity of the backup and the external DBMS logs. If a time stamp on the backup is similar to the on at the external DBMS, a backup server considers that all other log fields are similar and the log update is not required.

After databases are synchronized, the backup server applies change transactions on the external DBMS. Besides, prices and profit values for active orders (mt5_orders), positions (mt5_positions) and related trading accounts (mt5_accounts) are also periodically updated.

A detailed description of exported tables can be found in the following subsections:

  * [mt5_symbols](SQL-Export/mt5-symbols.md) — [symbols'](../../Platform-Setup/Symbols.md) configurations.
  * [mt5_symbols_sessions](SQL-Export/mt5-symbols-sessions.md) — symbols' [trade and quotation sessions](../../Platform-Setup/Symbols/Symbol-Settings/Sessions.md).
  * [mt5_groups](SQL-Export/mt5-groups.md) — [groups'](../../Platform-Setup/Groups.md) configurations.
  * [mt5_groups_symbols](SQL-Export/mt5-groups-symbols.md) — individual [symbol settings for groups](../../Platform-Setup/Groups/Group-Symbol-Settings.md).
  * [mt5_commissions](SQL-Export/mt5-commissions.md) — [commission](../../Platform-Setup/Groups/Commission-Settings.md) settings for groups.
  * [mt5_commissions_tiers](SQL-Export/mt5-commissions-tiers.md) — [commission level (#level)](../../Platform-Setup/Groups/Commission-Settings.md#level) settings.
  * [mt5_managers](SQL-Export/mt5-managers.md) — [manager](../../Platform-Setup/Managers.md) accounts.
  * [mt5_clients](SQL-Export/mt5-clients.md) — [client](../../Platform-Setup/Clients.md) database.
  * [mt5_documents](SQL-Export/mt5-documents.md) — database of [client documents (#documents)](../../Platform-Setup/Clients.md#documents).
  * [mt5_users](SQL-Export/mt5-users.md) — [account](../../Platform-Setup/Accounts.md) database.
  * [mt5_orders](SQL-Export/mt5-orders.md) — open [order](../../Platform-Setup/Orders.md) database.
  * [mt5_positions](SQL-Export/mt5-positions.md) — [position](../../Platform-Setup/Positions.md) database.
  * [mt5_orders_history](SQL-Export/mt5-orders-history.md) — closed [order](../../Platform-Setup/Orders.md) database.
  * [mt5_deals](SQL-Export/mt5-deals.md) — [deal](../../Platform-Setup/Deals.md) database.
  * [mt5_accounts](SQL-Export/mt5-accounts.md) — trade account state database.
  * [mt5_prices](SQL-Export/mt5-prices.md) — database of prices.
  * [mt5_daily](SQL-Export/mt5-daily.md) — database of daily reports.


  * [mt5_daily_orders](SQL-Export/mt5-daily-orders.md) — data on the status of open orders at the end of the trading day.
  * [mt5_daily_positions](SQL-Export/mt5-daily-positions.md) — data on the status of position at the end of the trading day.


  * [mt5_holidays](SQL-Export/mt5-holidays.md) — [holiday](../../Platform-Setup/Holidays.md) configurations.
  * [mt5_network](SQL-Export/mt5-network.md) — general [settings of servers](../../Platform-Setup/Network-cluster/Configuring-Servers.md).
  * [mt5_network_access_servers](SQL-Export/mt5-network-access-servers.md) — access servers settings.
  * [mt5_network_history_servers](SQL-Export/mt5-network-history-servers.md) — history server settings.
  * [mt5_network_trade_servers](SQL-Export/mt5-network-trade-servers.md) — trade servers settings.
  * [mt5_network_backup_servers](SQL-Export/mt5-network-backup-servers.md) — backup servers settings.
  * [mt5_network_backup_folders](SQL-Export/mt5-network-backup-folders.md) — backed up custom folders.
  * [mt5_firewall](SQL-Export/mt5-firewall.md) — [firewall](../../Platform-Setup/Security/Firewall.md) settings.
  * [mt5_routing](SQL-Export/mt5-routing.md) — settings of [routing rules](../../Platform-Setup/Routing.md).
  * [mt5_routing_dealers](SQL-Export/mt5-routing-dealers.md) — settings of [dealers/gateways (#dealers)](../../Platform-Setup/Routing.md#dealers) in routing rules.
  * [mt5_routing_conds](SQL-Export/mt5-routing-conds.md) — [additional conditions (#condition)](../../Platform-Setup/Routing/Actions-and-Conditions.md#condition) in routing rules
  * [mt5_feeders](SQL-Export/mt5-feeders.md) — settings of [data feeds](../../Platform-Setup/Data-Feeds.md).
  * [mt5_feeder_translates](SQL-Export/mt5-feeder-translates.md) — [conversion settings (#translation)](../../Platform-Setup/Data-Feeds/Configuration-of.md#translation) on data feeds.
  * [mt5_feeder_params](SQL-Export/mt5-feeder-params.md) — [additional settings (#parameters)](../../Platform-Setup/Data-Feeds/Configuration-of.md#parameters) of data feeds.


  * [mt5_feeder_symbols](SQL-Export/mt5-feeder-symbols.md) — [symbol settings (#symbols)](../../Platform-Setup/Data-Feeds/Configuration-of.md#symbols) for data feeds.


  * [mt5_reports](SQL-Export/mt5-reports.md) — [report](../../Platform-Setup/Reports.md) settings.
  * [mt5_report_params](SQL-Export/mt5-report-params.md) — [additional settings (#module)](../../Platform-Setup/Reports.md#module) of reports.
  * [mt5_plugins](SQL-Export/mt5-plugins.md) — [plugin](../../Platform-Setup/Plugins.md) settings
  * [mt5_plugin_params](SQL-Export/mt5-plugin-params.md) — [additional settings (#module)](../../Platform-Setup/Plugins.md#module) of plugins.
  * [mt5_time](SQL-Export/mt5-time.md) — platform [trading time settings](../../Platform-Setup/Time.md).
  * [mt5_time_weekdays](SQL-Export/mt5-time-weekdays.md) — [working time schedule (#daily-settings)](../../Platform-Setup/Time.md#daily-settings) of the platform, by days.
  * [mt5_gateways](SQL-Export/mt5-gateways.md) — gateway settings.
  * [mt5_gateways_params](SQL-Export/mt5-gateways-params.md) — additional gateway settings.
  * [mt5_gateways_translates](SQL-Export/mt5-gateways-translates.md) — translation settings in gateways.


  * [mt5_gateways_symbols](SQL-Export/mt5-gateways-symbols.md) — [symbol settings (#symbols)](../../Platform-Setup/Gateways/Configuration-of.md#symbols) for gateways.



## Your own data in MetaTrader 5 tables

In the platform, you can create your own tables and databases, add your own fields in mt5_* tables, which are used for data export, as well as create stored procedures and triggers.

  * The backup server does not recreate data, but only adds or updates existing records. A table entry is only deleted if the appropriate entry is deleted on the platform side. For example, if a user is added to the mt5_users tables, the appropriate user record will exist in the database until the user is deleted from MetaTrader 5.
  * The backup server only works with its own tables and fields.
  * The backup server does not create default indexes. Each index is an extra load on the database, which can slow down exports and information updates.
  * When you create your own fields in mt5_* tables, do not forget to set default values for them (or allow NULL). Otherwise, the backup server will not be able to add new entries to the tables.



## Additional information

Find additional recommendations on handling SQL databases in the articles:

  * [Export to SQL database takes too much time](https://support.metaquotes.net/en/articles/1598)
  * [How to present account permissions in MySQL](https://support.metaquotes.net/en/articles/1576)


