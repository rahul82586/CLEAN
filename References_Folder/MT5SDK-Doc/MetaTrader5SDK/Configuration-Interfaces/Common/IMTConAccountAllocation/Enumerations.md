[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAllocation](../IMTConAccountAllocation.md) / Enumerations

[Previous](../IMTConAccountAllocation.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConAccountAllocation](../IMTConAccountAllocation.md) contains the following enumerations:

  * [IMTConAccountAllocation::EnFlags (#enflags)](Enumerations.md#enflags)



<a id="enflags"></a>
## IMTConAccountAllocation::EnFlags (#enflags)

IMTConAccountAllocation::EnFlags lists additional account allocation settings.

ID | Value | Description  
FLAG_NONE | 0x00000000 | No flags.  
FLAG_DETAILED_FORM | 0x00000001 | Show extended questionnaire when opening an account. In addition to standard personal details, the questionnaire will require data on nationality, employment, income and trading experience.  
FLAG_REQUIRE_DOCS | 0x00000002 | Request ID and proof-of-address documents.  
FLAG_CONFIRM_PHONE | 0x00000004 | Enable verification of the phone specified when opening an account.  
FLAG_CONFIRM_EMAIL | 0x00000008 | Enable verification of the email specified when opening an account.  
FLAG_START_KYC | 0x00000010 | Automatically start [KYC verification](../../KYC/IMTCon.md) after opening an account.  
AGREEMENT_FLAG_ALL |  | Enumeration end. Corresponds to all flags enabled.  
  
The enumeration is used in the [IMTConAccountAllocation::Flags](Flags.md) method.
