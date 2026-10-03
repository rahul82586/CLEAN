[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [CMTManagerAPIFactory](../CMTManagerAPIFactory.md) / LicenseCheckManager

[Previous](LicenseCheckAdmin.md) | [Next](../Administrator-Interface.md)

# CMTManagerAPIFactory::LicenseCheckManager

Check whether the Manager API application use is authorized.

C++
    
    
    static MTAPIRES  CMTManagerAPIFactory::LicenseCheckManager(
       IMTManagerAPI*  manager,      // A pointer to the IMTManagerAPI interface
       LPCWSTR         name          // Module name
       )

.NET
    
    
    static MTRetCode  SMTManagerAPIFactory.LicenseCheckManager(
       CIMTManager     manager,      // IMTManagerAPI object
       string          name          // Module name
       )

### Program Parameters

**manager**  
[in] A pointer to theIMTManagerAPIinterface, using which the authorization to use Manager API is checked in the license.

**name**  
[in] The name of the Manager API application, for which the license is checked. A unique module name must be defined in advanced in the program code.

### Return Value

An indication of a successful verification is the [MT_RET_OK](../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Further Note

This factory method is provided for an easier license verification. The full description of the verification algorithm is provided in the section related to the [IMTManagerAPI::LicenseCheck](../Manager-Interface/Common-Functions/LicenseCheck.md) function.

License verification can only be performed after [connection to a server](../Manager-Interface/Connection-to-the-Server/Connect.md), otherwise the method will return the [MT_RET_ERR_DATA](../../Return-Codes/Common-errors.md) error.
