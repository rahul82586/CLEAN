[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../Configuration-Databases.md) / Groups

[Previous](Time/Update-Settings.md) | [Next](Groups/Data-Structure.md)

# Groups

The Web API provides the following requests for receiving settings of client groups on the server:

Request | Description  
---|---  
[/api/group/add](Groups/Add.md) | Create/edit a client group on the server.  
[/api/group/add_batch](Groups/Add-Multiple.md) | Create/edit multiple client groups on the server.  
[/api/group/delete](Groups/Delete.md) | Delete a client group from the server.  
[/api/group/delete_batch](Groups/Delete-Multiple.md) | Delete multiple client groups from the server.  
[/api/group/shift](Groups/Shift.md) | Change the position of a group configuration in the list.  
[/api/group/total](Groups/Get-Total.md) | Get the total number of groups available on the server.  
[/api/group/next](Groups/Get-by-Index.md) | Get the configuration of one or more groups by index in the list.  
[/api/group/get](Groups/Get-by-Name.md) | Get the group configuration by the name.  
  
The format, in which the data about group configuration are passed, are described in the ["Data Structure"](Groups/Data-Structure.md) section.
