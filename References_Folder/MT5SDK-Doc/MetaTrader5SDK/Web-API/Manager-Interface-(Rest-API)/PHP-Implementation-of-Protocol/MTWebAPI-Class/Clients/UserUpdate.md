[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Clients](../Clients.md) / UserUpdate

[Previous](UserAdd.md) | [Next](UserDelete.md)

# MTWebAPI::UserUpdate

Change a client account on the server.
    
    
    MTAPIRES  MTWebAPI::UserUpdate(
       MTUser  $user,          // Modifications to a client account
       MTUser  &$new_user      // Modified client account
       )

### Parameters

**$user**  
[in] An object of a client account filled in with the user data that you need to change. The object must first be created using theMTWebAPI::UserCreatemethod.

**& $new_user**  
[out] TheMTUserobject that describes the updated client account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

  * A user account can be updated only when you are connected to the same trade server where the account is located. If an account with the specified login is not found, code [MT_RET_ERR_NOTFOUND](../../../../../Return-Codes/Common-errors.md) is returned.



## Filling Updated User Data

To update a client account, correctly fill in the MTConUser structure with the following parameters:

  * Login — the login of the user account that is being added. In case no login is specified for an account (is equal to 0), the server automatically allocates a login from the available range.
  * Rights — user permissions. Passed using the [EnUserRights (#enusersrights)](../../../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights) enumeration (sum of values of appropriate flags).
  * Group — the group in which the user account should be created. This field is required.
  * Name — client's name. The maximum length of a client's symbol name is 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length. This field is required. 
  * Company — the name of the client's company. The maximum length of the company name is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
  * Language — client's language. Specified in the LANGID format used in the [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) systems (a value from Prim.lang.identifier).
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
  * Leverage — the size of a client's leverage in the leverage from 1 to 500.
  * Account — the number of a user's account in an external bank.
  * Agent — the number of an agent account.


