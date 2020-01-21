'''
注意append的坑 list1.append（list2）若之后list2改变 则list1加入过的list2也会改变 也就是说 他们公用一块空间
修改：list1.append（list2[:])相当于append的时候复制了一份list2
'''