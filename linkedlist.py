class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.awal = None

    def isEmpty(self):
        return self.awal is None

    def display(self):
        print("Isi Linked List : ", end="")
        if self.isEmpty():
            print("[Data Kosong]")
        else:
            bantu = self.awal
            while bantu is not None:
                print(bantu.info, " ", end="")
                bantu = bantu.next
            print()

    def size(self):
        if self.isEmpty():
            banyakNode = 0
        else:
            bantu = self.awal
            banyakNode = 1
            while bantu.next is not None:
                bantu = bantu.next
                banyakNode = banyakNode + 1
        return banyakNode

    def getFirst(self):
        return self.awal

    def getLast(self):
        if self.isEmpty():
            return None
        else:
            bantu = self.awal
            while bantu.next is not None:
                bantu = bantu.next
            return bantu

    def get(self, index):
        if self.isEmpty() or index<1 or index>self.size():
            return None
        else:
            bantu = self.awal
            posisi = 1
            while posisi<index:
                bantu = bantu.next
                posisi = posisi +1
            return bantu
    def addFirst(self, data):
        newNode = Node(data)
        newNode.next = self.awal
        self.awal = newNode
    def addLast(self, data):
        if self.isEmpty():
            self.addFirst(data)
        else:
            last = self.getLast()
            newNode = Node(data)
            last.next = newNode
    def add(self, index, data):
        if index==1:
            self.addFirst(data)
        elif index>1 and index<=self.size():
            prevNode = self.get(index-1)
            newNode = Node(data)
            newNode.next = prevNode.next
            prevNode.next = newNode
        else:
            print("Posisi Sisip Invalid")
    def update(self,index,data):
        nodeUpdate = self.get(index)
        if nodeUpdate is None:
            print("Data tidak ditemukan")
        else:
            nodeUpdate.info = data
    def removeFirst(self):
        if self.isEmpty():
            print("Penghapusan gagal karena list kosong")
        else:
            first = self.getFirst()
            self.awal = first.next
            del first
    def remove(self, index):
        if self.isEmpty():
            print("Penghapusan gagal karena list kosong")
        else:
            if index==1:
                self.removeFirst()
            else:
                prevNode = self.get(index-1)
                if prevNode is None:
                    print("Penghapusan gagal karena index tidak ditemukan")
                else:
                    deletedNode = prevNode.next
                    prevNode.next = deletedNode.next
                    del deletedNode
    def removeLast(self):
        self.remove(self.size())
