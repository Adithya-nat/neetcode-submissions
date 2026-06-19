class Node:
    def __init__(self):
        self.children = {}
        self.content = None 

class FileSystem:

    def __init__(self):
        self.root = Node()
    
    def getParts(self, path):
        if path == "/":
            return []
        return path.split("/")[1:]
        

    def ls(self, path: str) -> List[str]:
        curr = self.root
        names = self.getParts(path)

        for name in names:
            curr = curr.children[name]
        
        if curr.content is not None:
            return [names[-1]]
        else:
            return sorted(curr.children.keys())


        

    def mkdir(self, path: str) -> None:
        curr = self.root

        for name in self.getParts(path):
            if name not in curr.children:
                curr.children[name] = Node()
            curr=curr.children[name]
        


        

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root
        names = self.getParts(filePath)

        for name in names:
            if name not in curr.children:
                curr.children[name] = Node()
            curr=curr.children[name]
        
        if curr.content is None:
            curr.content = content
        else:
            curr.content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root
        names = self.getParts(filePath)

        for name in names:
            curr=curr.children[name]
        
        return curr.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
