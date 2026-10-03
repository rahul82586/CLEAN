[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Managers](../Managers.md) / Data Structure

[Previous](../Managers.md) | [Next](Add.md)

<a id="data-structure"></a>
# Data Structure (#data-structure)

A manager configuration is passed in JSON format in response to the [/api/manager/add](Add.md), [/api/manager/next](Get-by-Index.md) and [/api/manager/get](Get-by-Login.md) requests.

Parameter | Type | Purpose  
Login | Integer | The login of a manager.  
Name | String | The name of the manager. A read-only field. Corresponds to the value of the appropriate field of the [user](../../Users/Data-Structure.md) based on whose record the manager is created.  
Mailbox | String | The name of the manager's mailbox in the internal mailing system.  
Server | Integer | The ID of the trade server, to which the manager belongs.  
Right | Array | Manager permissions in the form of an array [1,1,0,0,...]. 1 — permission is granted, 0 — permission is not granted. The full list of permissions is described in the [EnManagerRights (#enmanagerrights)](../../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights) enumeration.  
RequestLimitLogs | Integer | The time period of system logs that are available to a manager. Specified as a value of the [EnManagerLimit (#enmanagerlimit)](../../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerlimit) enumeration.  
RequestLimitReports | Integer | The time period of reports that are available to a manager. Specified as a value of the [EnManagerLimit (#enmanagerlimit)](../../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerlimit) enumeration.  
Groups | Array | [Account groups (#groups)](Data-Structure.md#groups) managed by the manager.  
Access | Array | [Ranges of IP addresses (#ip)](Data-Structure.md#ip), from which a manager is allowed to connect to the platform.  
  
<a id="groups"></a>
## Groups (#groups)

Parameter | Type | Purpose  
Group | String | The path to the group.  
  
<a id="ip"></a>
## IP addresses (#ip)

Parameter | Type | Purpose  
From | String | The beginning of the range of IP addresses, from which a manager account can connect.  
To | String | The end of the range of IP addresses, from which a manager account can connect.
