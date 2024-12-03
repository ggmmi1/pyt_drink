vending_machine = ['게토레이', '레쓰비', '생수', '이프로']
beverage = input("마시고 싶은 음료?")
if beverage in vending_machine:
    print(f"{beverage}드릴게요")
else:
    print(f"{beverage}는 지금 없네요")
    
    
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
user = input("사용자 유형을 입력하세요.(소비자 또는 주인):")


if user == '소비자':
    choice = input("원하는 음료를 말해주세요,:")
    if choice in vending_machine:
        vending_machine.remove(choice)
        print(f"{choice} 드릴게요.")
    else:
        print(f"{choice}는 지금 없네요.")
elif user == '주인':
    select = input("원하는 작업을 선택하세요.(추가 또는 삭제):")
    print(select)
    
    if select == '추가':
        new_choice = input("추가할 음료를 선택하세요.:")
        vending_machine.append(new_choice)
        vending_machine.sort()
        print(f"{new_choice}를 추가했습니다. 현재 음료 리스트: {vending_machine}")
    elif select == '삭제':
        delete_drink = input("삭제할 음료를 입력하세요")
        if delete_drink in vending_machine:
            vending_machine.remove(delete_drink)
            print(f"{delete_drink}를 삭제했습니다. 현재 음료 리스트: {vending_machine}")
        else:
            print(f"{delete_drink}는 자판기에 없어서 삭제할 수 없습니다.")
    else:
        print(f"{select}는 없는 작업입니다. 다시 적어주세요.")
else:
    print(f"{user}는 잘못된 유형입니다. 다시 적어주세요.")
    
    
        