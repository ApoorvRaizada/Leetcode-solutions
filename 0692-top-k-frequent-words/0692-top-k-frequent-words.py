class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq={}
        n = words
        for n in words:
            freq[n]=freq.get(n,0)+1
        items=sorted(freq.items(),key=lambda x: (-x[1],x[0]))
        arr=[]
        for words,count in items[:k]:
            arr.append(words)
        return arr
        