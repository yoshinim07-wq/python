#with arg with return
'''def convert(s):
  out=''
  for i in s:
    if'a'<=i<='z':
      out+=chr(ord(i)-32)
    else:
      out+=i
  return out
print(convert(input('enter a string:')))'''
#without arg without return      
'''def convert():
  s=input('enter:')
  out=''
  for i in s:
    if'a'<=i<='z':
      out+=chr(ord(i)-32)
    else:
      out+=i
  print(out)
convert()'''
#without arg with return
'''def convert():
  s=input('enter:')
  out=''
  for i in s:
    if'a'<=i<='z':
      out+=chr(ord(i)-32)
    else:
      out+=i
  return out
print(convert())'''

'''class college:
  cname="GCEM"
  cloc="Hoodi"
s1=college()
print(s1.cname,s1.cloc)
print(college.cname)
college.cloc='KR Puram'
print(college.cloc)
print(s1.cloc)
print('changing loc wrt object')
s1.cloc='Hoodi'
print(s1.cloc)
print(college.cloc)'''

'''class college:
  cname="GCEM"
  cloc="Hoodi"
s1=college()
s1.name='Harish'
s1.phone=9900778708
s2=college()
s2.sname='Girish'
s2.phone=8899767546
print(s1.cloc)
s1.cloc='KR Puram'
print('after changing')
print(s1.cloc)
print(s2.cloc)
print(college.cloc)'''

class college:
  def __init__(self,name,phno,usn):
    self.name=name
    self.phno=phno
    self.usn=usn
    
  def display(self):
    print(self.name,self.phno,self.usn)
    
s1=college('Harish','980765','1GD35FF')
s2=college('Girish','234565','1GHY543')
print(s1.name)
print(s2.name)
s1.display()
s2.display()





