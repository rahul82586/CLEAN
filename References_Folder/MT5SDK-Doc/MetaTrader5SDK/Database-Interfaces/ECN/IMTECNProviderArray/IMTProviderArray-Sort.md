[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNProviderArray](../IMTProviderArray.md) / IMTProviderArray Sort

[Previous](IMTProviderArray-Next.md) | [Next](IMTProviderArray-Search.md)

# IMTECNProviderArray::Sort

Sort an array using the passed sort function.
    
    
    MTAPIRES  IMTECNProviderArray::Sort(
       MTSortFunctionPtr  sort_function      // sort function
       )

### Parameters

**sort_function**  
[in] A pointer to thesort function.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

Positioning of elements after sorting is determined by sort_function.

### Example
    
    
    //+------------------------------------------------------------------+
    //| The function compares providers for sorting                      |
    //+------------------------------------------------------------------+
    int SortProviders(const void* left,const void* right)
      {
       IMTECNProvider* lft=*(IMTECNProvider**)left;
       IMTECNProvider* rgh=*(IMTECNProvider**)right;
    //--- compare by provider ID
       return CMTStr::Compare(lft->RecordID(), rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| The function compares providers for search                       |
    //+------------------------------------------------------------------+
    int SearchProvider(const void* left,const void* right)
      {
       UINT64          lft=(UINT64)left;
       IMTECNProvider* rgh=*(IMTECNProvider**)right;
    //--- compare by provider ID
       return CMTStr::Compare(lft, rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Sorting and search method example                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTECNProviderArray* array;
       UINT64               recordid;
       int                  index;
       ...
    //--- initializing and filling the array of providers 'array'
       ...
    //--- sort
       array->Sort(SortProviders);
    //--- search
       index=array->Search(12345,SearchProvider);
    //---
       return(0);
      }
