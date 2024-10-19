function solution(k, tangerine) {
    var answer = 0;
    const tDict = {};
    
    tangerine.forEach((t) => (tDict[t] = (tDict[t] || 0) + 1));
    
    const tArr = Object.values(tDict).sort((a,b) => b-a);
    
    for(const t of tArr){
        answer++;
        if(t < k) k -= t;
        else break;
    }
    
    return answer;
}