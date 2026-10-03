[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserCertCreate

[Previous](UserPasswordChange.md) | [Next](UserCertUpdate.md)

# IMTAdminAPI::UserCertCreate

Create an object of a certificate.

C++
    
    
    IMTCertificate*  IMTAdminAPI::UserCertCreate()

.NET
    
    
    CIMTCertificate  CIMTAdminAPI.UserCertCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTCertificate](../../../Database-Interfaces/Certificates/IMTCertificate.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTCertificate::Release](../../../Database-Interfaces/Certificates/IMTCertificate/Release.md) method of this object.
