"""
@GAURAV SHUKLA
Code Notes:
d/mm/yy
1 < d < mm < yy
d is factor mm and mm is a factor of y
"divisor dates"
4/08/24
2/12/24
2024-2099
Answer format:
dmmyyDMMYY where dmmyy is the first non-divisor date in the gap and DMMYY is the last
or
divsor date +1  + successive divisor date -1 """
from datetime import date
dates = []
valid_divisor_date = lambda d, mm, yy: True if (1 < d < mm  < yy and mm%d == 0 and yy%mm == 0) else False
populate = lambda:[[[(dates.append([day,month,year]) if (valid_divisor_date(day,month,year)) else None) for day in range(1,10)] for month in range (1,13)] for year in range(24,100)]
difference = lambda d, d2: abs((date(d2[2]+2000,d2[1],d2[0])-date(d[2]+2000,d[1],d[0])).days)
populate()
diff = [difference(dates[idx],dates[idx+1]) for idx in range(len(dates)-1)]
d1,d2 = dates[diff.index(max(diff))] ,dates[diff.index(max(diff))+1]
print(f"Max difference is {max(diff)} days between {d1} and {d2}")
print(f"Final Answer is {d1[0]+1}0{d1[1]}{d1[2]}{d2[0]-1}0{d2[1]}{d2[2]}")