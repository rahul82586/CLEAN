[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Enumerations

[Previous](../IMTUser.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTUser](../IMTUser.md) class contains the following enumerations:

  * [IMTUser::EnUsersRights (#enusersrights)](Enumerations.md#enusersrights)
  * [IMTUser::EnUsersPasswords (#enuserspasswords)](Enumerations.md#enuserspasswords)
  * [IMTUser::EnUsersConnectionTypes (#enusersconnectiontypes)](Enumerations.md#enusersconnectiontypes)



<a id="enusersrights"></a>
## IMTUser::EnUsersRights (#enusersrights)

Permissions that can be given to a user are enumerated in IMTUser::EnUsersRights.

ID | Value | Description  
USER_RIGHT_NONE | 0x0000000000000000 | No permissions.  
USER_RIGHT_ENABLED | 0x0000000000000001 | The user is allowed to connect.  
USER_RIGHT_PASSWORD | 0x0000000000000002 | The user is allowed to change the password.  
USER_RIGHT_TRADE_DISABLED | 0x0000000000000004 | Trading is disabled for the user.  
USER_RIGHT_INVESTOR | 0x0000000000000008 | Service value for internal use.  
USER_RIGHT_CONFIRMED | 0x0000000000000010 | User's certificate is confirmed.  
USER_RIGHT_TRAILING | 0x0000000000000020 | The user is allowed to use trailing stop.  
USER_RIGHT_EXPERT | 0x0000000000000040 | The user is allowed to use Expert Advisors.  
USER_RIGHT_OBSOLETE | 0x0000000000000080 | The flag is obsolete and is not used.  
USER_RIGHT_REPORTS | 0x0000000000000100 | The user is allowed to receive daily reports. If the permission is not enabled, daily reports are neither generated nor sent for the account.  
USER_RIGHT_READONLY | 0x0000000000000200 | Service value for internal use.  
USER_RIGHT_RESET_PASS | 0x0000000000000400 | The user must change password during the next connection.  
USER_RIGHT_OTP_ENABLED | 0x0000000000000800 | The user can use OTP authentication.  
USER_RIGHT_SPONSORED_HOSTING | 0x0000000000002000 | Brokers can pay the [virtual hosting](https://www.mql5.com/en/vps) fee for their customers. The service is extremely important for traders, and the opportunity to receive a VPS for free can give them a good reason to choose your company over competitors. The availability of a broker-sponsored VPS is controlled at the individual account level. Only if this flag is enabled, the appropriate payment plan will be shown to the trader in the client terminal. For more details, please read the [appropriate section (#sponsored)](https://support.metaquotes.net/en/docs/community/vps#sponsored).  
USER_RIGHT_API_ENABLED | 0x0000000000004000 | The user is allowed to connect via the [Web API](../../../Web-API/README.md). The flag is obsolete and is not used.  
USER_RIGHT_PUSH_NOTIFICATION | 0x0000000000008000 | The user has enabled [Push notifications from the trade server (#notifications)](https://support.metaquotes.net/en/docs/mt5/client/settings#notifications) in the client terminal. The ability to subscribe to such notifications is defined by the group settings ([IMTConGroup::PERMISSION_NOTIFY_* (#enpermissionsflags)](../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enpermissionsflags)).  
USER_RIGHT_TECHNICAL | 0x0000000000010000 | Permission for convenient work with technical accounts. Disable it for testing accounts to hide them from all managers who do not have special access to technical accounts ([IMTConManager::RIGHT_ACC_TECHNICAL (#enmanagerrights)](../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights)). Such technical accounts can be confusing for the managers working with clients, in which case hiding them can be useful.  The permission affects the visibility in the general list of accounts in the Administrator and Manager terminals, as well as in the list of online accounts in the Manager terminal.  
USER_RIGHT_EXCLUDE_REPORTS | 0x0000000000020000 | Allows excluding an account from [server reports](../../../Configuration-Interfaces/Reports.md). Like the previous permission, it is intended for more convenient work with technical accounts.  
USER_RIGHT_ALL |  | End of enumeration. Corresponds to enabling of all permissions.  
  
This enumeration is used in the [IMTUser::Rights](Rights.md) method.

<a id="enuserspasswords"></a>
## IMTUser::EnUsersPasswords (#enuserspasswords)

Types of passwords are enumerated in IMTUser::EnUsersPasswords.

ID | Value | Description  
USER_PASS_MAIN | 0 | The master password.  
USER_PASS_INVESTOR | 1 | The investor password.  
USER_PASS_API | 2 | API password.  
  
This enumeration is used in the following methods:

  * [IMTAdminAPI::UserPasswordCheck](../../../Manager-API/Administrator-Interface/Users/UserPasswordCheck.md)
  * [IMTAdminAPI::UserPasswordChange](../../../Manager-API/Administrator-Interface/Users/UserPasswordChange.md)
  * [IMTManagerAPI::UserPasswordCheck](../../../Manager-API/Manager-Interface/Users/UserPasswordCheck.md)
  * [IMTManagerAPI::UserPasswordChange](../../../Manager-API/Manager-Interface/Users/UserPasswordChange.md)



<a id="enusersconnectiontypes"></a>
## IMTUser::EnUsersConnectionTypes (#enusersconnectiontypes)

Types of client connections are enumerated in IMTUser::EnUsersConnectionTypes:

ID | Value | Description  
USER_TYPE_CLIENT | 0 | Connection from a client terminal.  
USER_TYPE_CLIENT_WINMOBILE | 1 | Connection from a mobile terminal for Windows Mobile (not used at the moment).  
USER_TYPE_CLIENT_WINPHONE | 2 | Connection from a mobile terminal for Windows Phone 7 (not used at the moment).  
USER_TYPE_CLIENT_API_WEB | 3 | Connection via the client Web API.  
USER_TYPE_CLIENT_IPHONE | 4  | Connection from a mobile terminal for iPhone.  
USER_TYPE_CLIENT_ANDROID | 5 | Connection from a mobile terminal for Android.  
USER_TYPE_CLIENT_BLACKBERRY | 6 | Connection from a mobile terminal for BlackBerry (not used at the moment).  
USER_TYPE_CLIENT_WEB | 11 | Connection from a WebTerminal.  
USER_TYPE_ADMIN | 32 | Connection from an administrator terminal.  
USER_TYPE_MANAGER | 33 | Connection from a manager terminal.  
USER_TYPE_MANAGER_API | 34 | Connection via the manager interface of the Manager API.  
USER_TYPE_ADMIN_API | 36 | Connection via the administrator interface of the Manager API.  
USER_TYPE_MANAGER_API_WEB | 37 | Connection via the [manager Web API](../../../Web-API/README.md).  
USER_TYPE_FIRST |  | Beginning of enumeration. It corresponds to USER_TYPE_CLIENT.  
USER_TYPE_LAST |  | End of enumeration. It corresponds to USER_TYPE_ADMIN_API.  
  
This enumeration is used in the following methods:

  * [IMTUserSink::OnUserLogin](../IMTUserSink/OnUserLogin.md)
  * [IMTUserSink::HookUserLogin](../IMTUserSink/HookUserLogin.md)


