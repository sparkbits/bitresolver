import json
import sys
import argparse

# argv[1] - Mandatory letter
# argv[2] - Set of available letters

class Beeresolver:

    def __init__(self, file):
        self.data = {}
        self.candidates = []
        self.pangram = []
        self.min_len = 3
        with open(file) as json_file:
            self.data = json.load(json_file)

    def findAllWord(self,mandatory,letters,min_len = 3):
        setofletters = list(mandatory) + list(letters)
        self.min_len = min_len
        for key, value in self.data.items():
            index = key
            word = list(index.lower())
            ct = 0
            if mandatory not in word:
                continue
            for letter in word:
                if letter not in setofletters:
                    ct = 0
                    break
                else:
                    ct = ct + 1
            if ct == len(setofletters):
                self.pangram.append(key)
            if ct > self.min_len:
                self.candidates.append(index.lower())
        self.candidates = sorted(self.candidates,key = len)
        self.candidates.reverse()

    def Candidates(self):
        return self.candidates

    def Pangrams(self):
        return self.pangram

    def Printresults(self):
        print("Candidates:")
        print(self.Candidates())
        print("Pangrams:")
        print(self.Pangrams())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Bee Game Resolver v.1.0.0')
    parser.add_argument('-d','--dict',required=True,help="Csv file with words")
    parser.add_argument('-m', '--mainletter',required=True,help="The madatory letter.")
    parser.add_argument('-s', '--setofletters',required=True,help="The set of letters tp be used to build a word")
    args = parser.parse_args()
    bee = Beeresolver(args.dict)
    bee.findAllWord(args.mainletter,args.setofletters)
    bee.Printresults()