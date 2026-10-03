[🏠 Document Start](../README.md) / [SQL Export](README.md) / Installation and Setup of Oracle

[Previous](Installation-and-Setup-of-MS-SQL.md) | [Next](Installation-and-Setup-of-PostgreSQL.md)

# Installation and Setup of Oracle Database

Download the distribution kit from the Oracle's website ([http://www.oracle.com/technetwork/products/express-edition/downloads/index.html](https://www.oracle.com/technetwork/products/express-edition/downloads/index.html)) to install free version of Oracle Database Express Edition. Oracle allows the free use of only the 32-bit version of Express. Therefore, agree to the license terms and download Oracle Database Express Edition 11g Release 2 for Windows x32.

  * ["Update for Visual C++ 2013 and Visual C++ Redistributable Package"](https://support.microsoft.com/en-us/help/3179560/update-for-visual-c-2013-and-visual-c-redistributable-package) must be installed on the computer where the backup server is installer. Otherwise expert to Oracle databases will not be possible.


  * Oracle Database Express Edition is limited to 11 GB of user data. If the limit is exceeded, new data will not be added to the database.

  
---  
  
Distribution kit consists of a ZIP archive that should be unpacked into a temporary folder. Then launch DISK1\setup.exe and follow the instructions:

  * accept the license terms at License Agreement stage;
  * specify administrator password at Specify Database Passwords stage:



![Oracle_4](images/oracle_4.png)

Then click Next at the following stages and Install at the last one.

Create the client that will be used for connection. To do that, launch sqlplus.exe:

sqlplus.exe system/password  
---  
  
Use the same password that was specified at Specify Database Passwords stage during installation. For example:

sqlplus.exe system/MyAdminPassword  
---  
  
Then execute the following command to create the user:

create user user_name identified by password default tablespace users temporary tablespace temp;  
---  
  
And allow connection for it:

grant connect,resource to user_name;  
---  
  
For example:

create user mt5user identified by mt5password default tablespace users temporary tablespace temp;  
grant connect,resource to mt5user;  
---  
  
In case backup and Oracle servers are installed on the same computer, connection settings will be as follows:

![oracle_setting_local](images/oracle_setting_local.png)

In case backup and Oracle servers are located on different computers:

![oracle_setting_remote](images/oracle_setting_remote.png)

  * Oracle Database Express Edition has only one database named XE. Therefore, that is the database that should be specified in Data Folder parameter.
  * It is recommended to install Oracle and backup servers on the same computer for faster export. It should also be kept in mind that the backup server itself also consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backups will work close to necessary DBMS.

  
---  
  
Additional export parameters can be selected at [SQL Options (#sql-settings)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql-settings) tab.

The backup server will immediately start export into the external DBMS after all settings are specified. Request the log of the appropriate backup server using SQL keyword to track the export process: 

2012.10.18 16:33:36 SQL Export Oracle: successfully connected to database 'XE' at 'localhost' as user 'mt5user'  
2012.10.18 16:33:36 SQL Export Oracle: server version Oracle Database 11g Express Edition Release 11.2.0.2.0 - Production  
2012.10.18 16:33:36 SQL Export Oracle: table 'mt5_symbols' creating started  
2012.10.18 16:33:36 SQL Export Oracle: table 'mt5_symbols' created  
2012.10.18 16:33:36 SQL Export Oracle: primary key for 'mt5_symbols' adding started  
2012.10.18 16:33:36 SQL Export Oracle: primary key for 'mt5_symbols' added  
2012.10.18 16:33:36 SQL Export Oracle: table 'mt5_symbols_sessions' creating started  
2012.10.18 16:33:36 SQL Export Oracle: table 'mt5_symbols_sessions' created  
2012.10.18 16:33:36 SQL Export Oracle: primary key for 'mt5_symbols_sessions' adding started  
2012.10.18 16:33:36 SQL Export Oracle: primary key for 'mt5_symbols_sessions' added  
2012.10.18 16:33:36 SQL Export Symbols: 0 symbols and 0 sessions loaded in 203 msecs  
2012.10.18 16:33:36 SQL Export Symbols: synchronization started  
...  
---
