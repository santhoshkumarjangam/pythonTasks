class Bookstore:
    NoofBooks = 0

    def __init__(self, name, author):
        self.name = name
        self.author = author

        Bookstore.NoofBooks+=1

    def display(self):
        print(f"Book Name: {self.name}")
        print(f"Author Name: {self.author}")
        print(f"Number of Books: {Bookstore.NoofBooks}")


B1 = Bookstore("python crash course","eric mathews")
B1.display()

    



