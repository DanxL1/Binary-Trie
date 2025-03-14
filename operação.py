class Node:
    def __init__(self, letter):
        self.letter = letter
        self.left = None
        self.right = None
        self.last = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node("root")
        self.inserted_words = []

    def find(self, word):
        pointer = self.root
        for letter in word:
            if pointer.left is None:
                return False
            current = pointer.left
            while current is not None and current.letter < letter:
                current = current.right
            if current is None or current.letter != letter:
                return False
            pointer = current
        return pointer.last

    def search(self, word):
        pointer = self.root
        for letter in word:
            if pointer.left is None:
                return f"palavra inexistente: {word}"
            current = pointer.left
            while current is not None and current.letter < letter:
                current = current.right
            if current is None or current.letter != letter:
                return f"palavra inexistente: {word}"
            pointer = current
        if not pointer.last:
            return f"palavra inexistente: {word}"
        else:
            pointer.count += 1
            return f"palavra existente: {word} {pointer.count}"
        
    def insert(self, word):
        if self.find(word):
            return f"palavra ja existente: {word}"

        pointer = self.root
        for letter in word:
            if pointer.left is None or pointer.left.letter > letter:
                new_node = Node(letter)
                new_node.right = pointer.left
                pointer.left = new_node
                pointer = new_node
            else:
                prev = None
                current = pointer.left
                while current is not None and current.letter < letter:
                    prev = current
                    current = current.right
                if current is None or current.letter != letter:
                    new_node = Node(letter)
                    new_node.right = current
                    if prev:
                        prev.right = new_node
                    else:
                        pointer.left = new_node
                    pointer = new_node
                else:
                    pointer = current

    
        end_node = Node('*')
        end_node.right = pointer.left
        pointer.left = end_node
        pointer.last = True  # Marca o nó da última letra como terminal

        self.inserted_words.append(word)
        return f"palavra inserida: {word}"

    def search_counter(self):
        if not self.inserted_words:
            return "trie vazia"

        max_count = 0
        max_words = []
        for word in self.inserted_words:
            pointer = self.root
            for letter in word:
                current = pointer.left
                while current is not None and current.letter < letter:
                    current = current.right
                pointer = current
            if pointer.count > max_count:
                max_count = pointer.count
                max_words = [word]
            elif pointer.count == max_count:
                max_words.append(word)

        max_words.sort()
        output = ["palavras mais consultadas:"]
        output.extend(max_words)
        output.append(f"numero de acessos: {max_count}")
        return "\n".join(output)

    def prefix_search(self, prefix):
        if not self.inserted_words:
            return f"palavras com prefixo: {prefix}\ntrie vazia"

        output = [f"palavras com prefixo: {prefix}"]
        sorted_words = sorted(self.inserted_words)  # Ordena as palavras
        for word in sorted_words:
            if word.startswith(prefix):
                output.append(word)
        return "\n".join(output)

    def suffix_search(self, suffix):
        if not self.inserted_words:
            return f"palavras com sufixo: {suffix}\ntrie vazia"

        output = [f"palavras com sufixo: {suffix}"]
        sorted_words = sorted(self.inserted_words)  # Ordena as palavras
        for word in sorted_words:
            if word.endswith(suffix):
                output.append(word)
        return "\n".join(output)

    def print_trie(self):
        if not self.root.left:
            return "trie vazia"

        output = []

        def traverse(node):
            if node is None:
                return
            
            left_letter = node.left.letter if node.left else "nil"
            right_letter = node.right.letter if node.right else "nil"

            output.append(f"letra: {node.letter} fesq: {left_letter} fdir: {right_letter}")

            traverse(node.left)
            traverse(node.right)

        traverse(self.root.left)

        return "\n".join(output)


'''# Testes
if __name__ == "__main__":
    ex = Trie()
    print(ex.insert('casa'))
    print(ex.insert('capa'))
    print(ex.insert('caro'))
    print(ex.insert('carro'))
    print(ex.insert('bala'))
    print(ex.insert('balao'))
    print(ex.search('bala'))
    print(ex.search('carro'))
    print(ex.search('bala'))
    print(ex.prefix_search('ca'))
    print(ex.suffix_search('ro'))
    print(ex.print_trie())'''
