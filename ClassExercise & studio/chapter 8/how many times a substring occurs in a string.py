def my_count(string, substring):
    string_size = len(string)
    substring_size = len(substring)
    count = 0
    for i in range(0,string_size-substring_size+1):
        if string[i:i+substring_size] == substring:
            count+=1
    return count

print(my_count("aaaaaa", "aaa"))