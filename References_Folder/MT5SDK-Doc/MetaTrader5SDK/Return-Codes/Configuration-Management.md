[🏠 Document Start](../README.md) / [Return Codes](README.md) / Configuration Management

[Previous](Authentication.md) | [Next](User-management.md)

# Configuration Management

This group of codes is returned by the server in case [configurations](../Manager-API/Administrator-Interface/Configuration-Databases.md) are changed:

Constant | Value | Description  
MT_RET_CFG_LAST_ADMIN | 2000 | Deleting the last administrator configuration.  
MT_RET_CFG_LAST_ADMIN_GROUP | 2001 | The last group of administrators cannot be deleted.  
MT_RET_CFG_NOT_EMPTY | 2003 | The group contains accounts or trade operations.  
MT_RET_CFG_INVALID_RANGE | 2004 | Invalid range of accounts or trade operations.  
MT_RET_CFG_NOT_MANAGER_LOGIN | 2005 | The manager account does not belong to the manager group.  
MT_RET_CFG_BUILTIN | 2006 | Built-in protected configuration.  
MT_RET_CFG_DUPLICATE | 2007 | Duplicate configuration.  
MT_RET_CFG_LIMIT_REACHED | 2008 | Reached limit on the number of configurations.  
MT_RET_CFG_NO_ACCESS_TO_MAIN | 2009 | Incorrect network configuration.  
MT_RET_CFG_DEALER_ID_EXIST | 2010 | A dealer with the same ID (account number) already exists.  
MT_RET_CFG_BIND_ADDR_EXIST | 2011 | Connection address already exists.  
MT_RET_CFG_WORKING_TRADE | 2012 | An attempt to delete a working trade server.  
MT_RET_CFG_GATEWAY_NAME_EXIST | 2013 | Gateway with that name already exists.  
MT_RET_CFG_SWITCH_TO_BACKUP | 2014 | Switch to a backup server has been initiated for the Trade/History server.  
MT_RET_CFG_NO_BACKUP_MODULE | 2015 | No backup server.  
MT_RET_CFG_NO_TRADE_MODULE | 2016 | No trade server.  
MT_RET_CFG_NO_HISTORY_MODULE | 2017 | Ho history server.  
MT_RET_CFG_ANOTHER_SWITCH | 2018 | The process of switching to a backup server has already started.  
MT_RET_CFG_NO_LICENSE_FILE | 2019 | No license file.  
MT_RET_CFG_GATEWAY_LOGIN_EXIST | 2020 | Creating a manager configuration is not possible, because the login is already used by the gateway.  
MT_RET_CFG_INVALID_COMPANY | 2021 | The company name does not correspond to the license or White Label. The error is returned when you try to add or save a group with the [company name](../Configuration-Interfaces/Groups/IMTConGroup/Company.md) different from the one specified in the platform license as the main or additional White Label.
