[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / Installation and Setup of MS SQL

[Previous](Installation-and-Setup-of-MariaDB.md) | [Next](Installation-and-Setup-of-Oracle.md)

# Installation and Setup of Microsoft SQL Server

Download one of the distribution kits from Microsoft website ([http://www.microsoft.com/en-us/download/details.aspx?id=29062](https://www.microsoft.com/en-us/download/details.aspx?id=29062)) to install free version of Microsoft SQL Exress 2012.

You need to download ENU\x86\SQLEXPR_x86_ENU.exe or ENU\x64\SQLEXPR_x64_ENU.exe.

  * MetaTrader 5 supports data export both to Microsoft SQL Server 2005/2008/2012/2014/2016/2017/2019/2022 and to their Express versions.
  * Microsoft SQL Server Express 2005 has a limit of 4 GB on user data. Microsoft SQL Server Express 2008 R2 / 2012 has a limit of 10 GB. Therefore, it is recommended to use 2008 R2 or 2012 as Express version. If the limit is exceeded, new data will not be added to the database.


  * Operating system Windows 8 or higher is required for the [Microsoft SQL 2016](https://www.microsoft.com/en-us/download/details.aspx?id=56840) installation.


  * Select 32 or 64-bit considering potential volumes of databases. 64-bit server version is more preferable, as it makes possible to have data caches of bigger volume and has better scalability due to increasing RAM on the server.


  * By default, the backup server connects to the database using the Windows system driver MS OLE DB Provider for SQL Server (SQLOLEDB). This driver is pre-installed in all operating systems, however it is outdated and does not support the TLS 1.1 and TLS 1.2 protocols. If your company's policy does not allow using TLS protocols below 1.1. and they are disabled in the system, the SQLOLEDB driver will not be able to provide backup server connection to the database. In this case you should install an additional driver [MSOLEDBSQLS](https://www.microsoft.com/en-us/download/details.aspx?id=56730), which supports protocols TLS 1.1 and 1.2. After that the backup server will automatically start using the new driver for connecting to the database.

  
---  
  
Downloaded distribution kit should be installed in accordance with the instructions. First, select "New SQL Server stand-alone installation or add features to an existing installations" to install a new copy of Microsoft SQL Server. Check the "I accept the license terms" option at "License Terms" step. Leave default parameters at the following steps up to "Server Configuration". Set Automatic mode for "SQL Server Browser" at "Server Configuration" step:

![MSSQL_6_a](images/mssql_6_a.png)

Select "Mixed Mode (SQL Server authentication and Windows authentication)" and specify the administrator password at "Database Engine Configuration" step:

![MSSQL_8_a](images/mssql_8_a.png)

Leave default parameters at the following steps.

TCP/IP should also be enabled for access to SQL Server from the network. To do this, launch "SQL Server Configuration Manager" from the start menu:

![MSSQL_TCP](images/mssql_tcp.png)

Restart SQL Server (SQLExpress) service in SQL Server Services section.

Launch SQLCMD.exe application ("C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Binn\OSQL.EXE" or "C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Binn\OSQL.EXE") with the following parameters after installation to create a database:

SQLCMD.EXE -S localhost\SQLEXPRESS -U sa -P password  
---  
  
The password is the same as at "Database Engine Configuration" step. Execute the following command in SQLCMD.exe console:

CREATE DATABASE METATRADER5  
GO  
---  
  
The database will be generated.

In case backup and MS SQL servers are installed on the same computer, connection settings will be as follows:

![MSSQL_AA](images/mssql_aa.png)

In case backup and MS SQL servers are located on different computers:

![MSSQL_BA](images/mssql_ba.png)

> It is recommended to install MS SQL and backup servers on the same computer for faster export. It should also be kept in mind that the backup server itself also consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backups will work close to necessary DBMS.

Additional export parameters can be selected at [SQL Options (#sql-settings)](../../../Platform-Setup/Network-cluster/Configuring-Servers/Backup-Server.md#sql-settings) tab.

The backup server will immediately start export into the external DBMS after all settings are specified. Request the log of the appropriate backup server using SQL keyword to track the export process: 

13:24:40 SQL Export MSSQL: successfully connected to database 'mt5' at 'localhost\SQLEXPRESS' as user 'sa'  
13:24:40 SQL Export MSSQL: server version 11.0.2100.60 RTM (Express Edition)  
13:24:40 SQL Export MSSQL: table 'mt5_symbols' creating started  
13:24:40 SQL Export MSSQL: table 'mt5_symbols' created  
13:24:40 SQL Export MSSQL: primary key for 'mt5_symbols' adding started  
13:24:40 SQL Export MSSQL: primary key for 'mt5_symbols' added  
13:24:40 SQL Export MSSQL: table 'mt5_symbols_sessions' creating started  
13:24:40 SQL Export MSSQL: table 'mt5_symbols_sessions' created  
13:24:40 SQL Export MSSQL: primary key for 'mt5_symbols_sessions' adding started  
13:24:40 SQL Export MSSQL: primary key for 'mt5_symbols_sessions' added  
13:24:40 SQL Export Symbols: 0 symbols and 0 sessions loaded in 344 msecs  
13:24:40 SQL Export Symbols: synchronization started  
...  
---
