from Post import Post
class TextPost(Post):
    def __init__(self, owner, text):
        super().__init__(owner)
        self.text = text
        print(self._owner.UN + "published a post:\n" + self.text)


