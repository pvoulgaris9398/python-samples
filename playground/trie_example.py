# https://pypi.org/project/trie/
from trie import BinaryTrie as Trie


def main():
    trie = Trie(db={})
    trie.set("Apple", "Apple")
    trie.set("banana", "banana")
    trie.set("app", "app")
    trie.set("bat", "bat")
    trie.set("ball", "ball")

    print("Search Results")
    print("Does 'app' exist?", trie.search("app"))


if __name__ == "__main__":
    main()
