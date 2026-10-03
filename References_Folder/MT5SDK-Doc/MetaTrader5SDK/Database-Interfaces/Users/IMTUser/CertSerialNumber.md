[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / CertSerialNumber

[Previous](Group.md) | [Next](Rights.md)

# IMTUser::CertSerialNumber

Get the number of the last certificate that was used by the client for authorization.

C++
    
    
    UINT64  IMTUser::CertSerialNumber()  const

.NET (Gateway/Manager API)s
    
    
    ulong  CIMTUser.CertSerialNumber()

### Return Value

The number of the last certificate that was used by the client for authorization.

### Note

Certificates are used in the [extended authorization](../../../Configuration-Interfaces/Groups/IMTConGroup/AuthMode.md) mode.
