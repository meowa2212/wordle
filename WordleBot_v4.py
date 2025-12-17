from collections import Counter
from math import log2
from wordfreq import word_frequency

class Bot():
    def __init__(self, file_path_words="words_five.txt", file_path_entropy="entropies_2.txt"):
        with open(file_path_words, "r+t") as file:
            self.words = file.read().split()
        self.guessed = []
        choice = input("Calculate new entropies (y/N): ").lower()
        if choice in ["n", "", " "]:
            with open(file_path_entropy, "r+t") as file:    
                entropies = file.read().split("\n")
            entropies = [x.split() for x in entropies[:len(entropies)-1]]
            self.entropies = [(x[0], float(x[1]), float(x[2])) for x in entropies]
        elif choice == "y":
            self.all_entropy()
            self.save_entropies()
        self.first_round = True

    def save_entropies(self, file_path="entropies_2.txt"):
        with open(file_path, "w+t") as file:
            for i in self.entropies:
                file.write(f"{i[0]} {i[1]} {i[2]}\n")

    def make_pattern(self, word1, word2): # returns a pattern based on two given words
        result = [None] * 5
        remaining = Counter()

        for i in range(5):
            if word2[i] == word1[i]:
                result[i] = 'g'
            else:
                remaining[word1[i]] += 1

        for i in range(5):
            if result[i] is not None:
                continue

            letter = word2[i]
            if remaining[letter] > 0:
                result[i] = 'y'
                remaining[letter] -= 1
            else:
                result[i] = 'b'

        return ''.join(result)

    def limit(self, guess, pattern):
        new_words = []
        for word in self.words:
            if self.make_pattern(word, guess) == pattern:
                new_words.append(word)
        self.words = new_words

    def entropy(self, guess):
        counts = Counter()

        for target in self.words:
            final_pattern = self.make_pattern(target, guess)
            counts[final_pattern] += 1

        total_words = len(self.words)
        result_entropy = sum((c/total_words) * log2(total_words/c) for c in counts.values())
        return result_entropy

    def all_entropy(self):
        entropies = []
        length = len(self.words)
        done = 0
        for word in self.words:
            entropies.append((word, self.entropy(word), word_frequency(word, "en")*10000))
            done += 1
            print(f"{((done/length)*100):.3f}%")
        entropies.sort(key=lambda x: x[1], reverse=True)
        self.entropies = entropies[:]

    def data_screen(self):
        print(f"================= {len(self.words)} words left =================")
        [print(f"{x[0]}: {x[1]:.3f} bits, {x[2]:.5f} freq") for x in self.entropies[0:10]]
        print(f"================= {len(self.guessed)}/6 words guessed ================")
        [print(f"{x[0]}: ex {x[1]:.3f} bits, re: {x[2]:.3f} bits") for x in self.guessed]

    def round(self):
        if self.first_round == False:
            self.all_entropy()
        else:
            self.first_round = False

        self.data_screen()
        previous_words = self.words
        guess = input("guess: ")
        entropy = self.entropy(guess)
        pattern = input("pattern: ")
        self.limit(guess, pattern)
        self.guessed.append((guess, entropy, log2(len(previous_words)/len(self.words))))

def main():
    game = Bot()
    while True:
        game.round()
    


if __name__ == "__main__":
    main()