
class Bot():
    def __init__(self, file_path="words_five.txt"):
        with open(file_path, "r+t") as file:
            self.valid_words = file.read().split()
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.valid_chars = [alphabet[:] for x in range(5)]
        self.must_contain = []

    def _handle_black(self, ch: str):
        for i in range(len(self.valid_chars)):
            try:
                if len(self.valid_chars[i]) != 1:
                    self.valid_chars[i].remove(ch)
            except Exception:
                pass

    def _handle_yellow(self, ch: str, pos: int):
        try:
            self.valid_chars[pos].remove(ch)
            self.must_contain.append(ch)
        except Exception:
            pass


    def _handle_green(self, ch: str, pos: int):
        self.valid_chars[pos] = [ch,]

    def parse(self, used_word: str, pattern: str): # used word is a string for pattern b - black y - yellow g - green like yybgb
        for i in range(len(used_word)):
            match pattern[i]:
                case "g":
                    self._handle_green(used_word[i], i)
                case "b":
                    self._handle_black(used_word[i])
                case "y":
                    self._handle_yellow(used_word[i], i)
                    
    def limit(self):
        valid = []
        for word in self.valid_words:
            valid_flag = True
            for i in range(len(self.valid_chars)):
                valid_flag = (word[i] in self.valid_chars[i]) and valid_flag
            for ch in self.must_contain:
                valid_flag = (ch in word) and valid_flag
            if valid_flag:
                valid.append(word)
        self.valid_words = valid



def main():
    game = Bot()
    while len(game.valid_words) > 1:
        print(game.valid_words)
        [print(x) for x in game.valid_chars]
        game.parse(input("word used: ").lower(), input("pattern (b/y/g): "))
        game.limit()
    print(game.valid_words)
    [print(x) for x in game.valid_chars]

if __name__ == "__main__":
    main()