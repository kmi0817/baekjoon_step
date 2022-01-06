# accepted (runtime: 52ms, memory: 14.3MB)
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1) remove character that is not alphanumeric 2) make it lower 3) make list
        paragraph_list = re.sub(f'[^\w]', ' ', paragraph).lower().split()
        
        # filter the banned words
        words_except_banned = [word for word in paragraph_list if word not in banned]
        
        # count each word
        counter_dict = collections.Counter(words_except_banned)
        
        return counter_dict.most_common(1)[0][0]

# wrong answer (before using collection.Counter(), the problem occured)
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