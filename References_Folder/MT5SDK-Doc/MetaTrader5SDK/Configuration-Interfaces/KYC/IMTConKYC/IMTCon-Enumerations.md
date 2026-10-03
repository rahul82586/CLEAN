[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [KYC](../../KYC.md) / [IMTConKYC](../IMTCon.md) / IMTCon Enumerations

[Previous](../IMTCon.md) | [Next](IMTCon-Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTConKYC](../IMTCon.md) class contains the following enumerations:

  * [IMTConKYC::EnFlags (#enflags)](IMTCon-Enumerations.md#enflags)
  * [IMTConKYC::EnProviderType (#enprovidertype)](IMTCon-Enumerations.md#enprovidertype)



<a id="enflags"></a>
## IMTConKYC::EnFlags (#enflags)

IMTConKYC::EnFlags contains KYC provider configuration flags.

ID | Value | Description  
FLAG_NONE | 0 | No flags.  
FLAG_ENABLED | 1 | The KYC provider configuration is enabled. If the flag is not set, this provider will not be used for automated verifications.  
FLAG_DEFAULT | 2 | Default provider. The platform uses this option when selecting a KYC provider to check client data, if verification based on group or country settings failed.  
FLAG_FIRST |  | Beginning of enumeration. Corresponds to FLAG_NONE.  
FLAG_ALL |  | End of enumeration. Corresponds to enabling of all flags.  
  
The enumeration is used in the [IMTConKYC::Flags](IMTCon-Flags.md) method.

<a id="enprovidertype"></a>
## IMTConKYC::EnProviderType (#enprovidertype)

The IMTConKYC::EnProviderType enumeration contains supported KYC providers.

ID | Value | Description  
PROVIDER_KYC_SUMSUB | 0 | [Sum & Substance](https://sumsub.com/)  
PROVIDER_KYC_WORLD_CHECK | 1 | [World-Check](https://www.refinitiv.com/en/products/world-check-kyc-screening) (currently not supported)  
PROVIDER_KYC_ESPEAR | 2 | [eSpear](https://espear.com/) (currently not supported)  
PROVIDER_KYC_FIRST |  | Beginning of enumeration. Corresponds to PROVIDER_KYC_SUMSUB.  
PROVIDER_KYC_LAST | 299 | End of enumeration. Corresponds to PROVIDER_KYC_ESPEAR.  
  
The enumeration is used in the [IMTConKYC::ProviderType](IMTCon-ProviderType.md) method.
