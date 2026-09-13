
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))
    
    def next(self) -> int:
        self.hasNext()  # ensure top of stack is an integer
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self.stack.extend(reversed(top.getList()))
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

