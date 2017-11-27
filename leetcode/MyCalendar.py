# https://leetcode.com/problems/my-calendar-i/description/
class Node:
    
    __slots__ = 'start', 'end', 'left', 'right'
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
        
    def insert(self, node):
        if node.start >= self.end:
            if self.right is None:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if self.left is None:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        n = Node(start, end)
        if self.root is None:
            self.root = n
            return True
        return self.root.insert(n)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
