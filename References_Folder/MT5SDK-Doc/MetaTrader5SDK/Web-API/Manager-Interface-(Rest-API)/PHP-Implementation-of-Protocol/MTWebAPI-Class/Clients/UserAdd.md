[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Clients](../Clients.md) / UserAdd

[Previous](UserCreate.md) | [Next](UserUpdate.md)

# MTWebAPI::UserAdd

Create a client account on the server.
    
    
    MTAPIRES  MTWebAPI::UserAdd(
       MTUser  $user,          // The client account you are creating
       MTUser  &$new_user      // The created client account
       )

### Parameters

**$user**  
[in] An object of a client account filled in with the data of the user that you need to create. The object must first be created using theMTWebAPI::UserCreatemethod.

**& $new_user**  
[out] TheMTUserobject that describes the created client account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

  * In case there are no more available ranges of logins, the [MT_RET_USR_LOGIN_EXHAUSTED](../../../../../Return-Codes/User-management.md) error is returned.
  * You can add a user on a trade server only when connecting to this trade server. When trying to add a user on a different server, error [MT_RET_USR_LOGIN_PROHIBITED](../../../../../Return-Codes/User-management.md) is returned.
  * When calling the method, a check is made whether the entry already exists. If the account already exists, the [MT_RET_USR_LOGIN_EXIST](../../../../../Return-Codes/User-management.md) error is returned. The key field for comparison is the user login.
  * Before adding, the correctness of the record is checked. If the record is incorrect, the error code [MT_RET_ERR_PARAMS](../../../../../Return-Codes/Common-errors.md) is returned.
  * The error code [MT_RET_USR_INVALID_PASSWORD](../../../../../Return-Codes/User-management.md) is returned if the password of the new client is incorrect (not complex enough or does not meet the minimum length requirement specified for the client group).
  * The error code [MT_RET_ERR_PERMISSIONS](../../../../../Return-Codes/Common-errors.md) is returned in the following cases:


  * The [manager account](../../../Text-Protocol-(Raw-API)/Authentication.md#client-start) does not have a permission for editing accounts
  * The manager account does not have a permission for the group, where the account is being created
  * The group, to which the account is being added, does not exist on the server



## Filling Data of the New Client

To add a client account, correctly fill in the MTUser structure with the following parameters

  * Login — the login of the user account that is being added. In case no login is specified for an account (is equal to 0), the server automatically allocates a login from the available range.
  * Pass_main — the master password of the account. The password must contain at least two of three types of characters (lower case, upper case and digits) and meet the minimum length requirements set for the [group](../../../Configuration-Databases/Groups.md). This field is required.
  * Pass_invsetor — the investor password of the account. The password must contain at least two of three types of characters (lower case, upper case and digits) and meet the minimum length requirements set for the [group](../../../Configuration-Databases/Groups.md). This field is required.
  * Rights — user permissions. Passed using the [EnUserRights (#enusersrights)](../../../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights) enumeration (sum of values of appropriate flags).
  * Group — the group in which the user account should be created. This field is required.
  * Name — client's name. The maximum length of a client's symbol name is 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length. This field is required. 
  * Company — the name of the client's company. The maximum length of the company name is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
  * Language — client's language. Specified in the LANGID format used in the [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) systems (value from Prim.lang.identifier).
  * Country — client's country of residence.
  * City — client's city of residence.
  * State — client's state (region) of residence.
  * Zipcode — client's zip code.
  * Address — the address of the client. The maximum length of the address is 128 characters (including the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.
  * Phone — client's phone number.
  * Email — the email address of the client.
  * ID — the number of a client's identity document.
  * Status — client's status
  * Comment — a comment to the user. The maximum comment length is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
  * Color — the color of the client's requests shown when handling the requests via the manager terminal.
  * Pass_phone — client's phone password.
  * Leverage — the size of a client's leverage in the leverage from 1 to 500. This field is required.
  * Account — the number of a user's account in an external bank.
  * Agent — the number of an agent account.


