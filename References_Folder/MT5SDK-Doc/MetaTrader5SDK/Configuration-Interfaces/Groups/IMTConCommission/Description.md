[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / Description

[Previous](Name.md) | [Next](Path.md)

# IMTConCommission::Description

Get the description of commission configuration.

C++
    
    
    LPCWSTR  IMTConCommission::Description()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommission.Description()

Python (Manager API)
    
    
    MTConCommission.Description

### Return Value

If successful, it returns a pointer to a string with the description of the commission configuration. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConCommission](../IMTConCommission.md) object.

# IMTConCommission::Description

Set the description of commission configuration.

C++
    
    
    MTAPIRES  IMTConCommission::Description(
       LPCWSTR  descr      // Description of the configuration
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.Description(
       string   descr      // Description of the configuration
       )

Python (Manager API)
    
    
    MTConCommission.Description

### Parameters

**descr**  
[in] Description of the commission configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of commission configuration description is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
