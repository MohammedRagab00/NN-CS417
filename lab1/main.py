# a1 = [1, 2]
# a2 = [3, 4]
# a3 = {}
#
# for i in range(2):
#     a3[a1[i]] = a2[i]
#
# print(a3)

myList = [5, 2, 3, 4, 6, 1]


# myList.sort()

def my_fun(li, val):
    li.sort()
    l = 0
    r = len(li) - 1
    ans = []
    while l < r:
        if li[l] + li[r] == val:
            ans.append((li[l], li[r]))
            l += 1
            r -= 1
        elif li[l] + li[r] > val:
            r -= 1
        else:
            l += 1
    return ans


print(my_fun(myList, 7))

secondList = [5, 5, 5, 1, 1, 2]


def my_freq(li):
    mi = li[0]
    mp = {}
    for i in li:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
    return mp


print(my_freq(secondList))

# mp = {1:2,3:1}
# print(mp.get(2))
