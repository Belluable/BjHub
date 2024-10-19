function convertTime(time){
    const [h, m] = time.split(':');
    return Number(h)*60 + Number(m);
}
function solution(book_time) {
    book_time.sort();
    const room = [];
    
    for(let time of book_time){
        const [start, end] = [convertTime(time[0]), convertTime(time[1])+10];
        const idx = room.findIndex(x => x <= start);
        
        if(idx === -1){
            room.push(end);
        }
        else{
            room[idx] = end;
        }
    }
    
    var answer = room.length;
    return answer;
}