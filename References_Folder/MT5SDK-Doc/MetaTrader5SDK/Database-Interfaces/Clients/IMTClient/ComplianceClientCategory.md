[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClient](../IMTClient.md) / ComplianceClientCategory

[Previous](ComplianceApprovedBy.md) | [Next](ComplianceDateApproval.md)

# IMTClient::ComplianceClientCategory

Get the client compliance category, i.e. client classification based on the regulatory rules.

C++
    
    
    LPCWSTR  IMTClient::ComplianceClientCategory()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTClient.ComplianceClientCategory()

### Return Value

If successful, a pointer to a string with the category is returned. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTClient](../IMTClient.md) object.

# IMTClient::ComplianceClientCategory

Set the client compliance category, i.e. client classification based on the regulatory rules.

C++
    
    
    MTAPIRES  IMTClient::ComplianceClientCategory(
       LPCWSTR       category  // Compliance category
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTClient.ComplianceClientCategory(
       string        category  // Compliance category
       )

### Parameters

**category**  
[in] Client compliance category.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The category length is limited to 64 characters (including the end-of-line character). If a longer string is assigned, it will be trimmed up to this number of characters.
