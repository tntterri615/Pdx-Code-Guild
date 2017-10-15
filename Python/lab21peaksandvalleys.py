# # return the indices of peaks
#
# def peaks(data):
#     p = []
#     for i in range(1, len(data) - 1):
#         a = data[i - 1]
#         b = data[i]
#         c = data[i + 1]
#         if a < b > c:
#             p.append(i)
#     return p
#
# print(peaks([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]))


# return valleys of indices

# def valleys(data):
#     v = []
#     for i in range(1, len(data) - 1):
#         a = data[i - 1]
#         b = data[i]
#         c = data[i + 1]
#         if a > b < c:
#             v.append(i)
#     return v
#
#
# print(valleys([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]))


# return peaks and valleys

def peaks_and_valleys(data):
    p_v = []
    for i in range(1, len(data) - 1):
        a = data[i - 1]
        b = data[i]
        c = data[i + 1]
        if a < b > c:
            p_v.append(i)
        d = data[i - 1]
        e = data[i]
        f = data[i + 1]
        if d > e < f:
            p_v.append(i)
    return p_v


print(peaks_and_valleys([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]))
