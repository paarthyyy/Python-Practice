target_savings = int(input("Enter target savings: "))
current_savings = 0
deposit_count = 0

while current_savings < target_savings:
    deposit = int(input("Enter deposit amount: "))
    current_savings = current_savings + deposit
    deposit_count = deposit_count + 1

print("Target reached!")
print(deposit_count)
print(current_savings)


START 
INPUT target_savings
SET current_savings = 0
SET deposit_count =0

WHILE current_savings < target_savings
       STE deposit = input intergr "Enter deposit amount: "
       SET current_savings = current_savings + deposit
       SET deposit_count = deposit_count + 1
ENDWHILE
output Target reached!
output deposit_count
output current_savings

END