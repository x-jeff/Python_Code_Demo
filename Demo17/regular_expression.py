import re

a = '23123'
print(a == '23123')

# re.search
print(re.search('1', a))
print(re.search('23', a))
print(re.search('1', a).span())
print(re.search('23', a).span())

print(re.search('[0123]', a))
print(re.search('[13]', a))
print(re.search('[0-9]', a))
print(re.search('\d', a))

print(re.search('4', a))

a = 'cdbapa'
print(re.search('a', a))
print(re.search('[abcdefghijklmnopqrstuvwxyz]', a))
print(re.search('[a-z]', a))
b = 'A'
print(re.search('[a-z]', b))
print(re.search('[a-zA-Z]', b))
b = 'A4'
print(re.search('[a-zA-Z0-9]', b))
print(re.search('\w', b))

a = 'abc'
print(re.search('\w', a))
print(re.search('\w{2}', a))
print(re.search('\w{3}', a))
print(re.search('[acdf]', a))
print(re.search('[acabdf]{2}', a))

b = 'abcdefg'
print(re.search('\w{4,15}', b))
print(re.search('\w{4,6}', b))
print(re.search('\w{4,15}', a))
print(re.search('\w+', b))
b = 'a'
print(re.search('\w+', b))
b = ''
print(re.search('\w+', b))
print(re.search('\w*', b))

a = 'my phone is 134-1234-1234'
print(re.search('\d{3}-\d{4}-\d{4}', a))
b = 'my phone is 13412341234'
print(re.search('\d{3}-{0,1}\d{4}-{0,1}\d{4}', a))
print(re.search('\d{3}-{0,1}\d{4}-{0,1}\d{4}', b))
print(re.search('\d{3}-?\d{4}-?\d{4}', a))
print(re.search('\d{3}-?\d{4}-?\d{4}', b))

# re.match
email = 'david@largidata.com'
print(re.match('\w+@\w+', email))

m = re.match('(\w+)@(\w+)', email)
print(m)
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.groups())
print(m.groups()[0])
print(m.groups()[1])

m = re.match('(\w+)@([a-z\.]+)', email)
print(m.groups())
m = re.match('(\w+)@(.+)', email)
print(m.groups())

digit = '1999.5'
m = re.match('(\d+)\.(\d+)', digit)
print(m.groups())

name = 'David Chiu'
m = re.match('(\w+) (\w+)', name)
print(m.group(1))
print(m.group(2))
m = re.match('(?P<first_name>\w+) (?P<last_name>\w+)', name)
print(m.group('first_name'))
print(m.group('last_name'))

str1 = 'scp file.txt root@10.0.0.1:./'
m = re.search('^scp ([\w\.]+) (\w+)@([\w\.]+):(.+)', str1)
print(m)

s = '123 abc'
print(re.search('^[0-9]', s))
print(re.search('^[0-9]{2}', s))
print(re.search('^[2-9]', s))
print(re.search('^[a-z]', s))
print(re.search('[0-9]$', s))
print(re.search('[a-z]$', s))
