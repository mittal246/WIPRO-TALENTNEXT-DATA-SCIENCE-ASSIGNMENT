''' 
Task Description
You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.

 You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after the discount?
'''
def process_purchase_file():
    try:
        filename = input("Enter the purchase file name: ")
        with open(filename, 'r') as file:
            items = file.readlines()

        total_items = len(items)
        total_amount = 0
        free_items = 0

        for item in items:
            parts = item.strip().split()
            if len(parts) != 2:
                print(f"Skipping invalid line: {item}")
                continue
            name, price_str = parts
            try:
                price = float(price_str)
                if price == 0:
                    free_items += 1
                else:
                    total_amount += price
            except ValueError:
                print(f"Invalid price format for item: {name}")
                continue

        discount = 0.10 * total_amount  
        final_amount = total_amount - discount

        print("\nSummary:")
        print(f"Total items purchased: {total_items}")
        print(f"Free items: {free_items}")
        print(f"Total amount before discount: ₹{total_amount:.2f}")
        print(f"Discount amount (10%): ₹{discount:.2f}")
        print(f"Final amount to pay: ₹{final_amount:.2f}")

    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

process_purchase_file()
