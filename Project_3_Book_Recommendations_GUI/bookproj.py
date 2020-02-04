from breezypythongui import EasyFrame
import tkinter as tk

class GUI(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self)
        EasyFrame.setTitle(self, "Book Recommendations")
        EasyFrame.setResizable(self, True)
        
        self.friendsButton = self.addButton(text="Friends", row=0, column=0, command=self.viewFriends)
        self.addButton(text="Recommend", row=0, column=1, command=self.viewRecommend)
        self.addButton(text="Report", row=0, column=2, command=self.viewReport)

    def viewFriends(self):
        self.num_friends = self.prompterBox(title="Friends", promptString="# of Friends:", inputText="2")
        self.name = self.prompterBox(title="name", promptString="name:")
        self.friends = friends(self.name, self.num_friends)
        friends_string = ""
        for friend in self.friends:
            friends_string += (friend + '\n')
        self.messageBox(title="Friends", message=friends_string)

    def viewRecommend(self):
        print('recommend')

    def viewReport(self):
        print('report')


class FriendsGUI(GUI):

    def __init__(self):
        GUI.__init__(self)
        # EasyFrame.setTitle(self, "Friends")

        self.addLabel(text="reader", row=0, column=0)
        self.readerField = self.addTextField(text="", row=0, column=1)
        self.addLabel(text="number of Friends", row=1, column=0)
        self.friendField = self.addIntegerField(value=0, row=1, column=1)



def report():
    ratings = get_ratings()
    names = list(ratings.keys())
    names.sort()
    report = ''
    
    for name in names:
        report += (name + ':  ' + str(friends(name)) + '\n')
        recommended_books = recommend(name)
        for book in recommended_books:
            report += ('\t' + str(book) + '\n')


    return report




def recommend(name, numFriends=2):
    closest_friends = friends(name, numFriends=numFriends)
    ratings = get_ratings()
    books = get_books()
    
    friend_ratings = {}
    for friend in closest_friends:
        friend_ratings[friend] = ratings[friend]
    
    recommendee_ratings = ratings[name]
    
    recommended_books = []
    for i in range(0, len(books)):
        if recommendee_ratings[i] == 0:
            book_ok = True
            for friend in friend_ratings:
                if friend[i] < 3:
                    book_ok = False

            if book_ok:
                recommended_books.append(books[i])
    
    return recommended_books





def friends(name, numFriends=2):
    ratings = get_ratings()
    recommendee = ratings.pop(name, None)
    friends = {}
    
    for person in ratings:
        product = dot_product(recommendee, ratings[person])
        friends[person] = product
        
    sorted_friends = {}
    for w in sorted(friends, key=friends.get, reverse=True):
        sorted_friends[w] = friends[w]

    closest_friends = []
    for i in range(0, numFriends):
        closest_friends.append(list(sorted_friends.keys()[i]))
    closest_friends.sort()

    return closest_friends





def dot_product(recommendee, recommender):
    product = 0
    
    for i in range(0, len(recommendee)):
        product += (recommendee[i] * recommender[i])

    return product






def get_ratings():
    ratings = {}
    ratings_file = open('ratings.txt', 'r')
    content = ratings_file.readlines()
    ratings_file.close()
    
    for i in range(1, len(content), 2):
        name = content[i - 1].replace('\n', '').lower()
        numbers = content[i].replace('\n', '').split()
        numbers = list(map(int, numbers))
        ratings[name] = numbers
        
    return ratings






def swap_author_names(books):
    new_books = []
    for book in books:
        author = book[0].split()
        author = author[-1:] + author[0: -1]
        new_book = (" ".join(author), book[-1])
        new_books.append(new_book)

    return new_books





def swap_author_names_back(books):
    new_books = []
    for book in books:
        author = book[0].split()
        author = author[1: -1] + author[0:1]
        new_book = (" ".join(author), book[-1])
        new_books.append(new_book)

    return new_books





def get_books():
    books_file = open('booklist.txt', 'r')
    content = books_file.readlines()
    books_file.close()
    
    books = [tuple(line.replace('\n', '').split(',')) for line in content]
    books = swap_author_names(books)    
    books.sort()
    books = swap_author_names_back(books)
    
    return books





def main():
    """ Prints recommendations for all readers """
    
    GUI().mainloop()
        

if __name__ == "__main__":
    main()