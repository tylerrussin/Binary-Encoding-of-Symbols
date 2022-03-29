import sys

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
        '''Outputs print statements to print a 
           representation of the current binary tree values'''
        
        # Recursive depth first traversal structure
        def printTree(node, level=0):
            if node != None:
                printTree(node.left, level + 1)                 # Travel left
                print(' ' * 4 * level + '-> ' + str(node.val))  # Print current node
                printTree(node.right, level + 1)                # Travel right

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
            print(char, ' not a valid character')
            sys.exit()

    def encode_string(self, char_string):
        '''Take in raw character string return binary encoded string'''
        output = ''
        for char in char_string:
            output += self.encode_char(char)    # Call char encoding method
        
        return output

    def decode_string(self, encoded_string):
        output = ''
        current_node = self.head
        for val in encoded_string:
            if current_node:
                if current_node.val == None:
                    if val == '1':
                        current_node = current_node.left

                    else:
                        current_node = current_node.right

                    if current_node.val != None:
                        output += current_node.val
                        current_node = self.head
                    
            else:
                print(encoded_string, ' contains an invalid encoded character')
                sys.exit()
        
        return output



                

if __name__ == '__main__':

    # Sample character string
    char_input = 'ABCDEFGHIJKLMNOPQRSTUVWX      YZTHALHDFLJAEIHLJFALHEFSFJALJSFJIEAJFLSJFITIEZZZZEIFHLSSSLADBADEDBBDD'
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
        queue.insert(Node(n1.frequency + n2.frequency, None, left=n1, right=n2))

    # Save head of tree
    encoder = Tree(queue.delete())

    # encoder.__str__()
    string = 'HELLO WORLD'
    print(encoder.encode_string(string))

    string = '10010101110110000011001110000000000011000000111100110'
    print(encoder.decode_string(string))

