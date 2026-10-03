[🏠 Document Start](../README.md) / [SQL Export](README.md) / Installation and Setup of MySQL

[Previous](README.md) | [Next](Installation-and-Setup-of-MariaDB.md)

# Installation and Setup of MySQL Server

Download one of the distribution kits from MySQL website ([http://dev.mysql.com/downloads/mysql](https://dev.mysql.com/downloads/mysql)) to start installation.

> Select 32 or 64-bit considering potential volumes of databases. 64-bit server version is more preferable, as it makes possible to have data caches of more than 2 Gb and has better scalability due to increasing RAM on the server.

Downloaded distribution kit should be installed in accordance with the instructions:

  * at the first step, agree to the terms of use and click "Next"
  * at the second step, select the installation type ("Server only" is recommended)
  * at the third step, click "Execute" and wait for the installation to complete
  * at the fourth and fifth steps, click "Next" to go to the MySQL configuration



![MySQL Installation](images/mysql_install.gif)

During the first configuration step, select the installation type "Standalone MySQL Server /Classin MySQL Replication". Next, select the type of the computer on which MySQL is installed. Based on this information, the configuration Wizard sets efficient parameters for memory, hard drive and CPU consumption. Developer Machine should not be used in real work, therefore, select one of the following types:

  * Server Machine is used in case other services (for example, web server) are present on the computer. In this case, MySQL will consume a "moderate" amount of memory.
  * Dedicated MySQL Server Machine should be selected if the computer will be used exclusively for MySQL server. In this case, MySQL will consume "maximum available" amount of memory for faster performance.



In addition to the computer type, ports and communication channels can also be configured from here, although you can use default values ​​for these parameters.

![Database Configuration](images/mysql_configure.gif)

At the next step, specify the password for the root login (administrator account). Here you can also create additional accounts and configure permissions for them.

![Configuring MySQL Accounts](images/mysql_configure_users.png)

Further you will be asked to configure the integration of the MySQL server with the operating system, as well as the server extensions. You can use default settings for the above parameters. At the last step, click "Execute" and wait for the configuration to complete.

![MySQL configuration completion](images/mysql_configure_finish.gif)

To increase MySQL server performance, edit the my.ini file located in the MySQL installation directory, i.e. C:\Program Files\MySQL\MySQL Server 5.7\my.ini for the 64-bit version and C:\Program Files (x86)\MySQL\MySQL Server 5.7\my.ini for the 64-bit version. The file can also be located in C:\Program Data\MySQL\MySQL Server 5.7.

# InnoDB, unlike MyISAM, uses a buffer pool to cache both indexes and  
# row data. The bigger you set this the less disk I/O is needed to  
# access data in tables. On a dedicated database server you may set this  
# parameter up to 80% of the machine physical memory size. Do not set it  
# too large, though, because competition of the physical memory may  
# cause paging in the operating system. Note that on 32bit systems you  
# might be limited to 2-3.5G of user level memory per process, so do not  
# set it too high.  
innodb_buffer_pool_size=2046M  
---  
  
This parameter should be selected considering the server's bit count and available physical memory:

  * for a 32-bit server this value should not exceed 80 % of physical memory and it also should not exceed 2046;
  * for a 64-bit server this value should not exceed 80 % of physical memory.



When exporting data, the platform uses zero date if a date is not specified. Thus in my.ini you need to turn off the SQL modes that prohibit zero dates: NO_ZERO_IN_DATE and NO_ZERO_DATE. Find the "sql_mode" parameter and delete that modes from it:

sql_mode = "STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"  
---  
  
The last step is creation of the schema, to which MySQL data is exported, and performing configuration on the side of MetaTrader 5.

To do this, launch MySQL 5.7 Command Line Client in Start - All Programs - MySQL - MySQL Server 5.7 and enter root password. The following script should be executed after that:

create schema schema_name;  
---  
  
For example:

create schema metatrader5;  
---  
  
In case backup and MySQL servers are installed on the same computer, connection settings will be as follows:

![Export settings when installing MySQL on the same computer where the backup server is installed](images/mysql_platform_local.png)

In case backup and MySQL servers are located on different computers:

![Export settings when installing MySQL on a separate computer](images/mysql_platform_remote.png)

> It is recommended to install MySQL and backup servers on the same computer for faster export. It should also be kept in mind that the backup server itself also consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backups will work close to necessary DBMS.

Additional export parameters can be selected at [SQL Options (#sql-settings)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql-settings) tab.

After all settings are specified, the backup server will immediately start export into the external DBMS. Request the log of the appropriate backup server using SQL keyword to track the export process:

19:00:16 SQL Export MySQL: successfully connect to '127.0.0.1:metatrader5' for 'root'  
19:00:16 SQL Export MySQL: server version 5.7.19  
19:00:16 SQL Export MySQL: table 'mt5_symbols' creating started  
19:00:16 SQL Export MySQL: table 'mt5_symbols' created  
19:00:16 SQL Export MySQL: primary key for 'mt5_symbols' adding started  
19:00:16 SQL Export MySQL: primary key for 'mt5_symbols' added  
19:00:16 SQL Export MySQL: table 'mt5_symbols_sessions' creating started  
19:00:16 SQL Export MySQL: table 'mt5_symbols_sessions' created  
19:00:16 SQL Export MySQL: primary key for 'mt5_symbols_sessions' adding started  
19:00:16 SQL Export MySQL: primary key for 'mt5_symbols_sessions' added  
19:00:16 SQL Export Symbols: 0 symbols and 0 sessions loaded in 312 msecs  
19:00:16 SQL Export Symbols: synchronization started  
...  
---
