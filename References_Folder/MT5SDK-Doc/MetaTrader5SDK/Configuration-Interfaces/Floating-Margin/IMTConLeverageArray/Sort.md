[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageArray](../IMTConLeverageArray.md) / Sort

[Previous](Next.md) | [Next](Search.md)

# IMTConLeverageArray::Sort

Sort an array using the passed sort function.
    
    
    MTAPIRES  IMTConLeverageArray::Sort(
       MTSortFunctionPtr  sort_function      // Sort function
       )

### Parameters

**sort_function**  
[in] Pointer to thesort function.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

The arrangement of elements after sorting is determined by the sorting function sort_function.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function comparing elements for sorting                          |
    //+------------------------------------------------------------------+
    int SortParams(const void* left,const void* right)
      {
       IMTConLeverage* lft=*(IMTConLeverage**)left;
       IMTConLeverage* rgh=*(IMTConLeverage**)right;
    //--- compare by value
       return CMTStr::Name(lft->Symbol(), rgh->Name());
      }
    //+------------------------------------------------------------------+
    //| Parameter comparing function for search                          |
    //+------------------------------------------------------------------+
    int SearchParams(const void* left,const void* right)
      {
       LPCWSTR          lft=(LPCWSTR)left;
       IMTConLeverage*  rgh=*(IMTConLeverage**)right;
    //--- compare by value
       return CMTStr::Compare(lft, rgh->Name());
      }
    //+------------------------------------------------------------------+
    //| Sorting and search method example                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTConLeverageArray*  array;
       LPCWSTR               name;
       int                   index;
       ...
    //--- initialize and fill the the 'array' array of parameters
       ...
    //--- sorting
       array->Sort(SortParams);
    //--- Search
       index=array->Search(L"Night Rule",SearchParams);
    //---
       return(0);
      }
