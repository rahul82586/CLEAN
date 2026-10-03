[🏠 Document Start](../../README.md) / [MetaTrader 5 Trading Platform](../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../Platform-Components.md) / Backup Server

[Previous](History-Server/Console-Commands.md) | [Next](Backup-Server/Backup-Features.md)

# Backup Server

Servers of this type are used for creating backup copies of data that will be used in case of the trade or history server failure. They perform the following functions:

  * They provide the real-time backuping of the trade server and the history server. Each server is associated with one or more separate backup server instances which can replace it at any time.
  * They create backups of all databases every day, besides they perform regular backups of client and trade bases.
  * When backuping a history server they create real time backups of data required for correct restoring of [gateways](../Platform-Setup/Gateways.md): custom settings that can be stored (at developer's discretion) in the settings.dat file in a gateway work folder, and trade executions database.
  * They provide [automatic failover (#auto)](Backup-Server/Switching-to.md#auto) in case the primary server becomes unavailable.
  * Using backup servers, you can easily [migrate servers (#manual)](Backup-Server/Switching-to.md#manual) to new hardware.
  * Backup servers enable you to quickly [restore](Backup-Server/Restoring-Server.md) server operation in the manual mode even if the main trade server is unavailable, and connection to the platform via MetaTrader 5 Administrator is not possible.
  * [Replicate information](Backup-Server/SQL-Export.md) to database managed by MySQL, MariaDB, PostgreSQL, Firebird, MSSQL or Oracle.



> For server configuration details, please see the ["Network cluster"](../Platform-Setup/Network-cluster/Configuring-Servers.md) section.
