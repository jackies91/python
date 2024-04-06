#used as a global constant to represent the contribution rate to retirement
contribution_rate = 0.05

def main():
    gross_pay = float(input('Enter the gross pay: '))
    bonus = float(input('Enter the amount of bonuses: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)


#Show_pay_contrib function accepts gross pay as argument and displays retirment contribution for amount of pay
def show_pay_contrib(gross):
    contrib = gross * contribution_rate
    print(f'Contribution for gross pay: ${contrib:,.2f}.')

#show_bonus_contrib function accepts bonus amount as arugment and displays the retirement contrib for that amount
def show_bonus_contrib(bonus):
    contrib = bonus * contribution_rate
    print(f'Contribution for bonuses: ${contrib:,.2f}.')

#call main fun
main()