[🏠 Document Start](../README.md) / [Return Codes](README.md) / Authentication

[Previous](Common-errors.md) | [Next](Configuration-Management.md)

# Authentication

This group of codes is returned by the server during the authentication of users:

Constant | Value | Description  
MT_RET_AUTH_CLIENT_INVALID | 1000 | Invalid type of the terminal.  
MT_RET_AUTH_ACCOUNT_INVALID | 1001 | Invalid account.  
MT_RET_AUTH_ACCOUNT_DISABLED | 1002 | The account is disabled.  
MT_RET_AUTH_ADVANCED | 1003 | Extended authorization required.  
MT_RET_AUTH_CERTIFICATE | 1004 | Certificate required.  
MT_RET_AUTH_CERTIFICATE_BAD | 1005 | Invalid certificate.  
MT_RET_AUTH_NOTCONFIRMED | 1006 | The certificate is not confirmed.  
MT_RET_AUTH_SERVER_INTERNAL | 1007 | An attempt to connect to a server, which is not an access server.  
MT_RET_AUTH_SERVER_BAD | 1008 | Server is not authenticated.  
MT_RET_AUTH_UPDATE_ONLY | 1009 | Only update is available.  
MT_RET_AUTH_CLIENT_OLD | 1010 | Old client version.  
MT_RET_AUTH_MANAGER_NOCONFIG | 1011 | An appropriate manager configuration hasn't been created for the manager account.  
MT_RET_AUTH_MANAGER_IPBLOCK | 1012 | IP-address is not valid for the manager.  
MT_RET_AUTH_GROUP_INVALID | 1013 | The group is not initialized (you must restart the server).  
MT_RET_AUTH_CA_DISABLED | 1014 | Generation of certificates is disabled.  
MT_RET_AUTH_INVALID_ID | 1015 | Invalid ID or the server is disabled (the server ID should be checked).  
MT_RET_AUTH_INVALID_IP | 1016 | Invalid address (the server IP-address should be checked).  
MT_RET_AUTH_INVALID_TYPE | 1017 | Wrong type of server (server ID and type should be checked).  
MT_RET_AUTH_SERVER_BUSY | 1018 | The server is busy.  
MT_RET_AUTH_SERVER_CERT | 1019 | Invalid server certificate.  
MT_RET_AUTH_ACCOUNT_UNKNOWN | 1020 | Unknown account.  
MT_RET_AUTH_SERVER_OLD | 1021 | Outdated server version.  
MT_RET_AUTH_SERVER_LIMIT | 1022 | The server cannot be connected because of the license restrictions.  
MT_RET_AUTH_MOBILE_DISABLED | 1023 | Connections of mobile devices are not allowed in the license.  
MT_RET_AUTH_MANAGER_TYPE | 1024 | This type of connection is not permitted for manager.  
MT_RET_AUTH_DEMO_DISABLED | 1025 | Creation of demo accounts is disabled.  
MT_RET_AUTH_RESET_PASSWORD | 1026 | Master password must be changed.  
MT_RET_AUTH_OTP_INVALID | 1027 | Invalid [one-time password](https://support.metaquotes.net/en/docs/mt5/platform/administrator/getting_started/server_connect/otp).  
MT_RET_AUTH_OTP_NEED_SECRET | 1028 | No [secret key (#security)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/account_edit#security) is specified for the one-time password.  
MT_RET_AUTH_MIGRATION_MT4 | 1029 | Password change is required after account import from the MetaTrader 4 server.  
MT_RET_AUTH_MIGRATION_MT5 | 1030 | Password change is required after account import from the MetaTrader 5 server.  
MT_RET_AUTH_INVALID_VERIFY | 1031 | Invalid or expired verification code.  
MT_RET_AUTH_VERIFY_BAD_EMAIL | 1032 | Unable to send email verification code.  
MT_RET_AUTH_VERIFY_BAD_PHONE | 1033 | Unable to send phone number verification code.  
MT_RET_AUTH_API_DISABLED | 1034 | Connection via the API is prohibited for the account ([IMTUser::USER_RIGHT_API_ENABLED (#enusersrights)](../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights)).
