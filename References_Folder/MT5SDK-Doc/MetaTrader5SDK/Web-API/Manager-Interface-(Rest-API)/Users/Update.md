[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Update

[Previous](Add.md) | [Next](Delete.md)

# User Update

This request allows to modify a user account record on a trade server.

## Rest API

Request format
    
    
    GET /api/user/update?login=login&rights=rights&group=group&name=name&company=company&language=language&city=city&state=state&zipcode=zipcode&address=address&phone=phone&
    email=email&id=id&status=status&comment=comment&color=color&pass_phone=password&leverage=leverage&agent=account\r\n
     
    POST /api/user/update?login=login&rights=rights&group=group&name=name&company=company&language=language&city=city&state=state&zipcode=zipcode&address=address&phone=phone&
    email=email&id=id&status=status&comment=comment&color=color&pass_phone=password&leverage=leverage&agent=account\r\n
    { Description of a user being created in JSON format }

Response format
    
    
    {
      "retcode" : "0 Done",
      "answer" : { description }
    }

Example
    
    
    //--- request to the server
    POST /api/user/update?login=954402&group=demoforex&name=JohnSmith&leverage=200
    {
      "MQID" : "5CD369A9",
      "Company" : "Individual",
      "Country" : "United States",
      "City" : "New York"
    }
     
    //--- server response
    {
      "retcode" : "0 Done",
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
    
    
    USER_UPDATE|LOGIN=xxxx|RIGHTS=|GROUP=xxxx|NAME=xxxx|
    COMPANY=|LANGUAGE=|CITY=|STATE=|ZIPCODE=|ADDRESS=|PHONE=|EMAIL=|
    ID=|STATUS=|COMMENT=|COLOR=|PASS_PHONE=|LEVERAGE=|AGENT=|\r\n
    Client description in JSON format

Response format
    
    
    USER_UPDATE|RETCODE=xxxx yyyy|\r\n
    The body of the changed client record in JSON format

Example
    
    
    //--- request to the server
    018e00010USER_UPDATE|LOGIN=|RIGHTS=|GROUP=|NAME=Adam Smith|COMPANY=|LANGUAGE=|CITY=|STATE=|ZIPCODE=420000|
    ADDRESS=Street|PHONE=+357 25 875134|EMAIL=|ID=|STATUS=|COMMENT=|COLOR=|PASS_PHONE=|LEVERAGE=|AGENT=|
    //--- server response
    USER_UPDATE|RETCODE=0 Done|LOGIN=1023|
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

  * login — the login of an account which should be updated. This field is required.
  * rights — user permissions. Passed using the [EnUserRights (#enusersrights)](../../../Database-Interfaces/Users/IMTUser/Enumerations.md#enusersrights) enumeration (sum of values of appropriate flags).
  * group — the group to which an account should be moved.
  * name — client's name. The maximum length of a client's symbol name is 128 characters (including the end-of-line character). A longer string will be trimmed up to this length.
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
  * leverage — the size of a client's leverage in the leverage from 1 to 500. Leverage cannot be equal to 0.
  * account — the number of a user's account in an external bank. Corresponds to "Bank account" field in MetaTrader 5 Administrator terminal.
  * agent — the number of an agent account.



After the command parameters, you can specify the description of the changed parameters of the user account record in the JSON format. Parameters of the user record passed in the additional description overwrite parameters passed in the main body of the command. The complete description of the possible user parameters is provided in the ["Data structure"](Data-Structure.md) section.

The JSON description of the user record passed when updating is the same as the description returned by the server. For example:
    
    
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

  * If a parameter value is incorrect, the parameter does not change.
  * The parameters of the users, which cannot be changed from the Web API (for example, CertSerialNumber), also do not change.


  * Client description can be passed in the command parameters, in an additional body in in the JSON format, or both at once.

  
---  
  
## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — updated user parameters in JSON format. The complete description of the passed client parameters is given in the ["Data structure"](Data-Structure.md) section.



## Notes

A user account can be updated only when you are connected to the same trade server where the account is located. If an account with the specified login is not found, code [13](../../../Return-Codes/Common-errors.md) is returned.

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
