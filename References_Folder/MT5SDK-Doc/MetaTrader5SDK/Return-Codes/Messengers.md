[🏠 Document Start](../README.md) / [Return Codes](README.md) / Messengers

[Previous](API.md) | [Next](Subscriptions.md)

# Instant messengers

The server returns codes from this group when sending messages via instant messengers.

Constant | Value | Description  
MT_RET_MESSENGER_INVALID_PHONE | 14000 | An invalid phone number is specified. The number must be specified in the format +[country code][number], for example: +74951113594. The should be specified without spaces.  
MT_RET_MESSENGER_NOT_MOBILE | 14001 | A landline phone number is specified instead of a mobile one. Mobile phone numbers must be specified when sending messages. Messages cannot be delivered to other phone numbers.  
  
The codes are used for the following methods:

  * [IMTServerAPI::MessengerSend](../Server-API/Main-API-Interface/Configuration-Databases/Messengers/MessengerSend.md)
  * [IMTAdminAPI::MessengerSend](../Manager-API/Administrator-Interface/Configuration-Databases/Messengers/MessengerSend.md)
  * [IMTManagerAPI::MessengerSend](../Manager-API/Manager-Interface/Users/MessengerSend.md)
  * [/messenger_send](../Web-API/Manager-Interface-(Rest-API)/Configuration-Databases/Messengers/Send-Message.md)


