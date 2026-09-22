import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.frequency = 0
        self.word = "" 

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, frequency):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.frequency = frequency
        node.word = word
    
    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        heap = []
        self._collect_words(node, heap)
     
        top_5 = heapq.nsmallest(5, heap, key=lambda x: -x)
        return [word for _, word in top_5]
    
    def _collect_words(self, node, heap):
        if node.is_end:
            heap.append((node.frequency, node.word))
        for child in node.children.values():
            self._collect_words(child, heap)

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, request, priority):
       
        heapq.heappush(self.queue, (-priority, request))
    
    def dequeue(self):
        if not self.queue:
            return None
        _, request = heapq.heappop(self.queue)
        return request

if __name__ == "__main__":
   
    trie = Trie()
    word_list = [
    
    ]
    for word, freq in word_list:
        trie.insert(word, freq)
    

    pq = PriorityQueue()
    
    
    requests = [
        ("app", 0),   
        ("ban", 1),   
        ("ap", 0)     
    ]
    for query, priority in requests:
        pq.enqueue(query, priority)
    
   
    while True:
        query = pq.dequeue()
        if query is None:
            break
        result = trie.autocomplete(query)
        print(f"Запрос: '{query}' -> {result}")
