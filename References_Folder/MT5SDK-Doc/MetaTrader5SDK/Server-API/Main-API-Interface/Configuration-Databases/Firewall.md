[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Configuration Databases](../Configuration-Databases.md) / Firewall

[Previous](Holidays/HolidayNext.md) | [Next](Firewall/Create.md)

# Firewall Configuration

A firewall is designed to protect your system from access from unwanted IP addresses. If a group of addresses is blocked, users (client, manager, administrator) with the address within the specified range will not be able to connect to the server. By default, it is assumed that all addresses are allowed.

> The latest rule is applied to an address, regardless of previous instructions, except for the addresses that are always allowed. Thus, the position of each instruction in the list is a very important factor when setting access from IP addresses.

Functions described in this section allow managing the firewall configuration, as well subscribe and unsubscribe from events associated with its change.

Function | Purpose  
---|---  
[FirewallCreate](Firewall/Create.md) | Create an object of the firewall configuration.  
[FirewallSubscribe](Firewall/Subscribe.md) | Subscribe to events and hooks associated with the firewall configuration.  
[FirewallUnsubscribe](Firewall/Unsubscribe.md) | Unsubscribe from events and hooks associated with the firewall configuration.  
[FirewallAdd](Firewall/Add.md) | Add or update a firewall configuration.  
[FirewallDelete](Firewall/Delete.md) | Delete a configuration of a data feed by its index.  
[FirewallShift](Firewall/Shift.md) | Change the position of a firewall configuration in the list.  
[FirewallTotal](Firewall/Total.md) | The total number of firewall configurations available in the platform.  
[FirewallNex](Firewall/Next.md) | Get the firewall configuration by the index.
