[🏠 Document Start](../../../../README.md) / [MetaTrader 5 Trading Platform](../../../../MetaTrader-5-Trading-Platform.md) / [Platform Components](../../../Platform-Components.md) / [Backup Server](../../Backup-Server.md) / [SQL Export](../SQL-Export.md) / mt5_firewall

[Previous](mt5-network-backup-folders.md) | [Next](mt5-routing.md)

# mt5_firewall

Data on the [firewall settings](../../../Platform-Setup/Security/Firewall.md) is exported to this table. The table contains the following fields:

Name | Type | Description  
Timestamp | Integer | A unique value within the table. Used by MetaTrader 5 servers for internal purposes. If the Timestamp of a record has changed, it means that the record has been changed.  
Action | Integer | The type of actions undertaken in accordance with the firewall rule:

  * 0 — block
  * 1 — allow
  * 2 — always allow

  
From | String | Beginning of the range of the IP addresses the firewall rule is applied to.  
To | String | End of the range of the IP addresses the firewall rule is applied to.  
Comment | String | A comment to the firewall rule.
