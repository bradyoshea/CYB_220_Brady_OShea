
# This is a program to store new vehicle inventory and assist with monthly payments
# Create variable of your favorite car brand (e.g., brand = ‘RAM’)
carbrand = 'Chevrolet'

# Create list of 5 of their models from cheapest to most expensive
models = ['Equinox', 'Camaro', 'Silverado', 'Tahoe', 'Corvette']

# Append a 6th model to the list
models.append('Suburban')

# Create list of 5 standard colors for all models
colors = ['white', 'red', 'blue', 'black', 'gray']

# Replace your last color with a different color
colors[4] = 'silver'

# Create variable of the current year (e.g., YEAR = ‘2026’)
YEAR = 2026

# Create MSRP constant number (not string) of each of the models (e.g., MSRP_1500Truck = 33000)
MSRP_EQUINOX = 28_800
MSRP_CAMARO = 32_495
MSRP_SILVERADO = 36_900
MSRP_TAHOE = 59_500
MSRP_CORVETTE = 70_000
MSRP_SUBURBAN = 62_000

# Create a constant number (not string) for total months in 4yr, 5yr, and 6yr loans (e.g., fouryr = 48,sixyr = 72)
FOURYR = 48
FIVEYR = 60
SIXYR = 72

# Create a variable for the guest's name. Be courteous in your upcoming messages :)
guestname = "Bill"

# Create message variable (with f-string) welcoming customer to your new car store
greeting = f'Hello {guestname}, welcome to the dealership!'
print(greeting)

# Create awesome banner with your brand/name/dealership, however you want to welcome customers
banner =  r"""
_________ .__                               .__          __
\_   ___ \|  |__   _______  _________  ____ |  |   _____/  |_
/    \  \/|  |  \_/ __ \  \/ /\_  __ \/  _ \|  | _/ __ \   __
\     \___|   Y  \  ___/\   /  |  | \(  <_> )  |_\  ___/|  |
 \______  /___|  /\___  >\_/   |__|   \____/|____/\___  >__|
        \/     \/     \/                              \/    
"""

# Print awesome banner and welcome message
print(banner)

# Using title methods, print the vehicles in alphabetical order, with the year and available colors.
models.sort()
print(f'{YEAR} {models[0].title()}')
print(f'{YEAR} {models[1].title()}')
print(f'{YEAR} {models[2].title()}')
print(f'{YEAR} {models[3].title()}')
print(f'{YEAR} {models[4].title()}')
print(f'{YEAR} {models[5].title()}')
print(f'These models all come in {colors[0].title()}, {colors[1].title()}, {colors[2].title()}, {colors[3].title()}, and'
    f' {colors[4].title()}\n')

# Create a variable that calculates a monthly payment (no interest) for 5yr/60months for the first vehicle. Do not let more than two decimals to occur.
monthlypayment = round(100*MSRP_CAMARO/FIVEYR)/100

# and print that in a nice, kind message. Don't be rude/pushy to the customer :)
print(f'Monthly payment for the Camaro for 5 years is ${monthlypayment}')

# Do the same thing, but give them 4yr and 6yr options for the same vehicle
fouryrmonthlypayment = round(100*MSRP_CAMARO/FOURYR)/100
sixyrmonthlypayment = round(100*MSRP_CAMARO/SIXYR)/100

print(f'Monthly payment for the Camaro for 4 years is ${fouryrmonthlypayment}')
print(f'Monthly payment for the Camaro for 6 years is ${sixyrmonthlypayment}\n')

# Lastly, give them a 5yr option for each of the other vehicles, just to see if they are interested
monthlypaymentequinox = round(100*MSRP_EQUINOX/FIVEYR)/100
monthlypaymentsilverado = round(100*MSRP_SILVERADO/FIVEYR)/100
monthlypaymenttahoe = round(100*MSRP_TAHOE/FIVEYR)/100
monthlypaymentcorvette = round(100*MSRP_CORVETTE/FIVEYR)/100
monthlypaymentsuburban = round(100*MSRP_SUBURBAN/FIVEYR)/100

print(f'Monthly payment for the Equinox for 5 years is ${monthlypaymentequinox}')
print(f'Monthly payment for the Silverado for 5 years is ${monthlypaymentsilverado}')
print(f'Monthly payment for the Tahoe for 5 years is ${monthlypaymenttahoe}')
print(f'Monthly payment for the Corvette for 5 years is ${monthlypaymentcorvette}')
print(f'Monthly payment for the Suburban for 5 years is ${monthlypaymentsuburban}')

cashprice = MSRP_CAMARO*0.9
print(f'\nIf you pay for the Camaro in cash it is 10% off, making it ${cashprice}')

downpaymentprices = [MSRP_CAMARO*.98, MSRP_CAMARO*.95, MSRP_CAMARO*.92]
print(f'\nThere is also a discount for downpayments, a small downpayment (10%) makes the new price ${downpaymentprices[0]}\n' 
      f'A medium downpayment (20%) makes the new price ${downpaymentprices[1]}\nA large downpayment (30%) makes the new price' 
      f' ${downpaymentprices[2]}')

graycamaroprice = MSRP_CAMARO*1.1
print(f'\nThere is also an option for a gray Camaro, but because that color was discontinued it costs ${graycamaroprice} (10% extra)')