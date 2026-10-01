class Solution(object):
    def isValid(self, s):
     
        pairs = { ')': '(',']': '[','}': '{'}
        l=[]
        for i in s:
            if (i=='(' or  i=='[' or i == '{'):
                l.append(i)
            else:
                if (len(l)==0):
                    return False
                else:
                  d= l[-1]
                  if pairs[i]!=d:
                    return False
                l.pop()
        return len(l) == 0