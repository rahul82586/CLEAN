[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessenger](../IMTConMessenger.md) / Enumerations

[Previous](../IMTConMessenger.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConMessenger](../IMTConMessenger.md) class contains the following enumerations:

  * [IMTConMessenger::EnFlags (#enflags)](Enumerations.md#enflags)
  * [IMTConMessenger::EnProviderType (#enprovidertype)](Enumerations.md#enprovidertype)



<a id="enflags"></a>
## IMTConMessenger::EnFlags (#enflags)

The IMTConMessenger::EnFlags enumeration contains messenger configuration flags.

Identifier | Value | Description  
FLAG_NONE | 0 | No flags.  
FLAG_ENABLED | 1 | The messenger configuration is enabled. If the flag is not set, messages will not be sent via this messenger.  
FLAG_DEFAULT | 2 | The default messenger. If email verification is enabled in account allocation settings, but the messenger is not explicitly specified for the appropriate group, the platform will check the list of messengers and will send messages using the first available configuration with FLAG_DEFAULT.  
FLAG_FIRST |  | Beginning of enumeration. Corresponds to FLAG_NONE.  
FLAG_ALL |  | End of enumeration. All flags are enabled.  
  
The enumeration is used in the [IMTConMessenger::Flags](Flags.md) methods.

<a id="enprovidertype"></a>
## IMTConMessenger::EnProviderType (#enprovidertype)

Supported messaging service providers are enumerated in IMTConMessenger::EnProviderType.

Identifier | Value | Description  
SMS providers  
PROVIDER_SMS_BULKSMS | 0 | [BulkSMS](https://www.bulksms.com/)  
PROVIDER_SMS_CLICKATELL | 1 | [Clicatell](https://www.clickatell.com/)  
PROVIDER_SMS_WEBSMS | 2 | [WEBSMS](https://www.websms.ru/)  
PROVIDER_SMS_TWILIO | 3 | [Twilio](https://www.twilio.com/)  
PROVIDER_SMS_CMCOM | 4 | [CM.com](https://www.cm.com/)  
PROVIDER_SMS_VONAGE | 5 | [Vonage](https://www.vonage.com)  
PROVIDER_SMS_INFOBIP | 6 | [Infobip](https://www.infobip.com)  
PROVIDER_SMS_FONIVA | 7 | [Foniva](https://www.foniva.com.tr/)  
PROVIDER_SMS_FIRST |  | The beginning of the SMS providers enumeration. Corresponds to PROVIDER_SMS_BULKSMS.  
PROVIDER_SMS_LAST | 99 | The end of the SMS providers enumeration.  
Instant messengers  
PROVIDER_IM_TELEGRAM | 100 | [Telegram](https://telegram.org/)  
PROVIDER_IM_WHATSAPP | 101 | [WhatsApp](https://www.whatsapp.com/)  
PROVIDER_IM_VIBER | 102 | [Viber](https://www.viber.com/)  
PROVIDER_IM_FIRST |  | The beginning of the IM enumeration. Corresponds to PROVIDER_IM_TELEGRAM.  
PROVIDER_IM_LAST | 199 | The end of the IM enumeration.  
Push notification services  
PROVIDER_PUSH_METAQUOTES | 200 | MetaQuotes push notification service. Used by platform components.  
PROVIDER_PUSH_UNIVERSAL | 201 | Universal push notification service.  
PROVIDER_PUSH_FIRST |  | Beginning of enumeration of push notification services. Corresponds to PROVIDER_PUSH_METAQUOTES.  
PROVIDER_PUSH_LAST | 299 | End of enumeration of push notification services.  
  
The enumeration is used in the [IMTConMessenger::ProviderType](ProviderType.md) methods.
