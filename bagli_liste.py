class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # a. Veri ekleme
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # b. Indeks değerine göre silme işlemi
    def delete_node_by_index(self, index):
        if index < 0 or index >= self.get_length():
            raise ValueError("Index out of range")
        if index == 0:
            self.head = self.head.next
            return
        current_node = self.head
        for i in range(index-1):
            current_node = current_node.next
        current_node.next = current_node.next.next

    # c. Eleman sayısı döndürme
    def get_length(self):
        current_node = self.head
        length = 0
        while current_node:
            length += 1
            current_node = current_node.next
        return length

    # d. Tersten yazdırma
    def print_reverse(self):
        if self.head is None:
            print("Liste boş")
            return
        current_node = self.head
        prev_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # e. Eleman arama
    def search_node(self, data):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.data == data:
                return index
            index += 1
            current_node = current_node.next
        return None
linked_list = LinkedList()

linked_list.add_node("elma")
linked_list.add_node("armut")
linked_list.add_node("portakal")

print("Listenin uzunluğu:", linked_list.get_length())  # Output: Listenin uzunluğu: 3

linked_list.print_reverse()  # Output: portakal armut elma

print("Aranan elemanın indeksi:", linked_list.search_node("armut"))  # Output: Aranan elemanın indeksi: 1

linked_list.delete_node_by_index(1)

print("Listenin uzunluğu:", linked_list.get_length())  # Output: Listenin uzunluğu: 2

print(linked_list.print_reverse())  # Output: elma portakal

