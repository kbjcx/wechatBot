import os


class A:
    def get(self):
        path = os.path.join("./", "a.pkl")
        print(path)
        print(type(path))
        return path

    def put(self):
        path = os.path.join(self.get(), "sdsdvc")
