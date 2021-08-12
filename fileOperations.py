f = open('wasteland.txt', mode='wt', encoding ='utf-8')
f.write('What are the roots that clutch? ')
f.write('What branches grow \nout of this stony rubbish?')
f.close()
g = open('wasteland.txt', mode='rt', encoding='utf-8')
print(g.read())
print(g.seek(0))
print(g.readline())
print(g.readline())
g.seek(0)
g.readlines()
g.close()

h = open('wasteland.txt', mode='at', encoding='utf-8')
h.writelines(
    ['\nSon of man \n',
     'You cannot say, or guess, ',
     'for you know only, \n',
     'A hepa of broken images, '
     'where the sun beats\n']
)
h.close()