text=input("enter a string")
freq={}
for ch in text:
    freq[ch]= freq.get(ch,0)+1
for key, value in freq.items():
    print(key,":",value)