[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / FindRChar

[Previous](FindChar.md) | [Next](../CMTSync.md)

# CMTStr::FindRChar

Search for a character in the current string object, starting from the string end. The search is performed in the direction of the string start.
    
    
    int  CMTStr::FindRChar(
       const wchar_t  character      // The character to search for
       )  const

### Parameters

**character**  
[in] The character you want to find.

### Return Value

The position of the character, or a value <0, if the character is not found.

# CMTStr::FindRChar

Search for a character in the specified string, starting from the string end. The search is performed in the direction of the string start.
    
    
    static int  CMTStr::FindRChar(
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
