[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [Examples](../../Examples.md) / [Web Registration](../Web-Registration.md) / Setup

[Previous](Structure-of-Files-and-Folders.md) | [Next](Account-Registration-Process.md)

# Setup

To integrate the Web registration with your online resource, you must perform the following steps.

## System Requirements

The following conditions are required for the Web registration implementation:

  * MySQL server;
  * PHP version 5 or higher;
  * In the PHP project, include the php_mbstring.dll and php_sockets.dll modules;
  * A mail server for sending registration confirmation email.



## Copying/Inclusion into the Project

The first step is copying the whole Examples/PHP directory from the one where Web API is [installed](../../../../../Getting-Started/Setup.md) to your project working directory. Then include /Examples/web_registration/index.php into your PHP project.

## Configuration of Web Registration

All the basic settings of the Web registration of accounts are provided in the file at /Examples/web_registration/index.php:
    
    
    <?php
    //+------------------------------------------------------------------+
    //|                                             MetaTrader 5 Web API |
    //|                   Copyright 2001-2011, MetaQuotes Software Corp. |
    //|                                        https://www.metaquotes.net |
    //+------------------------------------------------------------------+
      define("PATH_TO_SCRIPTS", "../mt5_api/");
      include PATH_TO_SCRIPTS . "mt5_api.php";
      //---
      include "mysql.php";
      include "tools.php";
      include "web_pageform.php";
      //--- settings of connection
      define("MT5_SERVER_IP", "192.168.9.150");           // MetaTrader: ip MetaTrader 5 server
      define("MT5_SERVER_PORT", 1951);                    // MetaTrader: port MetaTrader 5 server
      define("MT5_SERVER_WEB_LOGIN", 1000);               // MetaTrader: login
      define("MT5_SERVER_WEB_PASSWORD", 'Password1');       // MetaTrader: password
      //---
      define('PAGE_ENCODING', 'utf-8');                   // Web: Page encoding
      //---
      define('MYSQL_SERVER',  'localhost');               // MySQL: Server
      define('MYSQL_LOGIN',   'mysql_login');             // MySQL: Login
      define('MYSQL_PASSWORD','mysql_password');          // MySQL: Password
      define('MYSQL_DB_NAME', 'mysql_db_name');           // MySQL: Database
      //---
      define('SMTP_SERVER',   'mail.mycompany.com');      // SMTP: Server
      define('SMTP_LOGIN',    'login');                   // SMTP: Login
      define('SMTP_PASSWORD', 'password');                // SMTP: Password
      define('SMTP_FROM',     'hello@mycompany.com');     // SMTP: From
      define('SMTP_FROM_NAME','Mr. Hello');               // SMTP: From Name
      //---
      $page = new WebPageForm();
      //---
      $page->CreatePage();
    ?>

It contains the following parameters to configure:

  * MT5_SERVER_IP — the address of the access server for connection.
  * MT5_SERVER_PORT — the port of the access server for connection.
  * MT5_SERVER_WEB_LOGIN — the login of the [manager account](../../../../Getting-Started.md).
  * MT5_SERVER_WEB_PASSWORD — the API password for the manager account.
  * PAGE_ENCODING — encoding in which the page will be displayed.
  * MYSQL_SERVER — the address of the MySQL server.
  * MYSQL_LOGIN — a login for connecting to the MySQL database.
  * MYSQL_PASSWORD — a password for connecting to the MySQL database.
  * MYSQL_DB_NAME — the name of the database to which you want to connect .
  * SMTP_SERVER — the address of the SMTP server from which emails for confirming registration will be sent.
  * SMTP_LOGIN — a login for authorizing on the SMTP server.
  * SMTP_PASSWORD — a password for authorizing on the SMTP server.
  * SMTP_FROM — the address from which emails will be sent.
  * SMTP_FROM_NAME — the name of the sender that will be specified in the emails.



> If you are an experienced PHP programmer, you can modify the Web registration by making the necessary changes to the [source files](Structure-of-Files-and-Folders.md).
