[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / FindR

[Previous](FindNoCase.md) | [Next](FindChar.md)

# CMTStr::FindR

Search for a substring in the current string object, starting from the string end. The search is performed in the direction of the string start.
    
    
    int  CMTStr::FindR(
       LPCWSTR  substring      // Substring to be searched
       )  const

### Parameters

**substring**  
[in] The substring you search for.

### Return Value

The position of the beginning of the substring, or a value <0, if the substring is not found.

### Note

Substring search is case sensitive.

# CMTStr::FindR

Search for a substring in the specified string, starting from the string end. The search is performed in the direction of the string start.
    
    
    static int  CMTStr::FindR(
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
