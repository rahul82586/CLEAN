[🏠 Document Start](../../README.md) / [Configuration Interfaces](../README.md) / [Managers](../Managers.md) / IMTConManager

[Previous](../Managers.md) | [Next](IMTConManager/Enumerations.md)

# IMTConManager

The IMTConManager contains the following methods:

Method | Purpose  
---|---  
[Release](IMTConManager/Release.md) | Delete the current object.  
[Assign](IMTConManager/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTConManager/Clear.md) | Clear an object.  
[Login](IMTConManager/Login.md) | Get and set the login of a manager.  
[Mailbox](IMTConManager/Mailbox.md) | Get and set the name of a manager's mailbox in the internal mail system.  
[Server](IMTConManager/Server.md) | Get and set the ID of the trade server, to which the manager belongs.  
[LimitLogs](IMTConManager/LimitLogs.md) | Get and set the time period of system logs available to a manager.  
[LimitReports](IMTConManager/LimitReports.md) | Get and set the time period of reports available to a manager.  
[Right](IMTConManager/Right.md) | Get and set the rights of a manager.  
[GroupAdd](IMTConManager/GroupAdd.md) | Add a group of accounts that the manager will process.  
[GroupUpdate](IMTConManager/GroupUpdate.md) | Modify a group of accounts, which is processed by the manager, at the specified position in the list.  
[GroupShift](IMTConManager/GroupShift.md) | Move a group of accounts, which is processed by the manager, in the list of groups.  
[GroupDelete](IMTConManager/GroupDelete.md) | Delete a group of accounts processed by the manager, by its index  
[GroupTotal](IMTConManager/GroupTotal.md) | Get the number of entries in the list of groups processed by a manager.  
[GroupNext](IMTConManager/GroupNext.md) | Get a group processed by the manager, at a specified position in the list.  
[AccessAdd](IMTConManager/AccessAdd.md) | Create a range of IP addresses, from which a manager is allowed to connect to the platform.  
[AccessUpdate](IMTConManager/AccessUpdate.md) | Modifies a range of IP addresses, from which a manager is allowed to connect to the platform, based on its position in the list.  
[AccessDelete](IMTConManager/AccessDelete.md) | Delete a range of IP addresses, from which a manager is allowed to connect to the platform, based on its position in the list.  
[AccessShift](IMTConManager/AccessShift.md) | Move a range of IP addresses, from which a manager is allowed to connect to the platform, in the list.  
[AccessTotal](IMTConManager/AccessTotal.md) | Get the number of ranges of IP addresses, from which a manager is allowed to connect to the platform.  
[AccessNext](IMTConManager/AccessNext.md) | Get a range of IP addresses, from which a manager is allowed to connect to the platform, based on its position in the list.  
[ReportAdd](IMTConManager/ReportAdd.md) | Create a report access permission for a manager.  
[ReportUpdate](IMTConManager/ReportUpdate.md) | Update a report access permission for a manager.  
[ReportDelete](IMTConManager/ReportDelete.md) | Delete a report access permission for a manager.  
[ReportShift](IMTConManager/ReportShift.md) | Shift a report access permission for a manager.  
[ReportTotal](IMTConManager/ReportTotal.md) | Get the number of report access permissions that the manager has.  
[ReportNext](IMTConManager/ReportNext.md) | Get a manager's report access permission based on the permission position in the list.  
  
The IMTConManager class contains the following enumerations:

Enumeration | Purpose  
---|---  
[EnManagerRights (#enmanagerrights)](IMTConManager/Enumerations.md#enmanagerrights) | Manager's permissions.  
[EnManagerRightFlags (#enmanagerrightflags)](IMTConManager/Enumerations.md#enmanagerrightflags) | A flag of permission/prohibition.  
[EnManagerLimit (#enmanagerlimit)](IMTConManager/Enumerations.md#enmanagerlimit) | Limit of access to system logs.
