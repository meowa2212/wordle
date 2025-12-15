
class Wordle_Bot():
    def __init__(self, file_path="words_five.txt"):
        with open(file_path, "r+t") as file:
            self.valid = file.read().split()
            self.yellow = [] # list of chars
            self.green = ["_", "_", "_", "_", "_"] # list of 5 chars for a not know value _

    def limit(self, black):
        valid = []
        for word in self.valid:
            valid_flag = True

            for ch in self.yellow:
                valid_flag = (ch in word) and valid_flag
            
            for ch in black:
                valid_flag = (ch not in word) and valid_flag

            for i in range(len(self.green)):
                if self.green[i] != "_":
                    valid_flag = (word[i] == self.green[i]) and valid_flag

            if valid_flag:
                valid.append(word)
        self.valid = valid

    def expand_yellow(self, yellow_chars: str):
        [self.yellow.append(x) for x in yellow_chars]
    
    def expand_green(self, green_chars: str = "_____"): # for a word like "audio" a viable layout would be "a_di_"
        for i in range(len(green_chars)):
            if green_chars[i] != "_":
                self.green[i] = green_chars[i]

                if green_chars[i] in self.yellow:
                    self.yellow.remove(green_chars[i])
                
# common letters: aesoriltnu
# arose until

def main():
        words = Wordle_Bot()
        while len(words.valid) > 1:
            print(words.valid)
            print(f"{len(words.valid)} valid words")
            black = [x for x in input("new black: ")]
            yellow = [x for x in input("new yellow: ")]
            green = input("new green: ")
            words.expand_yellow(yellow)
            words.expand_green(green)
            words.limit(black)
        print(words.valid)

            
        

if __name__ == "__main__":
    main()