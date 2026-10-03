[🏠 Document Start](../README.md) / SQL Export

[Previous](../Web-API/Manager-Interface-(Rest-API)/NET-Implementation-of-Protocol/WebTrader.md) | [Next](Installation-and-Setup-of-MySQL.md)

# SQL Export

The MetaTrader 5 trading platform provides standard options for the real-time data export to MySQL, Microsoft SQL Server, FireBird, Oracle, MariaDB and PostgreSQL databases. This option enables the quick and easy deployment of data export to an external DBMS for using the platform data in any popular programming language and third-party applications. Thus, it is possible to create an intermediate layer between a trade server and broker's program services that regularly access trading data. This reduces the load on the trade server when it receives the current trading data.

The export function is enabled by simple specification of settings for connection to DBMS via MetaTrader 5 Administrator. After that, the backup server will immediately perform an initial synchronization of data from the DBMS. Further, new data will be exported to the DBMS in real time. The following data is exported:

  * Information about clients (general information and trading status)
  * Current active orders and positions
  * The history of orders and deals
  * Current prices
  * Virtually all settings of the trading platform (except for the working time, synchronization and spreads)



The description of installation and setup of popular databases is provided in appropriate subsections:

  * [MySQL Server 5.7](Installation-and-Setup-of-MySQL.md) (supported versions: 5.1, 5.5, 5.6, 5.7)
  * [MariaDB 10.2](Installation-and-Setup-of-MariaDB.md) (all version supported)
  * [FireBird 3.0](Installation-and-Setup-of-FireBird.md) (supported versions: 2.0, 2.1, 2.5, 3.0)
  * [Microsoft SQL Express 2012](Installation-and-Setup-of-MS-SQL.md) (supported versions: 2005, 2008, 2008 R2, 2012, 2014, 2016)
  * [Oracle Database Express Edition 11g](Installation-and-Setup-of-Oracle.md) (supported versions: 11g/11g Express Edition, 12c)
  * [PostgreSQL](Installation-and-Setup-of-PostgreSQL.md) (supported versions: 8.4 — 10.1)



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

A detailed description of exported tables can be found in the [MetaTrader 5 Administrator User Guide](https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server/sql_export).

## Your own data in MetaTrader 5 tables

In the platform, you can create your own tables and databases, add your own fields in mt5_* tables, which are used for data export, as well as create stored procedures and triggers.

  * The backup server does not recreate data, but only adds or updates existing records. A table entry is only deleted if the appropriate entry is deleted on the platform side. For example, if a user is added to the mt5_users tables, the appropriate user record will exist in the database until the user is deleted from MetaTrader 5.
  * The backup server only works with its own tables and fields.
  * The backup server does not create default indexes. Each index is an extra load on the database, which can slow down exports and information updates.
  * When you create your own fields in mt5_* tables, do not forget to set default values for them (or allow NULL). Otherwise, the backup server will not be able to add new entries to the tables.


