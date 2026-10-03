[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConCommission](../IMTConCommission.md) / Name

[Previous](Clear.md) | [Next](Description.md)

# IMTConCommission::Name

Get the name of commission configuration.

C++
    
    
    LPCWSTR  IMTConCommission::Name()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommission.Name()

Python (Manager API)
    
    
    MTConCommission.Name

### Return Value

If successful, it returns a pointer to a string with the name of the commission configuration. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConCommission](../IMTConCommission.md) object.

# IMTConCommission::Name

Set the name of commission configuration.

C++
    
    
    MTAPIRES  IMTConCommission::Name(
       LPCWSTR  name      // Name of the configuration
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommission.Name(
       string   name      // Name of the configuration
       )

Python (Manager API)
    
    
    MTConCommission.Name

### Parameters

**name**  
[in] Name of the commission configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of commission configuration name is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
