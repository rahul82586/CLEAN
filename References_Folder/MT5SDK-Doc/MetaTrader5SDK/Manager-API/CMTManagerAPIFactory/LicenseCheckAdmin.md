[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [CMTManagerAPIFactory](../CMTManagerAPIFactory.md) / LicenseCheckAdmin

[Previous](Version.md) | [Next](LicenseCheckManager.md)

# CMTManagerAPIFactory::LicenseCheckAdmin

Check whether the Manager API application use is authorized.

C++
    
    
    static MTAPIRES  CMTManagerAPIFactory::LicenseCheckAdmin(
       IMTAdminAPI*    admin,        // A pointer to the IMTAdminAPI interface
       LPCWSTR         name          // Module name
       )

.NET
    
    
    static MTRetCode  SMTManagerAPIFactory.LicenseCheckAdmin(
       CIMTAdmin       admin,        // The IMTAdminAPI object
       string          name          // Module name
       )

### Program Parameters

**admin**  
[in] A pointer to theIMTAdminAPIinterface, using which the authorization to use Manager API is checked in the license.

**name**  
[in] The name of the Manager API application, for which the license is checked. A unique module name must be defined in advanced in the program code.

### Return Value

An indication of a successful verification is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Further Note

This factory method is provided for an easier license verification. The full description of the verification algorithm is provided in the section related to the [IMTAdminAPI::LicenseCheck](../Administrator-Interface/Common-Functions/LicenseCheck.md) function.
