"""
Animal Shelter
First In First Out Policy
Users can choose if they want to receive a dog or cat
They can't choose the cat or dog they want
"""
from typing import Optional


class Animal:
    def __init__(self, name: str):
        self.order: Optional[int] = None
        self.name: str = name

    def set_order(self, order: int):
        self.order = order

    def get_order(self) -> int:
        return self.order

    def is_older_than(self, other: "Animal"):
        return self.order < other.order


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class LinkedListNode:
    def __init__(self, value: Animal):
        self.value = value
        self.next = None


class AnimalLinkedList:
    def __init__(self):
        self.head: Optional[LinkedListNode] = None
        self.size: int = 0

    def add_last(self, value: Animal):
        self.size += 1
        if self.head is None:
            self.head = LinkedListNode(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = LinkedListNode(value)

    def remove_first(self) -> Animal:
        tmp = self.head
        if tmp is not None:
            self.size -= 1
        self.head = None if tmp is None else tmp.next
        return tmp.value

    def peek(self) -> Animal:
        return self.head.value if self.head else None

    def __len__(self):
        return self.size


class AnimalQueue:
    def __init__(self):
        self.dogs: Optional[AnimalLinkedList] = AnimalLinkedList()
        self.cats: Optional[AnimalLinkedList] = AnimalLinkedList()
        self.order: int = 0

    def enqueue(self, animal: Animal):
        animal.set_order(self.order)
        self.order += 1
        if isinstance(animal, Dog):
            self.dogs.add_last(animal)
        else:
            self.cats.add_last(animal)

    def dequeue_any(self) -> Animal:
        if len(self.dogs) == 0:
            return self.dequeue_cats()
        elif len(self.cats) == 0:
            return self.dequeue_dogs()
        dog = self.dogs.peek()
        cat = self.cats.peek()
        if dog.is_older_than(cat):
            return self.dequeue_dogs()
        else:
            return self.dequeue_cats()

    def dequeue_dogs(self) -> Animal:
        return self.dogs.remove_first()

    def dequeue_cats(self) -> Animal:
        return self.cats.remove_first()
