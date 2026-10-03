[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / Find

[Previous](CheckGroupMask.md) | [Next](FindNoCase.md)

# CMTStr::Find

Search for a substring in the current string object, starting at the specified position.
    
    
    int  CMTStr::Find(
       LPCWSTR  substring,     // Substring to be searched
       UINT     startpos       // Position
       )  const

### Parameters

**substring**  
[in] The substring you search for.

**startpos**  
[in] The position in a string object, from which search will begin. The numbering starts from zero, the search is carried out by the end of the string.

### Return Value

The position of the beginning of the substring, or a value <0, if the substring is not found.

### Note

Substring search is case sensitive.

# CMTStr::Find

Search for a substring in the current string object, starting at the zero position.
    
    
    int  CMTStr::Find(
       LPCWSTR  substring      // Substring to be searched
       )  const

### Parameters

**substring**  
[in] The substring you search for.

### Return Value

The position of the beginning of the substring, or a value <0, if the substring is not found.

### Note

Substring search is case sensitive.

# CMTStr::Find

Search for a substring in the specified string, starting at the specified position.
    
    
    static int  CMTStr::Find(
       LPCWSTR  str,        // String
       LPCWSTR  substr      // Substring to be searched
       )

### Parameters

**str**  
[in] The string, in which you want to find a substring.

**substr**  
[in] The substring you search for.

### Return Value

The position of the beginning of the substring, or a value <0, if the substring is not found.

### Note

Substring search is case sensitive.
