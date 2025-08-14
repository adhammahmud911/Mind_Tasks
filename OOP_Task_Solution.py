# =======================
# Task 1: Reports
# =======================
# 1.1 Difference between Shallow and Deep Copy
# Shallow Copy: Creates a new object but references the same nested objects.
# Deep Copy: Creates a new object and recursively copies all nested objects.

import copy

list1 = [[1, 2], [3, 4]]
shallow = copy.copy(list1)
shallow[0][0] = 99
print("After shallow copy change:", list1)  # Original changed

list1 = [[1, 2], [3, 4]]
deep = copy.deepcopy(list1)
deep[0][0] = 55
print("After deep copy change:", list1)  # Original unchanged

# 1.2 Multiple Inheritance in Python
class Parent:
    def greet(self): print("Hello from Parent")

class Child(Parent):
    def greet(self): print("Hello from Child")

Child().greet()  # Child overrides Parent

class A:
    def greet(self): print("Hello from A")

class B:
    def greet(self): print("Hello from B")

class C(A, B): pass

C().greet()  # Follows MRO (A first)


# =======================
# Task 2: Voting System with Encapsulation
# =======================

class VotingSystem:
    def __init__(self):
        self.__candidates = {}  # encapsulated data

    def add_candidate(self, name):
        if name not in self.__candidates:
            self.__candidates[name] = 0
            print(f"Candidate {name} added.")
        else:
            print("Candidate already exists.")

    def remove_candidate(self, name):
        if name in self.__candidates:
            del self.__candidates[name]
            print(f"Candidate {name} removed.")
        else:
            print("Candidate not found.")

    def vote_to_candidate(self, name):
        if name in self.__candidates:
            self.__candidates[name] += 1
            print(f"Vote added to {name}.")
        else:
            print("Candidate not found.")

    def display_winner(self):
        if not self.__candidates:
            print("No candidates.")
            return
        winner = max(self.__candidates, key=self.__candidates.get)
        print(f"Winner is {winner} with {self.__candidates[winner]} votes.")


# Example usage:
voting = VotingSystem()
voting.add_candidate("Adham")
voting.add_candidate("Ahmed")
voting.vote_to_candidate("Adham")
voting.vote_to_candidate("Adham")
voting.vote_to_candidate("Ahmed")
voting.display_winner()


# =======================
# Task 3: Smartphone Class with Multiple Inheritance
# =======================

class Phone:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Contact {name} added.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} removed.")
        else:
            print("Contact not found.")

    def make_call(self, name):
        if name in self.contacts:
            print(f"Calling {name}...")
        else:
            print("Contact not found.")


class Camera:
    def take_pic(self):
        print("The picture was taken successfully.")


class Smartphone(Phone, Camera):
    pass


# Example usage:
sp = Smartphone()
sp.add_contact("Adham", "12345")
sp.make_call("Adham")
sp.take_pic()
