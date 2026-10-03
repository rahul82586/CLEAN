[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Set OTP Key

[Previous](Get-OTP-Key.md) | [Next](Sync-with-External-System.md)

# Set an OTP key

The request allows setting a secret key which links the trading account and a one-time password generator.

## Rest API

Request Format
    
    
    GET /api/user/otp_secret/set?login=login&otp_secret=key
    POST /api/user/otp_secret/set
    {
      "Login" : "login",
      "OtpSecret" : "key"
    }

Response Format
    
    
    { "retcode" : "code description" }

The example
    
    
    //--- request to the server
    POST /api/user/otp_secret/set
    {
      "Login" : "61232",
      "OtpSecret" : "1234899311914576"
    }
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    USER_OTP_SECRET_SET|LOGIN=login|OTP_SECRET=key|\r\n

Response Format
    
    
    USER_OTP_SECRET_SET|RETCODE=code description|\r\n

## Request Parameters

  * login — the login of the user for whom you want to set the OTP key.
  * otp_secret or OtpSecret — OTP secret key. For security reasons, it is not recommended to pass the key in the request parameters — instead, pass it in an additional body as OtpSecret.



  * Client description can be passed in the command parameters, in an additional body in the JSON format, or both at once. A description passed in an additional body has higher priority.


  * We strongly urge you against passing passwords in the command parameters since request addresses may be logged/cached by intermediary network devices the request passes through on its way from the client to the server. Always send passwords in an additional request body.

  
---  
  
## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

To use the request, we need the [IMTConManager::RIGHT_ACC_MANAGER (#enmanagerrights)](../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights) permission.

The key is a link between the account and the [one-time password generator](https://support.metaquotes.net/ru/docs/mt5/platform/administrator/getting_started/server_connect/otp) it is bound to. The key is represented by a sequence of 16 characters generated based on the data about the device the MetaTrader 5 mobile platform is installed on. Fur further information about the secret key please read the [MetaTrader 5 Administrator Documentation (#security)](https://support.metaquotes.net/ru/docs/mt5/platform/administration/admin_accounts/account_edit#security).
