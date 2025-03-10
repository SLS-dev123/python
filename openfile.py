def readfile():
    file = open('app.py.txt')
    content = file.read()
    print(content)
    file.close()
    return
def main():
    readfile()
    return
