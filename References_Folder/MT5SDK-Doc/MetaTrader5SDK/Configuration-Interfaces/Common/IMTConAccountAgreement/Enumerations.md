[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAgreement](../IMTConAccountAgreement.md) / Enumerations

[Previous](../IMTConAccountAgreement.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConAccountAgreement](../IMTConAccountAgreement.md) class contains the following enumerations:

  * [IMTConAccountAgreement::EnCaptionType (#encaptiontype)](Enumerations.md#encaptiontype)
  * [IMTConAccountAgreement::EnFlags (#enflags)](Enumerations.md#enflags)



<a id="encaptiontype"></a>
## IMTConAccountAgreement::EnCaptionType (#encaptiontype)

IMTConAccountAgreement::EnCaptionType lists types of agreements which are shown to clients when opening an account.

ID | Value | Description  
CAPTION_CUSTOM | 0 | Custom agreement.  
CAPTION_CLIENT_AGREEMENT | 1 | Client agreement.  
CAPTION_RISK_DISCLOSURE | 2 | Risk Disclaimer.  
CAPTION_CLIENT_AGREEMENT_AND_RISK_DISCLOSURE | 3 | Client agreement and Risk disclaimer.  
CAPTION_COMPLAINTS_HANDLING_PROCEDURE | 4 | Complaint handling procedure.  
CAPTION_ORDER_EXECUTION_POLICY | 5 | Order execution policy.  
CAPTION_CLIENT_CATEGORISATION_NOTICE | 6 | Client categorization procedure.  
CAPTION_CONFLICTS_OF_INTEREST_POLICY | 7 | Conflict of interest clause.  
CAPTION_DATA_PROTECTION_POLICY | 8 | Data protection policy.  
CAPTION_FIRST |  | Enumeration start. Corresponds to CAPTION_CUSTOM.  
CAPTION_LAST |  | Enumeration end. Corresponds to CAPTION_DATA_PROTECTION_POLICY.  
  
The enumeration is used in the [IMTConAccountAgreement::CaptionType](CaptionType.md) method.

<a id="enflags"></a>
## IMTConAccountAgreement::EnFlags (#enflags)

IMTConAccountAgreement::EnFlags lists additional agreement settings.

ID | Value | Description  
AGREEMENT_FLAG_NONE | 0x00000000 | No flags.  
AGREEMENT_FLAG_MANDATORY | 0x00000001 | The agreement is required. A user cannot open an account without accepting the agreement.  
AGREEMENT_FLAG_ALL |  | Enumeration end. Corresponds to all flags enabled.  
  
The enumeration is used in the [IMTConAccountAgreement::Flags](Flags.md) method.
