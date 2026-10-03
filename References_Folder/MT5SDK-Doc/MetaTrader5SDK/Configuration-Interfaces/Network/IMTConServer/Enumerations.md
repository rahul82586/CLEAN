[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / Enumerations

[Previous](../IMTConServer.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConServer](../IMTConServer.md) class contains the following enumerations:

<a id="enservertypes"></a>
## IMTConServer::EnServerTypes (#enservertypes)

Server types are listed in IMTConServer::EnServerTypes.

ID | Value | Purpose  
NET_MAIN_TRADE_SERVER | 0 | The Main Trade Server.  
NET_TRADE_SERVER | 1 | Trade Server.  
NET_HISTORY_SERVER | 2 | History Server.  
NET_ACCESS_SERVER | 3 | Access Server.  
NET_BACKUP_SERVER | 4  | Backup Server.  
NET_ANTIDDOS_SERVER | 7 | Component for connecting an external Anti-DDoS service provider.  
NET_SERVER_FIRST |  | Beginning of enumeration. It correspond to NET_MAIN_TRADE_SERVER.  
NET_SERVER_LAST |  | End of enumeration. It correspond to NET_ANTIDDOS_SERVER.  
  
This enumeration is used in the [IMTConServer::Type](Type.md) method.

<a id="enfailovermodes"></a>
## IMTConServer::EnFailoverModes (#enfailovermodes)

Automated failover modes are enumerated in IMTConServer::EnFailoverModes.

Identifier | Value | Purpose  
FAILOVER_MODE_DISABLED | 0 | Automated failover is disabled.  
FAILOVER_MODE_BY_MOST | 1 | Switch to a backup server if the main server is unavailable for the most of monitoring access points.  
FAILOVER_MODE_BY_ALL | 2 | Switch to a backup server if the main server is unavailable for all of the monitoring access points.  
FAILOVER_MODE_FIRST |  | Beginning of enumeration. It corresponds to FAILOVER_MODE_DISABLED.  
FAILOVER_MODE_LAST |  | End of enumeration. It corresponds to FAILOVER_MODE_BY_ALL.  
  
This enumeration is used in the [IMTConServer::FailoverMode](FailoverMode.md) method.
