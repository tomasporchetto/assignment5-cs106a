"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""


INPUT_FILE = 'bill1.txt'


def main():
    credit_card_total_per_store = {}

    with open(INPUT_FILE, 'r') as file:
        for line in file:
            line = line.strip()
            lines = line.split()
            rm_date = lines.pop(0)
            result = ' '.join(lines)
            firs_sqr_br_replaced = result.replace("[", "")
            last_sqr_br_replaced = firs_sqr_br_replaced.replace("]","")
            list = last_sqr_br_replaced.split("$")

            for i in range(len(list)):
                if i == 0:
                    number = list[i+1]
                    #print(number)
                    check_existing_store = credit_card_total_per_store.get(list[i])
                    #print(check_existing_store)
                    if check_existing_store != None:
                        add_store_billing(credit_card_total_per_store, list[i], int(number))
                    else:
                        credit_card_total_per_store[list[i]] = int(list[i + 1])
            
            print(credit_card_total_per_store)

def add_store_billing(dic, name, number):
    #print(name, number)
    #value = int(dic.get(name))
    #value += number
    #print(value)
    dic[name] += number
    #return dic[name]
    


            
            



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
