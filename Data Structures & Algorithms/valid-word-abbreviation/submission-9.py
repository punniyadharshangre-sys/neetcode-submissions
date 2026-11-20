class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        length=len(word)
        len_abbr=len(abbr)
        i,j=0,0
        num=''
        while i<length and j<len_abbr:

            if abbr[j].isdigit():
                if abbr[j]=='0':
                    return False
                while j<len_abbr and abbr[j].isdigit()  :
                    num+=abbr[j]
                    j+=1

                i+=int(num)
                num=''
                print(i,j)
            else:
                if abbr[j]==word[i]:
                    i+=1
                    j+=1
                else:
                    return False

        return i==length and j==len_abbr
        


