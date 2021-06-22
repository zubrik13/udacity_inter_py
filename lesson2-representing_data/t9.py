import helper
import operator


def parse_content(content):
    """
    Method to parse data into a hash map,
    where key is a word (str) and val it's number representation (int)
    """
    items = content.split("\n")
    words = {item.split()[0]: int(item.split()[1]) for item in items}

    return words


def make_tree(words):
    """
    Method to transform parser data into a trie DS (keys stored as BST), aka nested hash map
    time complexity : O(M*logN), where M - max. string length, N - number of items,
    search - O(M)
    penalty - storage requirements
    """
    ## creates our root dict()
    trie = dict()

    for word, number in words.items():
        ## create a temporary dict based off our root dict object
        temp_dict = trie

        for letter in word:
            ## update our temporary dict and add our current letter and a sub-dictionary
            temp_dict = temp_dict.setdefault(letter, {})

        ## If our word is finished, add {'$key': 'value'} this tells us our word is finished
        temp_dict[f"${word}"] = number

    return trie


# solution by a teacher - advanced
def predict(tree, numbers):
    """
    Pseudo code:
    1. Find the internal nodes corresponding to the user's supplied letters.
    2. Build a collection of all of the words that could be built starting from any of those internal nodes.
    3. Sort the possible words by their frequency.

    :param tree:
    :param numbers:
    :return:
    """
    leaves = [tree]
    for number in numbers:
        letters = helper.keymap[number]
        leaves = [leaf.get(letter, None) for letter in letters for leaf in leaves]
        while True:
            try:
                leaves.remove(None)
            except ValueError:
                break
    words = {}
    for node in leaves:
        while node:
            letter, child = node.popitem()
            if not isinstance(child, dict):  # We have a word!
                word, frequency = letter[1:], child
                words[word] = frequency
                continue
            leaves.append(child)
    return sorted(words.items(), key=operator.itemgetter(1), reverse=True)


if __name__ == '__main__':
    content = helper.read_content(filename='ngrams-10k.txt')
    # content = "ban 10\nband 5\nbar 14\ncan 32\ncandy 7"

    # PART 1: Parsing a string into a dictionary.
    words = parse_content(content)

    # PART 2: Building a trie from a collection of words.
    tree = make_tree(words)
    # print(tree)

    while True:
        # PART 3: Predict words that could follow
        numbers = helper.ask_for_numbers()
        predictions = predict(tree, numbers)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:10]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break
