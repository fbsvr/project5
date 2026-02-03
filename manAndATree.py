import copy
#first, we take an input for the treewidth and convert to an integer
treewidth = int(input())

#tree consists of 4 parts in total
#put all parts of it into a list
#first of all, the big triangle part of the tree is written bellow
tree = list()
for x in range(treewidth//2):
   if x== treewidth//2 -1:
      tree += [[' ']* 7 + ['/'] +  ['_'] * (treewidth-2) + ['\\'] + [' '] * 7 ]
   else:
      tree +=[[' '] * (treewidth//2 +6 -x) + ['/'] +  [' '] *(2*x) + ['\\'] + [' '] * (treewidth//2 +6 -x) ]
#second and third part of the tree are written bellow, since they're identical, the code is the same
for y in range(treewidth//2-1):
   if y == treewidth//2-2 :
      tree += [[' ']* 7 + ['/'] + ['_'] * (treewidth-2) + ['\\'] + [' ']* 7]
   else:
      tree += [[' '] * (treewidth//2+5-y) + ['/'] + [' '] * (2*y+2) + ['\\'] + [' '] * (treewidth//2+5-y)]
for y in range(treewidth//2-1):
   if y == treewidth//2-2 :
      tree += [[' ']* 7 + ['/'] + ['_'] * (treewidth-2) + ['\\'] + [' ']* 7 ]
   else:
      tree += [[' '] * (treewidth//2+5-y) + ['/'] + [' '] * (2*y+2) + ['\\'] + [' '] * (treewidth//2+5-y)]
#and lastly the part that is not any relevant to the treewidth
for z in range(2):
   tree += [[' '] * (treewidth//2+6) + ['|'] * 2 + [' '] * (treewidth//2+6)]

#the length of the tree is equal to (3*treewidth//2)
#when treewidth is 4, person is bigger than the tree
#but in all other scenarios tree is bigger. when treewidth is 4, the length of the tree is 6 and the length of the person is 8
#for the treewidth is 4, add two other rows to equalize their lengths
if treewidth == 4:
   for i in range(2):
      tree = [[' '] * (treewidth + 14)] + tree

#down below, create the person figure in a list
#all rows of the person are written as one of the characters of the big list
person=list()
person.append([' ', ' ', '_', ' ', ' '])
person.append([' ', '(', ' ', ')', ' '])
person.append([' ', ' ', 'Y', ' ', ' '])
person.append([' ', '/', '|', '\\', ' '])
person.append(['|', ' ', '|', ' ', '|'])
person.append([' ', ' ', '|', ' ', ' '])
person.append([' ', '/', ' ', '\\', ' '])
person.append(['|', ' ', ' ', ' ', '|'])

#when treewidth is 4, the length of the person will be less than the length of the tree
#to make them in the same length, add more rows with blanks
if treewidth != 4:
   person = [[' '] * 5] * (3 * treewidth // 2 - 8) + person

#lastly the part where we move the person from left to right 
for t in range(treewidth + 10): #move the tree treewidth + 10 times
   tree_ = copy.deepcopy(tree) #to not lose the original version of our tree list, create a copy of it
   if treewidth!= 4: 
      for row_index in range(3 * treewidth//2):
         for col_index in range(len(person[0])): #move the person step by step
            if tree[row_index][col_index + t] == ' ':
               tree[row_index][col_index + t] = person[row_index][col_index]#do this movement with changing characters of the list
            num_ = (treewidth-4) //2
            rem_ =row_index % (num_ +1)
            for tree_col_index in range(len(tree[0])): #delete the parts of the person coincide with the blanks of the tree
               if row_index != 3*treewidth//2-1 and row_index != 3*treewidth//2-2 and rem_ != 0 and tree_col_index in range(treewidth//2 +7 -rem_, treewidth//2+7 + rem_):
                  tree[row_index][tree_col_index]= ' ' 
   else:#when treewidth is 4, there is a special occassion
      for row_index in range(len(person)):#since there is no blank in the tree when treewidth is 4, no need to delete the parts of the person coincide with the blanks of the tree
         for col_index in range(len(person[0])): 
            if tree[row_index][col_index + t] == ' ':
               tree[row_index][col_index + t] = person[row_index][col_index]   
   for row in tree:
      for character in row:
         print(character, end='')
      print()#we print every character step by step
   tree = copy.deepcopy(tree_)#turn the tree into its original version

