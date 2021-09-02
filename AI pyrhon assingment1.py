Python 3.8.9 (tags/v3.8.9:a743f81, Apr  6 2021, 14:02:34) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a =6; a+=30; a%3; print(a)
0
36
>>> a =20; a+=30; a%3; print(a\)
			 
SyntaxError: unexpected character after line continuation character
>>> a =20; a+=30; a%3; print(a)
2
50
>>> a =20; a+=30; a%=3; print(a)
2
>>> True * False
0
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3) nad (9>3)
 
SyntaxError: invalid syntax
>>> ((6>3) and (7<4) or (18==3) and (9>3)
 True is False
 
SyntaxError: invalid syntax
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in True
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    False in True
TypeError: argument of type 'bool' is not iterable
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> 
>>> #ouestion 3
>>> s1 = "Nice to have it "
>>> s2 = "here"
>>> s3 + s1+s2
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s3 + s1+s2
NameError: name 's3' is not defined
>>> s3 = s1+s2
>>> 
>>> s3
'Nice to have it here'
>>> 
>>> ##question 4
>>> lst= [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a=lst[3][1][2];
>>> print (a)
['hello']
>>> 
>>> #question 4
>>> #question 5
>>> 
>>> ####################
>>> a
['hello']
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a
[1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a.inset(0,s1)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.inset(0,s1)
AttributeError: 'list' object has no attribute 'inset'
>>> a.insert(0,s1)
>>> a.insert(len(a),s2)
>>> 
>>> a
['Nice to have it ', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> ###########################Q.6
>>> numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]
>>> for i in numbers:
	if i == 237:
		print(i)
		break;
	elif i % 2 ==0:
		print(i)

		
386
462
418
344
236
566
978
328
162
758
918
237
>>> ######################################Q7
>>> color_list_1 = set(["White", "Black", "Red"])
>>> color_list_2 = set(["Red", "Green"])
>>> color_list_1.difference(color_list_2)
{'Black', 'White'}
>>> 
>>> #########################################Q8
>>> a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)
SyntaxError: multiple statements found while compiling a single statement
>>> a = int(input("Input an integer : "))
Input an integer :  5
>>> n1 = int( "%s" % a )
>>> n2 = int( "%s%s" % (a,a) )
>>> n3 = int( "%s%s%s" % (a,a,a) )
>>> n1+n2+n3
615
>>> 
>>> #############################################Q9
>>> #Q10
>>> 