def loading_bar(stage:int) -> str:
    percentage = stage // 10
    dots = 10 - percentage
    if stage == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{stage}% [{'%' * percentage}{'.' * dots}]\nStill loading..."

number = int(input())
result = loading_bar(number)
print(result)