class Sentence:
    def __init__(self, plain_text):
        self.words = plain_text.split(' ')
        self.tokens = {}

    def __getitem__(self, item):
        wt = self.WordToken()
        self.tokens[item] = wt
        return self.tokens[item]

    class WordToken:
        def __init__(self, capitalize=False):
            self.capitalize = capitalize

    def __str__(self):
        result = []
        for i in range(len(self.words)):
            w = self.words[i]
            if i in self.tokens and self.tokens[i].capitalize:
                w = w.upper()
            result.append(w)
        return ' '.join(result)