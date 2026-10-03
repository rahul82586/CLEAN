[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Messengers](../../Messengers.md) / [IMTConMessengerCountry](../IMTConMessengerCountry.md) / PhoneCode

[Previous](Clear.md) | [Next](MessageTemplate.md)

# IMTConMessengerCountry::PhoneCode

Get a country calling code.

C++
    
    
    LPCWSTR  IMTConMessengerCountry::PhoneCode()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConMessengerCountry.PhoneCode()

Python
    
    
    MTConMessengerCountry.PhoneCode

### Return Value

If successful, the method returns a pointer to a string with the calling code. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConMessengerCountry](../IMTConMessengerCountry.md) object.

# IMTConMessengerCountry::PhoneCode

Set the country calling code.

C++
    
    
    MTAPIRES  IMTConMessengerCountry::PhoneCode(
       LPCWSTR  code      // Country code
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConMessengerCountry.PhoneCode(
       srting   code      // Country code
       )

Python
    
    
    MTConMessengerCountry.PhoneCode

### Parameters

**code**  
[in] Country calling code, including the "+" sign.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
