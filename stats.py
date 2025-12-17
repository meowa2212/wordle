import pandas as pd
import plotly.express as px


def read_file(file_path="words_five.txt"):
    with open(file_path, "r+t", encoding="utf-8") as file:
        return file.read().split()

def read_freq(file_path="freqs.txt"):
    with open(file_path, "r+t", encoding="utf-8") as file:
        freqs = file.read().split("\n")
    freqs = [tuple(x.split()) for x in freqs[:len(freqs)-1]]
    freqs.sort(key= lambda x: x[1], reverse=True)
    return freqs

def main():
    file = pd.read_csv("kursy.csv", parse_dates=["Data"])
    file.info()
    fig = px.line(file, x='Data', y='Kurs średni')
    fig.update_xaxes(title_text="Data")
    fig.update_yaxes(title_text="Kurs w PLN")
    fig.show()
    # freqs = read_freq()
    # fig = px.bar(x=[x[0] for x in freqs[:100]], y=[x[1] for x in freqs[:100]], template="plotly_dark")
    # fig.show()
    # df = pd.DataFrame({'x': [1,2,3,4,5], 'y': [1,4,9,16,25]})
    # fig = px.scatter(df, x='x', y='y', title= "Punktowy")
    # fig.show()


    # occurences = dict()
    # for word in words:
    #     for ch in word:
    #         if ch not in occurences.keys():
    #             occurences[ch] = 1
    #         else:
    #             occurences[ch] += 1

    # print("nigga" in words)

    # print(sorted(occurences.items(), key=lambda item: item[1], reverse=True))
    # print(sorted(occurences.keys()))



if __name__ == "__main__":
    main()