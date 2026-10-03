[🏠 Document Start](../README.md) / [SQL Export](README.md) / Installation and Setup of PostgreSQL

[Previous](Installation-and-Setup-of-Oracle.md) | [Next](../Internal-Data-Types/README.md)

# Installation and Setup of PostgreSQL

Download the required version of PostgreSQL installer from the [official website](https://www.postgresql.org/download/).

> ["Update for Visual C++ 2013 and Visual C++ Redistributable Package"](https://support.microsoft.com/en-us/help/3179560/update-for-visual-c-2013-and-visual-c-redistributable-package) must be installed on the computer where the backup server is installer. Otherwise expert to Oracle databases will not be possible.

Run the installation file and follow the on-screen instructions. Choose an installation directory an a set of components:

![Installation of PostgreSQL](images/postgre1.gif)

Next, select the directory, in which the databases will be stored, set a password for the administrator account "postgres". Then specify the port at which the PostgreSQL server will listen to incoming connections.

![Installation of PostgreSQL](images/postgre2.gif)

Next, set the [locale](https://postgrespro.com/docs/postgrespro/9.5/locale.html) to be used by by the database cluster. The locale is inherited from the operating system be default. Locale affects the operation of some SQL requests. In the next steps, click "Next", and wait for the installation to complete.

![Installation of PostgreSQL](images/postgre3.gif)

After installation, run the pgAdmin utility from the Start menu. Connect to the server using the postgres login and the password specified during installation. Next, create a database to export information from MetaTrader 5.

![Creating a database in PostgreSQL](images/postgre_db_create.png)

Then configure data export on the platform site. In case the backup server and PostgreSQL servers are installed on the same computer, connection parameters should be configured as follows:

![Export settings when installing PostgreSQL on the same computer where the backup server is installed](images/postgres_settings_local.png)

In case the backup server and PostgreSQL servers are installed on different computers, connection parameters should be configured as follows:

![Export settings when installing PostgreSQL on a separate computer](images/postgres_settings_remote.png)

> It is recommended to install PostgreSQL and the backup server on the same computer for faster export. However, it should also be kept in mind that the backup server consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backup servers will run close to necessary DBMS. 

Additional export parameters can be selected at [SQL Options (#sql-settings)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql-settings) tab.

The backup server will immediately start export into the external DBMS after all settings are specified. Request the log of the appropriate backup server using SQL keyword to track the export process:

2017.12.21 15:17:17.154 SQL Export PostgreSQL: server version 10.1   
2017.12.21 15:17:17.156 SQL Export PostgreSQL: successfully connected to database 'metatrader5' at 'localhost' as user 'postgres'   
2017.12.21 15:17:17.170 SQL Export PostgreSQL: table 'mt5_symbols_sessions' creating started   
2017.12.21 15:17:17.180 SQL Export PostgreSQL: table 'mt5_symbols_sessions' created   
...  
---
