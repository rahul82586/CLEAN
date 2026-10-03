[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Data Structure

[Previous](../Firewall.md) | [Next](Add.md)

# Data Structure

Group configuration is passed in JSON format as a response to the [/api/firewall/add](Add.md) and [/api/firewall/next](Get-by-Index.md) requests.

Parameter | Type | Purpose  
Action | Integer | The type of actions undertaken in accordance with the firewall rule. Passed as a value of the [EnAction (#enaction)](../../../../Configuration-Interfaces/Firewall/IMTConFirewall/IMTCon-Enumerations.md#enaction) enumeration.  
From | String | Beginning of the range of IP addresses to which the firewall is applied.  
To | String | End of the range of IP addresses to which the firewall rule is applied.  
Comment | String | A comment to the firewall rule.
