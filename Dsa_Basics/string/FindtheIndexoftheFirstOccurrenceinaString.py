def FindtheIndexoftheFirstOccurrenceinaString(haystack,needle):
    for i,v in enumerate(haystack):
        # print(i,v)
        if v == needle[0]:
            if needle == haystack[i : i+ len(needle)]:
                print(i)
    print('-1')

    
haystack = "sadbutsad"
needle = "sad"
print(FindtheIndexoftheFirstOccurrenceinaString(haystack,needle))