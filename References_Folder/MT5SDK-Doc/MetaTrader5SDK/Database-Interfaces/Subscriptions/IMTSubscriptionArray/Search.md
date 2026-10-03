[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Subscriptions](../../Subscriptions.md) / [IMTSubscriptionArray](../IMTSubscriptionArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTSubscriptionArray::Search

Search in an array for an element that matches the search key.
    
    
    int  IMTSubscriptionArray::Search(
       const void*        key,               // Sorting key
       MTSortFunctionPtr  sort_function      // A pointer to the search function
       )  const

### Parameters

**key**  
[in] A pointer to the sorting key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to thesearch function.

### Return Value

If successful, the method returns the position of the subscription object that meets the search criteria. Otherwise, -1 is returned.

### Note

For a successful search, an array must first be sorted by calling the [IMTSubscriptionArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Comparison function for sorting subscriptions |
    //+------------------------------------------------------------------+
    int SortSubscriptions(const void* left,const void* right)
      {
       IMTSubscription* lft=*(IMTSubscription**)left;
       IMTSubscription* rgh=*(IMTSubscription**)right;
    //--- Compare by subscription ID
       if(lft->ID()<rgh->ID()) return(-1);
       if(lft->ID()>rgh->ID()) return(1);
    //---
       return(0);
      }
    //+------------------------------------------------------------------+
    //| Subscriptions comparing function for search                      |
    //+------------------------------------------------------------------+
    int SearchSubscriptions(const void* left,const void* right)
      {
       UINT64           lft=(UINT64)left;
       IMTSubscription* rgh=*(IMTSubscription**)right;
    //--- Compare by subscription ID
       if(lft<rgh->ID()) return(-1);
       if(lft>rgh->ID()) return(1);
    //---
       return(0);
      }
    //+------------------------------------------------------------------+
    //| Sorting and search method example                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTSubscriptionArray* array;
       UINT64                recordid;
       int                   index;
       ...
    //--- Initialize and fill the 'array' array of subscriptions
       ...
    //--- Sorting
       array->Sort(SortSubscriptions);
    //--- Search
       recordid=12345;
       index=array->Search(&recordid,SearchSubscriptions);
    //---
       return(0);
      }
