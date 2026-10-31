class TreeNode:
    def __init__(self):
        self.d = {}
        self.is_last = False


class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        word = word.lower()
        current_node = self.root
        for char in word:
            if char in current_node.d:
                current_node = current_node.d[char]
            else:
                current_node.d[char] = TreeNode()
                current_node = current_node.d[char]
        current_node.is_last = True
        

    def search(self, word: str) -> bool:
        word = word.lower()
        current_node = self.root
        for char in word:
            if char in current_node.d:
                current_node = current_node.d[char]
            else:
                return False
        if current_node.is_last is True:
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool:
        prefix = prefix.lower()
        current_node = self.root
        for char in prefix:
            if char in current_node.d:
                current_node = current_node.d[char]
            else:
                return False
        if len(current_node.d) > 0 or current_node.is_last is True:
            return True
        return False
        
        