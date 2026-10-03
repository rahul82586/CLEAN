[🏠 Document Start](../../../README.md) / [MetaTrader 5 Trading Platform](../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../Platform-Components.md) / [Access Server](../Access-Server.md) / Antiflood Control

[Previous](Structure-of-Directories-and-Files.md) | [Next](Priority.md)

# Antiflood Control

The antiflood control system works on [access servers](../Access-Server.md). It allows protecting the trading platform from external harmful attacks. This protection system collects the database of users who send incorrect requests to the server (e.g. attempt to authorize with an incorrect login or password), as well as users who send too often requests.

> Antiflood control works with all types of connections to the server including manager ones (via the manager terminal and Manager API).

The number of connections and incorrect request per time unit can be set up on the ["Access" (#antiflood)](../../Platform-Setup/Network-cluster/Configuring-Servers/Access-Server.md#antiflood) tab of the access server:

!["Access" tab](images/network_add_access.png)

## System of Operation

The antiflood control system monitors user activity. Users are identified by their IP addresses as well as by the ID linked to their computers and operating systems. The following two activity types are controlled:

  * The total number of connections from one user  
The system tracks if a user creates too many connections. When a user connects to the server, their connection counter is incremented by one. If the next connection occurs in less than 3 seconds, the counter is incremented. If the specified time interval is exceeded, the counter is reset. When the counter reaches the number specified in the "Connections" field, the user is blocked for 5 minutes. The blocking period increases if the connections limit is reached again. The maximum blocking period is one hour.
  * Number of invalid packets from one user  
The system blocks brute-force attacks by analyzing authentication errors, which imply multiple login attempts with incorrect data. Also, the system detects garbage flood packets, which can be sent to the server by third-party utilities in an effort to reduce the server performance (i.e. a DoS attack). When a user sends an invalid packet to the server, the user's error counter is incremented by one. If the next invalid packet is sent in less than 5 minutes, the counter is incremented. If the specified time interval is exceeded, the counter is reset. When the counter reaches the number specified in the "Errors" field, the user is blocked for 5 minutes. The blocking period increases if the connections limit is reached again. The maximum blocking period is one hour.



The following records appear in the access server operation [Journal](../../Platform-Setup/Network-cluster/Journal.md) when a user is blocked:

  * IP is blocked after N connections [intruder] — a user is blocked by IP if the number of connections is exceeded;
  * CID is blocked after N errors [intruder] — a user is blocked by CID (computer ID) if the number of errors is exceeded.



  * It is strongly recommended to keep the antiflood control system enabled.
  * IP addresses added to the "permit always" list in the [corresponding section](../../Platform-Setup/Security/Firewall.md), are not checked by the antiflood control system.

  
---  
  
## Retrieve IP address from X-Forwarded-For

Clients can connect to the platform through public services from various proxy servers. This may happen, for example, if you use an [Anti DDoS system](../../Platform-Setup/Security/Anti-DDoS-Protection.md), such as Cloudflare. In this case, the proxy server address will be displayed for the client's IP address in [account details](../../Platform-Setup/Accounts/Editing-Account.md) and [logs](../../Platform-Setup/Network-cluster/Journal.md). The same address will be used for anti-flood control system checks. To avoid this and provide real data, you can add proxy server addresses to the [firewall](../../Platform-Setup/Security/Firewall.md) whitelist (the "always allow" rule). In this case, the access server will try to retrieve the user's real IP address from the X-Forwarded-For header provided by the proxy server upon connection.

> Please make sure the IP addresses you are adding to the whitelist belong to trusted services, which may not transmit false addresses in requests.
