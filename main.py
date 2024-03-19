with open("books/book.txt", 'r') as f:
    content = f.read()
    words = len(content.split())
    d = {}
    for i in content:
        if i not in d:
            if i.isalpha():
                d[i] = 1
        else:
            d[i] +=1
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words were found in the document")
    d = sorted(d.items(), key=lambda x:x[1], reverse=True)
    for i in d:
        if i[0]!= " " or i[0]!= "\n":
            print(f"The '{i[0]}' character was found {i[1]} times")

    print("--- End report ---")
