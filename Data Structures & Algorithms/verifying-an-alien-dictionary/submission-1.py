class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash_order={c:i for i,c in enumerate(list(order))}
        length=len(words)
        if length>1:
            i,j=0,1
            while j<length:
                w1,w2=words[i],words[j]
                w1c,w2c=0,0
                case=False
                while w1c<len(w1) and w2c<len(w2):
                    c1,c2=w1[w1c],w2[w2c]
                    if hash_order[c1]<hash_order[c2]:
                        case=True
                        break
                    elif hash_order[c1]==hash_order[c2]:
                        w1c+=1
                        w2c+=1
                    else:
                        return False
                if w1c<len(w1) and not case:
                    return False
                
                i+=1
                j+=1
            return True

        else:
            return True


            
        