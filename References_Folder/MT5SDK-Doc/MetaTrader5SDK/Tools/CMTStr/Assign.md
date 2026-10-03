[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / Assign

[Previous](Refresh.md) | [Next](Format.md)

# CMTStr::Assign

Assign a string from an object to another object.
    
    
    void  CMTStr::Assign(
       const CMTStr  &from      // The string to assign
       )

### Parameters

**& from**  
[in] A pointer to theCMTStrobject, a string from which should be assigned to the current object.

### Note

This method clears the object and assigns a string from the specified object to it.

# CMTStr::Assign

Assign the specified Unicode string to an object.
    
    
    void  CMTStr::Assign(
       LPCWSTR  from      // A string to assign
       )

### Parameters

**from**  
[in] The string that you want to assign to the object.

### Note

This method clears the object and assigns the specified string to it.

# CMTStr::Assign

Assign the specified number of characters form a Unicode string to an object.
    
    
    void  CMTStr::Assign(
       LPCWSTR     from,         // String
       const UINT  from_len      // Number of characters
       )

### Parameters

**from**  
[in] The string, characters from which you want to assign to the object.

**from_len**  
[in] Restrictions on the copied string. No more that from_len characters from the from string are copied to the string object.

### Note

This method clears the object and assigns a string from the specified object to it.

# CMTStr::Assign

Assign the specified ANSI string to an object.
    
    
    void  CMTStr::Assign(
       LPCSTR  from      // A string to assign
       )

### Parameters

**from**  
[in] The ANSI string that you want to assign to the object.

### Note

This method clears the object and assigns a string from the specified object to it.

# CMTStr::Assign

Assign the specified number of characters form an ANSI string to an object.
    
    
    void  CMTStr::Assign(
       LPCSTR      from,         // String
       const UINT  from_len      // Number of characters
       )

### Parameters

**from**  
[in] The string, characters from which you want to assign to the object.

**from_len**  
[in] Restrictions on the copied string. No more that from_len characters from the from string are copied to the string object.

### Note

This method clears the object and assigns a string from the specified object to it.
