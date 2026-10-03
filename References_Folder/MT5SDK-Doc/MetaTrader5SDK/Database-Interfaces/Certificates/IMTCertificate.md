[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Certificates](../Certificates.md) / IMTCertificate

[Previous](../Certificates.md) | [Next](IMTCertificate/Release.md)

# IMTCertificate

The IMTCertificate class contains the following methods:

Method | Purpose  
---|---  
[Release](IMTCertificate/Release.md) | Delete the current object.  
[Assign](IMTCertificate/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTCertificate/Clear.md) | Clear an object.  
[Open](IMTCertificate/Open.md) | Loads certificate description from a specified file.  
[OpenMemory](IMTCertificate/OpenMemory.md) | Loads certificate description from the memory.  
[Save](IMTCertificate/Save.md) | Saves the certificate to a file.  
[Close](IMTCertificate/Close.md) | Closes (unloads) a certificate that was earlier opened by IMTCertificate::Open or IMTCertificate::OpenMemory.  
[Raw](IMTCertificate/Raw.md) | Gets a pointer to the memory to which the certificate is loaded.  
[RawSize](IMTCertificate/RawSize.md) | Gets the amount of the memory occupied by the certificate.  
[IsOpened](IMTCertificate/IsOpened.md) | Checks whether an object interface has an open certificate.  
[IsRoot](IMTCertificate/IsRoot.md) | Checks if the loaded certificate is the root one.  
[IsCA](IMTCertificate/IsCA.md) | Checks the loaded certificate - if it is possible to generate other certificates on its basis.  
[IsEqual](IMTCertificate/IsEqual.md) | Checks if the passed certificate is identical to the loaded one.  
[SerialNumber](IMTCertificate/SerialNumber.md) | Gets the serial number of the loaded certificate.  
[ValidFrom](IMTCertificate/ValidFrom.md) | Gets date since which the loaded certificate is valid.  
[ValidTo](IMTCertificate/ValidTo.md) | Gets date until which the loaded certificate is valid.  
[NameCommon](IMTCertificate/NameCommon.md) | Gets the common name of the loaded certificate.  
[NameIssuer](IMTCertificate/NameIssuer.md) | Get the name of the issuer (vendor) of the loaded certificate.  
[NameOrganization](IMTCertificate/NameOrganization.md) | Gets the name of the organization (O), to which the loaded certificate has been issued.  
[NameOrganizationUnit](IMTCertificate/NameOrganizationUnit.md) | Gets the name of the organization unit (OU), to which the loaded certificate has been issued.  
[NameGiven](IMTCertificate/NameGiven.md) | Gets the name of the person (G), to whom the loaded certificate has been issued.
