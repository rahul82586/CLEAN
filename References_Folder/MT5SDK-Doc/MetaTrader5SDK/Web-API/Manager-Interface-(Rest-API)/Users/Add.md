[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Add

[Previous](Data-Structure.md) | [Next](Update.md)

# Adding a User

This request allows to create a user account record on a trade server.

## Rest API

Request format
    
    
    GET /api/user/add?login=login&pass_main=password&pass_investor=password&rights=rights&group=group&name=name&company=company&language=language&city=city&state=state&zipcode=zipcode&
    address=address&phone=phone&email=email&id=id&status=status&comment=comment&color=color&pass_phone=password&leverage=leverage&agent=account
     
    POST /api/user/add?login=login&pass-main=password&pass_investor=password&rights=rights&group=group&name=name&company=company&language=language&city=city&state=state&zipcode=zipcode&
    address=address&phone=phone&email=email&id=id&status=status&comment=comment&color=color&pass_phone=password&leverage=leverage&agent=account
    { Description of a user being created in JSON format }

Response format
    
    
    {
      "retcode" : "0 Done",
      "login" : "login",
      "answer" : { description }
    }

Example
    
    
    //--- request to the server
    POST /api/user/add?group=demoforex&name=JohnSmith&leverage=100
    {
      "PassMain" : "1Ar#pqkj",
      "PassInvestor" : "2Ar#pqkj",
      "MQID" : "5CD369A9",
      "Company" : "Individual",
      "Country" : "United States",
      "City" : "New York"
    }
     
    //--- server response
    {
      "retcode" : "0 Done",
      "login" : "954402",
      "answer" : { 
        "Login" : "954402",
        "Group" : "demoforex",
        "CertSerialNumber" : "0",
        "Rights" : "2531",
        "MQID" : "5CD369A9",
        "Registration" : "1572956466",
        "LastAccess" : "1572956466",
        "LastPassChange" : "1572956466",
        "Name" : "JohnSmith",
        "Company" : "Individual",
    ...
      }
    }

## Raw API

Request format
    
    
    USER_ADD|LOGIN=login|PASS_MAIN=password|PASS_INVESTOR=password|RIGHTS=rights|GROUP=group|NAME=name|COMPANY=company|LANGUAGE=language|CITY=city|STATE=state|ZIPCODE=zipcode|
    ADDRESS=address|PHONE=phone|EMAIL=email|ID=id|STATUS=status|COMMENT=comment|COLOR=color|PASS_PHONE=password|LEVERAGE=leverage|AGENT=agent|\r\n
    Client description in JSON format

Response format
    
    
    USER_ADD|RETCODE=xxxx yyyy|LOGIN=zzzz|\r\n
    The body of the created client record in JSON format

Example
    
    
    //--- request to the server
    01e400010USER_ADD|LOGIN=0|PASS_MAIN=main_password|PASS_INVESTOR=invest_password|RIGHTS=|GROUP=demo\demoforex|
    NAME=New Test Name|COMPANY=|LANGUAGE=|CITY=|STATE=|ZIPCODE=|ADDRESS=|PHONE=|EMAIL=|ID=|STATUS=|COMMENT=|COLOR=|
    PASS_PHONE=|LEVERAGE=|AGENT=|
    //--- server response
    USER_ADD|RETCODE=0 Done|LOGIN=1023|
    {
    "Login" : "1023",
    "Group" : "demo\demoforex",
    "CertSerialNumber" : "0",
    "Rights" : "483",
    "Registration" : "1314700797",
    "LastAccess" : "1314700797",
    "LastIP" : "Unresolved",
    ...
    }

## Request Parameters

  * login — login of the user account that is being added. In case no login is specified for an account (is equal to 0), the server automatically allocates a login from the available range.
  * pass_main or PassMain — master password of the account. The password must contain four character types: lowercase letters, uppercase letters, numbers, and [special characters](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters) (#, @, ! etc.). For example, 1Ar#pqkj. The minimum password length is determined by [group](../Configuration-Databases/Groups.md) settings, while the lowest possible value is 8 characters. The maximum length is 16 characters. This field is required. For security reasons, it is not recommended to pass the password in the request parameters — instead, pass it in an additional body as PassMain.
  * pass_investor or PassInvestor — investor password of the account. The password must contain four character types: lowercase letters, uppercase letters, numbers, and [special characters](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters) (#, @, ! etc.). For example, 1Ar#pqkj. The minimum password length is determined by [group](../Configuration-Databases/Groups.md) settings, while the lowest possible value is 8 characters. The maximum length is 16 characters. This field is required. For security reasons, it is not recommended to pass the password in the request parameters — instead, pass it in an additional body as PassInvestor.
  * rights — user permissions. Passed using the [EnUserRights (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights) enumeration (sum of values of appropriate flags). To allow an account to be used in client terminals, enable the [IMTUser::USER_RIGHT_ENABLED (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights) right for that account.
  * group — group in which the user account should be created. This field is required.
  * name — client's name. The maximum length of a client's symbol name is 128 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length. This field is required. 
  * company — name of the client's company. The maximum length of the company name is 64 characters (including the end-of-line character. A longer string will be trimmed up to this length.
  * language — client's language. Specified in the LANGID format used in the [MS Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318693) (value from Prim.lang.identifier).
  * country — the user's country of residence.
  * city — user's city of residence.
  * state — user's state (region) of residence.
  * zipcode — user's zip code.
  * address — the address of the user. The maximum address length is limited to 128 characters (including the end-of-line character). A longer string will be trimmed up to this length.
  * phone — user's phone number.
  * email — the email address of the user.
  * id — the number of a client's identity document.
  * status — client's status.
  * comment — a comment to the user The comment length is limited to 64 characters (including the end-of-line character). A longer string will be trimmed up to this length.
  * color — the color of the client's requests shown when handling the requests via the manager terminal.
  * pass_phone or PhonePassword — the user's phone password. For security reasons, it is not recommended to pass the password in the request parameters — instead, pass it in an additional body as PhonePassword.
  * leverage — the size of a client's leverage in the leverage from 1 to 500. This field is required.
  * account — the number of a user's account in an external bank. Corresponds to "Bank account" field in MetaTrader 5 Administrator terminal.
  * agent — the number of an agent account.



After the command parameters, you can specify the description of the parameters of the user account record in the JSON format. Parameters of the user record passed in the additional description overwrite parameters passed in the main body of the command. The complete description of the possible user parameters is provided in the ["Data structure"](Data-Structure.md) section.

The JSON description of the user record passed when creating is the same as the description returned by the server. For example:
    
    
    {
    "Login" : "1023",
    "Group" : "demo\demoforex",
    "CertSerialNumber" : "0",
    "Rights" : "483",
    "Registration" : "1314700797",
    "LastAccess" : "1314700797",
    "LastIP" : "0.0.0.0",
    "Name" : "John Smith",
    ...
    }

  * Client description can be passed in the command parameters, in an additional body in the JSON format, or both at once. A description passed in an additional body has higher priority.


  * We strongly urge you against passing passwords in the command parameters since request addresses may be logged/cached by intermediary network devices the request passes through on its way from the client to the server. Always send passwords in an additional request body.

  
---  
  
## Response parameters

  * retcode — if successful, the command returns [a response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * login — the login of the created user.



## Notes

  * In case there are no more available ranges of logins, error [3002](../../../Return-Codes/User-management.md) is returned.
  * You can add a user on a trade server only when connecting to this trade server. When trying to add a user on a different server, error [3003](../../../Return-Codes/User-management.md) is returned.
  * When executing the command, it checks whether the entry already exists. If an account already exists, error [3004](../../../Return-Codes/User-management.md) is returned. The key field for comparison is the user login.
  * Before adding, the correctness of the record is checked. If the entry is incorrect, it returns the error code [3](../../../Return-Codes/Common-errors.md).
  * The error code [3006](../../../Return-Codes/User-management.md) is returned if the password of the new client is incorrect (not complex enough or does not meet the minimum length requirement specified for the client group).
  * The error code [8](../../../Return-Codes/Common-errors.md) is returned in the following cases:


  * The [manager account](../Text-Protocol-(Raw-API)/Authentication.md#client-start) does not have a permission for editing accounts
  * The manager account does not have a permission for the group, where the account is being created
  * The group, to which the account is being added, does not exist on the server



Please pay attention to the [ApiData property (#apidata)](Data-Structure.md#apidata) use specifics. Acceptable fields for each of the property cell (which are always 16):

  * Required fields AppID and ID containing the the application ID and the property ID.
  * One of the fields: ValueInt, ValueUInt or ValueDouble, to determine the cell value type. If several fields are specified, the presence of the fields will be checked in the following order: ValueInt, ValueUInt, ValueDouble. The type of the last one found will be used in this case. For example, to write a value of the 'unsigned' type, specify:


    
    
    {
      ...
      "ApiData": [
        {
          "AppID": "1",
          "ID": "2",
          "ValueUInt": "3",
        },
        ...
      ],
      ...
    }

Accordingly, when using *_get_* methods, take a value from the ValueUInt field of the corresponding cell within the ApiData property.
