[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserCertCreate

[Previous](UserPasswordChange.md) | [Next](UserCertUpdate.md)

# IMTManagerAPI::UserCertCreate

Create an object of a certificate.

C++
    
    
    IMTCertificate*  IMTManagerAPI::UserCertCreate()

.NET
    
    
    CIMTCertificate  CIMTManagerAPI.UserCertCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTCertificate](../../../Database-Interfaces/Certificates/IMTCertificate.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTCertificate::Release](../../../Database-Interfaces/Certificates/IMTCertificate/Release.md) method of this object.
