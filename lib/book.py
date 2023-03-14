#!/usr/bin/env python3

class Book:
    def __init__(self, title = "That Book", author = "Unknown", page_count = 0, genre = "unknown"):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.genre = genre

    def get_author(self):
        return self._author
    
    def set_author(self, author):
        self._author = author

    author = property(get_author, set_author,)
    
    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        # if (type(page_count) in (int)):
        # if isinstance(page_count, int):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    page_count = property(get_page_count, set_page_count,)

    def get_genre(self):
        return self._genre
    
    def set_genre(self, genre):
        self._genre = genre
    
    genre = property(get_genre, set_genre,)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")