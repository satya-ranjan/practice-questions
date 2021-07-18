items_input =int(input("Enter the hoe many input you want to input :"))
items_are = input("Enter the items separeted by space : ").split()
sum = 0
percentage = 1
for i in range(len(items_are)):
    items_are[i] = int(items_are[i])
    if items_are[i] > 1000:
        sum = sum + items_are[i]
    percentage = 0.1*sum
print(percentage)
