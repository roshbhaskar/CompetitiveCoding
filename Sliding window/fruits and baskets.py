 def totalFruit(self, fruits: List[int]) -> int:
        maps={}
        start=0
        end=0
        count=0
        while(end<len(fruits)):
            if(fruits[end] not in maps):
                maps[fruits[end]]=1
            else:
                maps[fruits[end]]+=1
            #yeha
            # if(len(maps)<2):
            #     end+=1
            if(len(maps)<=2):#this is for k==2
                count=max(count,end-start+1)
                end+=1
            elif(len(maps)>2):
                while(len(maps)>2):
                    maps[fruits[start]]-=1
                    if(maps[fruits[start]]==0):
                        maps.pop(fruits[start])
                    start+=1
                end+=1
        return count
            