class LongNameDict(dict):# dict,list,file,str,object builtin fun extends
    def Longest_Key(self):
        longest = None
        for key in self:
            if not longest or len(key)> len(longest):
                longest =key
        return longest
longkey = LongNameDict()
longkey['hello']=5
longkey["Longest yet"]= 2
longkey['hello2']='world'
print(longkey.Longest_Key())