[🏠 Document Start](../README.md) / [SQL Export](README.md) / Installation and Setup of FireBird

[Previous](Installation-and-Setup-of-MariaDB.md) | [Next](Installation-and-Setup-of-MS-SQL.md)

# Installation and Setup of FireBird

Download one of the distribution kits from FireBird website ([http://www.firebirdsql.org/en/server-packages](https://www.firebirdsql.org/en/server-packages)).

> Select 32 or 64-bit considering potential volumes of databases. 64-bit server version is more preferable, as it makes possible to have data caches of more than 2 GB and has better scalability due to increasing RAM on the server.

Run the installation file and follow the on-screen instructions. Agree to the terms of use and specify FireBird installation path (you may use the default path). Next, specify the list of components to install or use the default option.

![FireBird installation](images/firebird_install.gif)

Then specify the name for the program group in the Start menu and configure the integration of the FireBird server with the operating system (these parameters can also be left by default). At the next step, specify the password for the SYSDBA login (administrator account). Start the installation process by pressing "Install" and wait for it to finish.

![FireBird installation](images/firebird_install2.gif)

After installation, you need to create a schema (database) to which data will be exported. To do this, open "Start — All Programs — FireBird 3.0" and launch "Firebird ISQL Tool". Execute the following command in it:

CREATE DATABASE 'path_to_the_DB\DB-file_name.fdb' page_size 16384 user 'user_name' password 'password';  
---  
  
Example:

![Example of FireBird database creation](images/firebird_base_create.png)

In this example, 'c:\databases' directory should be created in advance.

Additional Firebird setup should be performed to increase efficiency. To do this, edit the firebird.conf configuration text file in the installation directory:

# ----------------------------  
# Number of cached database pages  
#  
# This sets the number of pages from any one database that can be held  
# in cache at once. If you increase this value, the engine will  
# allocate more pages to the cache for every database. By default, the  
# SuperServer allocates 2048 pages for each database and the classic  
# allocates 75 pages per client connection per database.  
#  
# Type: integer  
#  
  
DefaultDbCachePages = 65536  
---  
  
It means that DefaultDbCachePages line should be uncommented and the value of 65536 should be set for it. This will make Firebird to use cache of 1 GB for the database. If necessary, you can set a lower value using the following equation:

Cache size = Page size (16 Kb) * DefaultDbCachePages  
---  
  
> The maximum value for DefaultDbCachePages is 65536 meaning that the maximum cache for 16 Kb pages will be approximately equal to 1 GB.

In case backup and FireBird servers are installed on the same computer, connection settings will be as follows:

![fb_setting_local](images/fb_setting_local.png)

In case backup and FireBird servers are located on different computers:

![fb_setting_remote](images/fb_setting_remote.png)

> It is recommended to install FireBird and backup servers on the same computer for faster export. It should also be kept in mind that the backup server itself also consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backups will work close to necessary DBMS.

Additional export parameters can be selected at [SQL Options (#sql-settings)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql-settings) tab.

The backup server will immediately start export into the external DBMS after all settings are specified. Request the log of the appropriate backup server using SQL keyword to track the export process: 

2012.10.17 15:16:08 SQL Export Firebird: successfully connected to database 'c:\databases\metatrader5.fdb' at '127.0.0.1' as user 'SYSDBA'  
2012.10.17 15:16:08 SQL Export Firebird: server version 3.0.2  
2012.10.17 15:16:08 SQL Export Firebird: table 'mt5_symbols' creating started  
2012.10.17 15:16:08 SQL Export Firebird: table 'mt5_symbols' created  
2012.10.17 15:16:08 SQL Export Firebird: primary key for 'mt5_symbols' adding started  
2012.10.17 15:16:08 SQL Export Firebird: primary key for 'mt5_symbols' added  
2012.10.17 15:16:08 SQL Export Firebird: table 'mt5_symbols_sessions' creating started  
2012.10.17 15:16:08 SQL Export Firebird: table 'mt5_symbols_sessions' created  
2012.10.17 15:16:08 SQL Export Firebird: primary key for 'mt5_symbols_sessions' adding started  
2012.10.17 15:16:08 SQL Export Firebird: primary key for 'mt5_symbols_sessions' added  
2012.10.17 15:16:08 SQL Export Symbols: 0 symbols and 0 sessions loaded in 93 msecs  
2012.10.17 15:16:08 SQL Export Symbols: synchronization started  
...  
---
