from matplotlib import pyplot as plt

from Post import Post


class ImagePost(Post):
    def __init__(self, owner, path):
        super().__init__(owner)
        self.path = path
        print(self)

    def display(self):
        print("Shows picture") # maybe we don't need to print it!
        img = plt.imread(self.path)
        plt.imshow(img)
        plt.show()
    def __str__(self):
        return self._owner.UN + " posted a picture\n"
