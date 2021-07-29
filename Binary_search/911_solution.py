#bs+hash
#bs+hash

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.time_winning = collections.defaultdict()
        vote_count = collections.defaultdict(int)
        #print(vote_count)
        cur_max, cur_win = 0, -1
        
        for p, t in zip(persons, times):
            vote_count[p] += 1
            if vote_count[p] >= cur_max: 
                cur_max, cur_win = vote_count[p], p
                #print(cur_max,cur_win)
            self.time_winning[t] = cur_win
        self.times = times 
        #print(self.time_winning)
        #print(self.times)

    def q(self, t: int) -> int:
        if t in self.time_winning:
            return self.time_winning[t]
        #print(self.time_winning)
        #print(t)
        i = bisect.bisect(self.times, t)
        #print("i",i)
        return self.time_winning[self.times[i-1]]
