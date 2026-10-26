# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.idx = 0
        self.vals = []

        def dfs(items):
            for i in items:
                if i.isInteger():
                    self.vals.append(i.getInteger())
                else:
                    dfs(i.getList())

        dfs(nestedList)  
    
    def next(self) -> int:
        val = self.vals[self.idx]
        self.idx += 1
        return val
    
    def hasNext(self) -> bool:
        return self.idx < len(self.vals)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())