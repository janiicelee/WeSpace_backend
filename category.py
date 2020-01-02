arr = ['공연장',
       '다목적홀',
       '독립오피스',
       '레저시설',
       '루프탑',
       '브라이덜샤워',
       '세미나실',
       '스터디룸',
       '스튜디오',
       '엠티장소',
       '연습실',
       '일하기좋은카페',
       '작업실',
       '카페',
       '코워킹스페이스',
       '파티룸',
       '한옥',
       '회의실']
with open('./test.txt', 'w', newline="") as sql:
    for i in arr:
        data = "insert into space_categories value(null,'" + \
            i + "',now(),now());"
        sql.write(data)
