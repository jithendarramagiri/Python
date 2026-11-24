lst = [1,2,3,4,5,1,2,1]
freq = {}
for num in lst:
    if num in freq:
        freq[num] =  freq[num] + 1
    else:
        freq[num] = 1
print(freq)
s = " red car blue car black car"
words = s.split()
print(words)
f = {}
mos_rep_word = ""
max = 0
for word in words:
    if word in f:
        f[word] += 1
    else:
        f[word] = 1
print(f)
for key in f :
    if f[key] > max:
        max = f[key]
        mos_rep_word = key
