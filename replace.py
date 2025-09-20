Text = "Python is Great "
words = Text.split()

for i in range (len(words)):
    if words[i]=="is":
        words[i]="will be"

words = " ".join(words)
print(f"Before Replacing: {Text}")
print(f"After Replacing: {words}")     