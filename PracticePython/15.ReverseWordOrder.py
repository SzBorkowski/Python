def reverse(x):
    newsent = []
    for word in x.split():
        newsent.insert(0,word)
    return " ".join(newsent)

def reverse_v2(x):
  return ' '.join(x.split()[::-1])

sentence = str(input("Write a sentence to reverse it: "))
print(reverse(sentence))
print(reverse_v2(sentence))