[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Certificates](../Certificates.md) / UserCertCreate

[Previous](../Certificates.md) | [Next](UserCertUpdate.md)

# IMTServerAPI::UserCertCreate

Create an object of a certificate.
    
    
    IMTCertificate*  IMTServerAPI::UserCertCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTCertificate](../../../Database-Interfaces/Certificates/IMTCertificate.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTCertificate::Release](../../../Database-Interfaces/Certificates/IMTCertificate/Release.md) method of this object.
