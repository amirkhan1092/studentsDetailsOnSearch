
print('Welcome to the file handling based Student Details Search ')
print('''
Select the Category 
1. MCA
2. Btech Section E
3. Btech Section J
4. Btech Section X

''')
c = input('enter the choices 1/2/3/4 ')

if c == '1':
    file = 'mca1st.dat'
elif c == '2':
    file = 'sectionE.dat'
elif c == '3':
    file = 'sectionJ.dat'
elif c == '4':
    file = 'sectionX.dat'



a = open(file,'r')

data = a.readlines()
data_t = []
for k in data:
    data_t.append(k.split('\t'))

data_dict = dict(data_t)

name = input('enter the full name of the Student ')

search = data_dict.get(name.upper())
if search:
    print('Name found')
    print(name.upper()+' +91'+search)
else:
    print(search)


a.close()