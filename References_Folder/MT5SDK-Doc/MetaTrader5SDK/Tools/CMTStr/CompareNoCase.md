[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / CompareNoCase

[Previous](Compare.md) | [Next](CheckGroupMask.md)

# CMTStr::CompareNoCase

Case insensitive comparison of a string object with the specified string.
    
    
    int  CMTStr::CompareNoCase(
       LPCWSTR  str      // String
       )  const

### Parameters

**str**  
[in] The string, with which you compare the current string object.

### Return Value

If the strings are equal, it returns 0. A value < 0 means that the string object is less than str, a value > 0 means that it's greater than str.

# CMTStr::CompareNoCase

Case insensitive comparison of a string object with the specified string till the specified character.
    
    
    int  CMTStr::CompareNoCase(
       LPCWSTR  str,       // String
       UINT     count      // The number of the character
       )  const

### Parameters

**str**  
[in] The string, with which you compare the current string object.

**count**  
[in] The number of the character, to which the strings are compared. Numbering starts from 0.

### Return Value

If the strings are equal, it returns 0. A value < 0 means that the string object is less than str, a value > 0 means that it's greater than str.

### Note

Compares a string with the specified one, but to the character specified in the count parameter.

# CMTStr::CompareNoCase

Case insensitive comparison of a string object with the specified string object.
    
    
    int  CMTStr::CompareNoCase(
       const CMTStr&  str      // String object
       )  const

### Parameters

**str**  
[in] TheCMTStrstring object, with which you compare the current string object.

### Return Value

If the objects are equal, it returns 0. A value < 0 means that the current string object is less than str, a value > 0 means that it's greater than str.

# CMTStr::CompareNoCase

Case insensitive comparison of two strings.
    
    
    static int  CMTStr::CompareNoCase(
       LPCWSTR  str1,     // A string to compare
       LPCWSTR  str2      // A string to compare
       )

### Parameters

**str1**  
[in] A string to compare.

**str2**  
[in] A string to compare.

### Return Value

If the strings are equal, it returns 0. A value < 0 means that the string str1 is less than str2, a value > 0 means that str1 is greater than str2.

# CMTStr::CompareNoCase

Case insensitive comparison of two strings till the specified character.
    
    
    static int  CMTStr::CompareNoCase(
       LPCWSTR  str1,      // A string to compare
       LPCWSTR  str2,      // A string to compare
       UINT     count      // The number of the character
       )

### Parameters

**str1**  
[in] A string to compare.

**str2**  
[in] A string to compare.

**count**  
[in] The number of the character, to which the strings are compared. Numbering starts from 0.

### Return Value

If the strings are equal, it returns 0. A value < 0 means that the string str1 is less than str2, a value > 0 means that str1 is greater than str2.

### Note

The function compares two strings, but to the character specified in the count parameter.
