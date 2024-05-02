import json


class FriendsDict:
    def __init__(self,fdict = None):
        self._fdict = fdict if fdict is not None else {}

    def append(self,new_main_friend,amount_of_friends):
        self._fdict[new_main_friend] = [input() for _ in range(amount_of_friends)]

    def get_fdict(self):
        return self._fdict

    def upload(self):
        with open('friends.json','w') as file:
            json.dump(self._fdict,file)

    def download(self):
        with open('friends.json', 'r') as file:
            self._fdict = json.load(file)

test_dict = {}
test = FriendsDict(test_dict)
test.append('a',4)
print(test.get_fdict())
test.upload()
test_2 = FriendsDict()
test_2.download()
print(test_2.get_fdict())