class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # divide into digit log and letter log
        digits, letters = [], []
        for log in logs :
            if log.split()[1].isdigit() :
                digits.append(log)
            else :
                letters.append(log)
                
        # reorder letters
        
        
        # answer
        return letters + digits