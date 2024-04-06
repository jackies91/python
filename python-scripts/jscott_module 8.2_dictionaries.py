#Jackie Scott
#11/26/23
#Module 8.2 Dictionaries 

#This program will search the dictionary for a ticker symbol and then print the ticker symbol and the stock price. If the ticker symbol is not located, print a message indicating that the ticker symbol was not found.

# Create a variable to control the loop.
another_stock = 'Y' 

while another_stock.upper() == 'Y':

#Create Stock dictionary
    stocks = {
    'TSLA': 900.58,
    'AAPL': 2875.50,
    'GOOGL': 2500.54,
    'FB': 650.00,
    'SOFI': 6.92,
    'KIRK': 8.72,
    'AMZN': 145.58,
    'QQQ': 389.51,
    'GME': 12.20,
    'KBR': 52.27
}
    
#Ask the user to enter a ticker symbol
    user_input = input('Enter a stock ticker symbol: ')

#converting user input to upper case otherwise we will not get a match since our dictionary is all uppercase
    ticker = user_input.upper()

#Search the dictionary for the entered ticker symbol
    if ticker in stocks:
        print(f'Stock Ticker: {ticker}\nStock Price: ${stocks[ticker]:.2f}')
        another_stock = input('Do you want to search another stock ticker? (Enter y for yes): ')
    else:
        print(f"Stock Ticker '{ticker}' not found.")
        another_stock = input('Do you want to search another stock ticker? (Enter y for yes): ')