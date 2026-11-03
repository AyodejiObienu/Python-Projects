# a program that reads a sales csv and produces a summary containing:
# total revenue✅, number of valid transactions✅, average transaction value✅, best selling product✅, highest revenue day✅.
# project specifications:
# calculate total revenue
# count the number of valid transactions
# calculate average transaction value
# find the best selling product by quantity
# find a day with the highest revenue
# handle invalid and missing values appropriately.
# no ai must be used to write this code, do it all yourself.
import csv
from collections import Counter
total_revenue = 0
valid_transactions = 0
average_transaction_value = 0
best_selling_product = ''
highest_revenue = 0
best_selling_day = ''
product_quantity = {}
daily_revenue = {}
# product_counts = Counter(product_list)
with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        try:
            day = row['date'].strip()
            product = row['product'].strip()
            quantity = int(row['quantity'])
            price = float(row['unit_price'])

            if not product or quantity <= 0 or price < 0:
                continue
            revenue = quantity * price
            daily_revenue[day] = daily_revenue.get(day, 0) + revenue
            product_quantity[product] = product_quantity.get(
                product, 0) + quantity
            total_revenue += revenue
            valid_transactions += 1
            average_transaction_value = total_revenue / valid_transactions

        except ValueError:
            continue

        if revenue > highest_revenue:
            highest_revenue = revenue
            best_selling_day = day
        best_selling_day = max(daily_revenue, key=daily_revenue.get)
        highest_revenue = daily_revenue[best_selling_day]

        best_selling_product = max(product_quantity, key=product_quantity.get)

    # for product in product_list:
    #     if product_list.count(product) > product_list.count(best_selling_product):
    #       best_selling_product = product
        # highest_revenue = product_list.count(product) * price


print(f'Total Revenue: ${total_revenue:.2f}')
print(f'Number of Valid Transactions: {valid_transactions}')
print(f'Average Transaction Value: ${average_transaction_value:.2f}')
print(
    f'Best Selling Product: {best_selling_product}, Highest Revenue: ${highest_revenue:.2f}')
print(f'Highest Revenue Day: {best_selling_day}')
print(f'Highest Revenue Day: ${highest_revenue:.2f}')
# print(f'Product List: {product_list}')
print(daily_revenue)
