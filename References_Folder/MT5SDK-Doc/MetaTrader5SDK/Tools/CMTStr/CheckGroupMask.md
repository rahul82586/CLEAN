[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / CheckGroupMask

[Previous](CompareNoCase.md) | [Next](Find.md)

# CMTStr::CheckGroupMask

Check the correspondence of a string to the specified mask.
    
    
    static bool  CMTStr::CheckGroupMask(
       LPCWSTR  groupmask      // Mask
       LPCWSTR  grouplist,     // String
       )

### Parameters

**groupmask**  
[in] Mask. Is specified using characters "*" (any value) and "!" (exception). For example, masks are used to specify groups of accounts: "demo*,!demoforex" - all groups whose names begin with demo, except for the group demoforex.

**grouplist**  
[in] The string to check.

### Return Value

In the case of matching returns true. Otherwise - false.

### Note

The function compares whether the specified string corresponds to the mask (*). For example, the string "demo/Forex" corresponds to the mask "demo*".
