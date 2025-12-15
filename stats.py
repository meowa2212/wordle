
def read_file(file_path="words_five.txt"):
    with open(file_path, "r+t", encoding="utf-8") as file:
        return file.read().split()

def main():
    words = read_file()
    occurences = dict()
    for word in words:
        for ch in word:
            if ch not in occurences.keys():
                occurences[ch] = 1
            else:
                occurences[ch] += 1
    
    print(sorted(occurences.items(), key=lambda item: item[1], reverse=True))
    print(len(occurences.keys()))

if __name__ == "__main__":
    main()