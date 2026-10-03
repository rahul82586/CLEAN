[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Get OTP Key

[Previous](Confirm-Certificate.md) | [Next](Set-OTP-Key.md)

# Get an OTP key

The request allows receiving a secret key which links the trading account and a one-time password generator.

## Rest API

Request Format
    
    
    GET /api/user/otp_secret/get?login=login
    POST /api/user/otp_secret/get?login=login

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { "OTP_SECRET" : "key" }
    }

The example
    
    
    //--- request to the server
    GET /api/user/otp_secret/get?login=61232
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "OTP_SECRET" : "1230987"}
    }

## Raw API

Request Format
    
    
    USER_OTP_SECRET_GET|LOGIN=login|\r\n

Response Format
    
    
    USER_OTP_SECRET_GET|RETCODE=code description|OTP_SECRET=key|\r\n

## Request Parameters

  * login — the login of the user whose OTP key you want to receive.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * OTP_SECRET — OTP secret key.



## Note

To use the request, we need the [IMTConManager::RIGHT_ACC_MANAGER (#enmanagerrights)](../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights) permission.

The key is a link between the account and the [one-time password generator](https://support.metaquotes.net/ru/docs/mt5/platform/administrator/getting_started/server_connect/otp) it is bound to. The key is represented by a sequence of 16 characters generated based on the data about the device the MetaTrader 5 mobile platform is installed on. Fur further information about the secret key please read the [MetaTrader 5 Administrator Documentation (#security)](https://support.metaquotes.net/ru/docs/mt5/platform/administration/admin_accounts/account_edit#security).
