from operação import Trie, Node  # Importa a classe Trie do arquivo trie.py

def main():
    trie = Trie()

    while True:
        comando = input().strip()

        if comando == 'i':  # Inserção de palavra
            palavra = input().strip()
            print(trie.insert(palavra))

        elif comando == 'c':  # Consulta de palavra
            palavra = input().strip()
            print(trie.search(palavra))

        elif comando == 'f':  # Palavras mais consultadas
            print(trie.search_counter())

        elif comando == 'r':  # Busca por prefixo
            prefixo = input().strip()
            print(trie.prefix_search(prefixo))

        elif comando == 's':  # Busca por sufixo
            sufixo = input().strip()
            print(trie.suffix_search(sufixo))

        elif comando == 'p':  # Impressão da Trie
            print(trie.print_trie())

        elif comando == 'e':  # Fim da execução
            break

if __name__ == "__main__":
    main()
