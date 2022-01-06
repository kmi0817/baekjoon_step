class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        updated_paragraph = ""
        for char in paragraph :
            if char.isalpha() :
                updated_paragraph += char
            elif char.isspace() :
                updated_paragraph += char
                
        
        counter_dict = collections.Counter(updated_paragraph.lower().split())
        
        for i in range(len(counter_dict)) :
            most_common = counter_dict.most_common(1)[0][0]
            if most_common not in banned :
                return most_common
            else :
                del counter_dict[most_common]