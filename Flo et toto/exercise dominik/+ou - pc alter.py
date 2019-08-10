nb=int(input("inserez un nombre"))

machine=50
max=100
min=0

while machine != nb:
    print(machine)
    response=input("+ou-")
    if response=="+":
        min=machine+1
        machine=min+(max-min)//2
    elif response =="-":
        max=machine-1
        machine=min+(max-min)//2
print(machine)
print("jai gangné")