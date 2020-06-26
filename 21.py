import re   
s= 'mother,father,brother,sisters,cousin'
text = 'brother'
for mm in re.findall(text,s):
    print('Found "%s"' % mm)