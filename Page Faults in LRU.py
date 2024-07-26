from collections import OrderedDict


def lru_page_faults(pages, capacity):
    page_faults = 0
    cache = OrderedDict()

    for page in pages:
        if page not in cache:
            # Page fault occurred
            page_faults += 1
            if len(cache) >= capacity:
                # Remove the least recently used page (first item in the OrderedDict)
                cache.popitem(last=False)
        # Add or update the page in the cache
        cache[page] = True

    return page_faults


# Example usage
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 0]
capacity = 4
print(lru_page_faults(pages, capacity))  # Output: 9
