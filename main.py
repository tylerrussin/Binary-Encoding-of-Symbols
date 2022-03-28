class PriorityQueue():
    '''A specialized queue data structure to 
       to return the lowest frequency count values'''

    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str((i.frequency, i.val)) for i in self.queue])

    def __len__(self):
        return len(self.queue)

    def insert(self, node):
        self.queue.append(node)

    def delete(self):
        # Empty array Edge case
        if len(self.queue) == 0:
            return None

        # Target the value with lowest frequency
        min_freq = 0
        
        for i in range(0, len(self.queue)):
            if self.queue[min_freq].frequency > self.queue[i].frequency:
                min_freq = i

        # Remove from queue
        return self.queue.pop(min_freq)
        

# Binary tree node
class Node():
    def __init__(self, frequency, val, left=None, right=None):
        self.frequency = frequency
        self.val = val
        self.left = left
        self.right = right

# Binary tree
class Tree():
    def __init__(self, head):
        self.head = head

    def __str__(self):
        def printTree(node, level=0):
            if node != None:
                printTree(node.left, level + 1)
                print(' ' * 4 * level + '-> ' + str(node.val))
                printTree(node.right, level + 1)

        printTree(self.head)

    def encode_char(self, char):
        '''Using depth first traversal recursivly till letter is found'''
        def create_path(node, char, path):
            if node != None:
                # Found targert
                if node.val == char:
                    return path

                p1 = create_path(node.left, char, path + '1')    # Left node
                p2 = create_path(node.right, char, path + '0')   # Right node

                # Structure to output targeted path
                if p1:
                    return p1
                if p2:
                    return p2

        path = ''
        path = create_path(self.head, char, path)

        # Output path
        if path:
            return path
        else:
            print('character not valid')
                

if __name__ == '__main__':

    # Sample character string
    char_input = 'ADBADEDBBDD'
    frequency_dict = {}

    # Create frequecny dicitonary
    for char in char_input:
        if char in frequency_dict.keys():
            frequency_dict[char] += 1   # Increment count
        
        else:
            frequency_dict[char] = 1    # Initiate key
    

    # Populate priority queue
    queue = PriorityQueue()
    for key, value in frequency_dict.items():
        queue.insert(Node(value, key))   # Insert nodes of key value pairs

    # Create tree
    while queue.__len__() > 1:
        # Retrive two lowest probabites
        n1 = queue.delete()
        n2 = queue.delete()

        # Insert probabiltiy as a value
        queue.insert(Node(n1.frequency + n2.frequency, 0, left=n1, right=n2))

    # Save head of tree
    encoder = Tree(queue.delete())

    letter = 'E'
    print(encoder.encode_char(letter))
