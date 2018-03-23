'''
    A program to find whether the url in backload_urls is full, part or none
    author : Akshay Jaitly
    Runtime : O(m*n)
    Used Trie data structure for effective management of 1 million plus queries
    '''
import collections, sys

class TrieNode:
    
    # Trie node class
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.exist = False

class TrieTree:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, value):
        currNode = self.root
        for c in value:
            currNode = currNode.child[c]
        currNode.exist = True
    
    def make_Trie(self, values):
        for value in values:
            self.insert(value)

    def search(self, query):
        currNode = self.root
        matchVal = 0
        for c in query:
            currNode = currNode.child.get(c)
            
            # 16 domains and protocols for matching
            if currNode is None:
                return -1 if matchVal < 16 else 0
            matchVal += 1
        return 1


class Solution:
    # Setting the user input to match with the three possible values
    def urlEquate(self, file=None):
        backload_urls, queries = self.urlInput(file)
        result = []
        Tree = TrieTree()
        Tree.make_Trie(backload_urls)

        for query in queries:
            result.append(Tree.search(query))

        self.urlDiscover(result)

    # User input
    def urlInput(self, file=None):
        backload_urls = input('backload_urls:').split(',') # comma seperation
        queryNum = int(input('No. of queries:'))# No. of queries to be passed
        queries = []
        for i in range(queryNum):
            queries.append(input('Query %d ' % (i + 1)))
        return (backload_urls, queries)

    # urlDiscover function prints whether url is found or not
    def urlDiscover(self, results):
        for result in results:
            if result == 1:
                print('FULL URL FOUND')
            elif result == -1:
                print('NO URL FOUND')
            else:
                print('PARTIAL URL FOUND')

if __name__ == '__main__':
    solution = Solution()
    solution.urlEquate()

