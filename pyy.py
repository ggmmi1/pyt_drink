

    

age=int(input('나이'))
pay=intput('결제수단')
if age<8 or age> 74:
    print(f'{age}세의 {pay} 요금은 무료입니다.')
elif age<14:
    print(f'{age}세의 {pay} 요금은 450원입니다.')
elif age<20:
    if pay == '카드':
     print(f'{age}세의 {pay} 요금은 720원입니다.')
    else:
     print(f'{age}세의 {pay} 요금은 1000원입니다.')
elif age<75:
    if pay == "카드":
     print(f"{age}세의 {pay} 요금은 1200원입니다.")
    else:
     print(f"{age}세의 {pay} 요금은 1300원입니다.")
   