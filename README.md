# Fake Account
Package that generates fields for registration accounts based on faker
### Installation
```
pip install git+https://github.com/smnenko/fake_account.git
```
### Example
```py
from fake_account import FakeAccount


if __name__ == '__main__':
    for _ in range(10):
        fa = FakeAccount()
        print(fa.username, fa.password, fa.secret_answer)
```
### License
Fake Account is packaged and distributed using the MIT License which allows for commercial use, distribution, modification and private use provided that all copies of the software contain the same license and copyright.

By the community, for the community.
A passion project by Stanislav Semenenko
