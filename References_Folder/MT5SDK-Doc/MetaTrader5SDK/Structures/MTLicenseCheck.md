[🏠 Document Start](../README.md) / [Structures](README.md) / MTLicenseCheck

[Previous](MTProxyInfo.md) | [Next](MTTick.md)

# MTLicenseCheck

The MTLicenseCheck structure is used for checking the license. The structure is defined with the one-byte alignment.
    
    
    #pragma pack(push,1)
    struct MTLicenseCheck
      {
       wchar_t           name[128];                             // Name of the license
       int               data_reserved[128];                    // A reserved field for future use
       char              random[256];                           // A random sequence for signature verification
       UINT              random_size;                           // Size of the random sequence
       MTAPIRES          retcode;                               // Result of the license check
       int               result_reserved[128];                  // A reserved field for future use
       char              sign[1024];                            // Signature of the license check results
       UINT              sign_size;                             // Size of the signature to check the license
       int               sign_reserved[64];                     // A reserved field for future use
      };
    #pragma pack(pop)

This structure is used in the following methods:

  * [IMTAdminAPI::LicenseCheck](../Manager-API/Administrator-Interface/Common-Functions/LicenseCheck.md)
  * [IMTManagerAPI::LicenseCheck](../Manager-API/Manager-Interface/Common-Functions/LicenseCheck.md)
  * [IMTGatewayAPI::LicenseCheck](../Gateway-API/Main-Interface/Common-Functions/LicenseCheck.md)



The structure contains the following parameters:

Field | Type | Description  
name | wchar_t | License name. It is filled in by a programmer before the call of LicenseCheck.  
data_reserved | int | A reserved field for future use.  
random | char | A random sequence to check the license. It is filled in by a programmer before the call of LicenseCheck. The length of the random sequence must be at least 64 bytes.  
random_size | UINT | The size of a random sequence. It is filled in by a programmer before the call of LicenseCheck.  
retcode | MTAPIRES | The result of license verification. It is filled in by a MetaTrader 5 server after the call of LicenseCheck.  
result_reserved | int | A reserved field for future use.  
sign | char | Signature of the license check results. It is filled in by a MetaTrader 5 server after the call of LicenseCheck.  
sign_size | UINT | The size of the signature to check the license. It is filled in by a MetaTrader 5 server after the call of LicenseCheck.  
sign_reserved | int | A reserved field for future use.  
  
> [Server API](../Server-API/Main-API-Interface/Common-Functions/LicenseCheck.md) and [Report API](../Server-API/Main-API-Interface/Common-Functions/LicenseCheck.md) also provide the possibility to control the licenses using LicenseCheck methods; MTLicenseCheck structure is not used in them, only the license name is passed. Plugins and reports work directly on the server, and thus they do not need to transmit data over the network to verify the license. Therefore, there is no need to additionally sign data using random sequences.
