

a = open('sectionE.dat','r')

data = a.readlines()
data_t = []
for k in data:
    data_t.append(tuple(k.split('\t')))


data_dict = dict(data_t)

name = input('enter the name of the Student ')

search = data_dict.get(name.upper(),'Not found')
if search != 'Not found':
    print('Name found')
    print(name.upper()+' +91'+search)
else:
    print(search)


a.close()