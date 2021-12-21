s = 'GeeksforGeeks'
s = s.replace('G','P',1)
print(s)

a = '/add 8+3'
a = a.replace('/add','',1)
num = list(map(int,a.split('+')))
print(sum(num))
