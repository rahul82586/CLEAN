[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / FindChar

[Previous](FindR.md) | [Next](FindRChar.md)

# CMTStr::FindChar

Search for a character in the current string object, starting from the zero position.
    
    
    int  CMTStr::FindChar(
       const wchar_t  character      // The character to search for
       )  const

### Parameters

**character**  
[in] The character you want to find.

### Return Value

The position of the character, or a value <0, if the character is not found.

# CMTStr::FindChar

Search for a character in the specified string, starting from the specified position.
    
    
    static int  CMTStr::FindChar(
       LPCWSTR  str,           
       wchar_t  character      // Character to search for
       )

### Parameters

**str**  
[in] The string, in which you want to find a character.

**character**  
[in] The character you want to find.

### Return Value

The position of the character, or a value <0, if the character is not found.
