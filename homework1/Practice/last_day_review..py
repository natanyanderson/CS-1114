def read_txt_file(txt_file, splitter=None):
    results = []
    for line in txt_file:
        if (splitter == None):
            parts = line.split()
        else:
            parts = line.split(splitter)
        for word in parts:

            if (word.isalpha()):
                word = word.lower()
                results.append(word)
    return results

def get_word_set(txt_filename, csv_filename):

    try:
        txt_file = open(txt_filename, "r")
    except FileNotFoundError:
        return []
    try:
        cvs_file = open(csv_filename, "r")
    except FileNotFoundError:
        return []

    results = []

    txt_list = read_txt_file(txt_file)
    csv_list = read_csv_file(csv_file)

    for word in txt_file:
        if word in csv_list and word not in results:
            results.append(word)
    return results

def main():
    print(get_word_set("cardcaptor.csv", "proust.txt"))

if __name__ == "__main__":
    main()