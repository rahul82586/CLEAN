[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / FindNoCase

[Previous](Find.md) | [Next](FindR.md)

# CMTStr::FindNoCase

Search for a substring in the current string object, starting from the specified position, ignoring case.
    
    
    int  CMTStr::FindNoCase(
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

# CMTStr::FindNoCase

Search for a substring in the current string object, starting from the zero position, ignoring case.
    
    
    int  CMTStr::FindNoCase(
       LPCWSTR  substring      // Substring to be searched
       )  const

### Parameters

**substring**  
[in] The substring you search for.

### Return Value

The position of the beginning of the substring, or a value <0, if the substring is not found.

# CMTStr::FindNoCase

Search for a substring in the specified string, starting from the specified position, ignoring case.
    
    
    static int  CMTStr::FindNoCase(
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
