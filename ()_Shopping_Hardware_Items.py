
#===========================================
#=================[ITEM]====================
#================[CLASSES]==================
#===========================================


class Item:
    def __init__(self, Name, Cost, ToBuy, Total):
        self.Name = Name              # name of hardware item
        self.Cost = Cost              # cost of hardware item
        self.ToBuy = ToBuy            # amount that the user wants to buy
        self.Total = Total            # Cost x ToBuy


Hammer      = Item("Hammer",      9.99, 0,0)
Spanner     = Item("Spanner",     7.50, 0,0)
Wrench      = Item("Wrench",      8.00, 0,0)
Screwdriver = Item("Screwdriver", 8.20, 0,0)
Chainsaw    = Item("Chainsaw",   84.00, 0,0)
Lawnmower   = Item("Lawnmower",  60.00, 0,0)
Soil        = Item("Soil",       50.00, 0,0)
Shovel      = Item("Shovel",     15.00, 0,0)
Axe         = Item("Axe",        25.00, 0,0)
Hose        = Item("Hose",       12.00, 0,0)


#===========================================
#===============[GLOBAL]====================
#==============[VARIABLES]==================
#===========================================


all_items = [Hammer,Spanner,Wrench,Screwdriver,Chainsaw,Lawnmower,Soil,Shovel,Axe,Hose]
money_starting = 500
fullname_of_user = "Ben Arthur"


#===========================================
#=================[DISPLAY]=================
#================[FUNCTIONS]================
#===========================================


def fDisplay_Welcome():
    print()
    print("===========================================")
    print("==========WELCOME TO BENS BIG ASS==========")
    print("==============HARDWARE STORE===============")
    print("===========================================")    
    print()


def fDisplay_Status():
    subtotal = 0

#---display header
    print()
    for a in range(1):
        print("{2:15} {3:7} {1:2} {4:4} {5:6}".format("", "|", "Name".rjust(13),"Cost".center(7),"Buy".rjust(1),"Total".rjust(2)))
        print("-" * 39)

#---display content
    for a in range(10):                               #ref:   0   1    2                              3                     4                                   5                       
        print("{2:15} ${3:6.2f} {1:2} {4:4} ${5:6.2f}".format("", "|", (all_items[a].Name).rjust(13), (all_items[a].Cost), str(all_items[a].ToBuy).rjust(1), (all_items[a].Total)))

#---display total
    for a in range(10):
        subtotal += all_items[a].Total
    for a in range(1):
        print("-" * 39)
        print("{2:23} {1:7} ${3:6.2f}".format("", "|", "Total".rjust(23),subtotal))
        print()


#==========================================
#=================[PART 1]=================
#================[SHOPPING]================
#==========================================


def fShopping_Time(money_starting):

    # this code needs to be changed
    money_remaining = money_starting

    bln_exit_loop = False
    while bln_exit_loop == False:

#[EXIT ON ZERO MONEY]
        # exit function if money reached 0
        # we can just change the while loop to while money > 0
        if money_remaining <= 0:
            money_spent = money_starting - money_remaining
            #THIS CODE NEEDS WORK
            return money_spent

#[DISPLAY MENU]
        # display the purchase menu, and how much money the user has left
        fDisplay_Status()
        print("You currently have ${0:0.2f} of Big Bens Buckaroos".format(money_remaining))

#[PREPARE INPUTS]
        #  create user input restriction list from item names
        allowed_inputs = get_item_name_list()

        # add "0" and "<" as allowed inputs. These will be to exit the shopping.
        allowed_inputs.append("0")
        allowed_inputs.append("<")

        # store user input as variable
        user_input = fValidate_User_Input(allowed_inputs, "Purchase an Item")

#[EXIT ON USER COMMAND]
        # exit function if user typed in a "0" or a "<"
        if user_input == "0" or user_input == "<":
            money_spent = money_starting - money_remaining
            return money_spent

#[PURCHASED ITEM]
        # search the item in the dictionary to return the class item
        class_item = get_item_stats(user_input.title())

        # check if user can afford item. If not, reset loop.
        if not check_if_afford(money_remaining, class_item.Cost):

            print("you cant afford this")
            input("Press any key to continue")
            continue

        # check if the user can afford item
        if check_if_afford(money_remaining, class_item.Cost):

            # take the cost of item, remove it from money remaining
            money_remaining -= class_item.Cost
            increase_item_to_buy(class_item)

            # inform the user what they had purchased and add it to the list
            print("you purchased {0} for ${1:0.2f}".format(user_input.title(), class_item.Cost))

            # wait for user input, and reset loop once done
            input("Press any key to continue")
            

#==========================================
#=================[PART 2]=================
#================[PAYMENTS]================
#==========================================

def fPayment_Time(total_bill):
    global payment_method
    #Need to return the payment method, the total amount, the amount paid, the amount received
    
#[USER INPUT]
    allowed_inputs = ["Cash","Credit"]
    user_input = fValidate_User_Input(allowed_inputs,"Pay by cash or credit?")

#[PAID CREDIT]
    if user_input.title() == "Credit":
        payment_method = "Credit"   #Change gloabl variable - required for receipt output

        if total_bill < 20:
            print("the minimum credit card purchase is $20.00 and this transaction will be processed as a cash sale")
            print("user_input has been changed from 'Credit' to 'Cash'")
            user_input = "Cash"
        if total_bill >= 20:
            return payment_method, total_bill, 0, 0

#[PAID CASH]           
    if user_input.title() == "Cash":
        payment_method = "Cash"   #Change gloabl variable - required for receipt output

        # loop user input until the amount paid is greater than the amount owed
        bln_loop_block = True
        while bln_loop_block == True:
            try:
                money_paid = float(input("Input cash tendered: "))
                if money_paid >= total_bill:
                    change_given = int(money_paid) - total_bill
                    bln_loop_block = False
                    print('${0:0.2f} of change was given to the customer'.format(change_given))
                    return payment_method, total_bill, money_paid, change_given
                    
                else:
                    raise ValueError()
            except ValueError:
                print("Error: Not enough money was paid. Or there was an input error")


#==========================================
#=================[PART 3]=================
#================[RECIEPTS]================
#==========================================

def fIssue_Receipt(payment_method, total_bill, money_paid, change_given):

#[PART 1 - STORE DOCUMENT LINES]
#==============================

#---store receipt title
    text_document_title = []
    text_document_title.append("===========================================")
    text_document_title.append("===============BENS BIG ASS================")
    text_document_title.append("==============HARDWARE STORE===============")
    text_document_title.append("===========================================")
    text_document_title.append("")
    text_document_title.append("Receipt:")

#---store table header
    for a in range(1):
        text_table_header1 = ("{2:15} {3:7} {1:2} {4:4} {5:6}".format("", "|", "Name".rjust(13),"Cost".center(7),"Num".rjust(1),"Total".rjust(2)))
        text_table_header2 = ("-" * 39)

#---store table body
    text_table_body = []
    for a in range(10):
        if all_items[a].ToBuy > 0:
            b = ("{2:15} ${3:6.2f} {1:2} {4:4} ${5:6.2f}".format("", "|", (all_items[a].Name).rjust(13), (all_items[a].Cost), str(all_items[a].ToBuy).rjust(1), (all_items[a].Total)))
            text_table_body.append(b)
            
#---store table subtotal
    for a in range(1):
        text_table_total1 = ("-" * 39)
        text_table_total2 = ("{2:23} {1:7} ${3:6.2f}".format("", "|", "Total".rjust(23),total_bill))
        print()

#---store receipt footer
    text_document_footer = []

    if payment_method == "Credit":
        text_document_footer.append("Bens Big Ass Hardware Store - Credit Transation")
        text_document_footer.append("")
        text_document_footer.append("Thank you for your payment..." + fullname_of_user)
        text_document_footer.append("Total:  ${0:0.2f}".format(total_bill))
        text_document_footer.append("CREDIT CARD PAYMENT ACCEPTED")

    if payment_method == "Cash":
        text_document_footer.append("Thank you for your payment..." + fullname_of_user)
        text_document_footer.append("")
        text_document_footer.append("Total:  ${0:0.2f}".format(total_bill))
        text_document_footer.append("Amount Tendered:  ${0:0.2f}".format(money_paid))
        text_document_footer.append("Change:  ${0:0.2f}".format(change_given))


#[PART 2 - WRITE LINES TO NOTEPAD]
#==============================

    with open("output.txt","w") as output_file:

        #document header
        output_file.writelines("\n".join(text_document_title))
        output_file.write("\n")

        # table header
        output_file.write(text_table_header1 + "\n")
        output_file.write(text_table_header2 + "\n")

        # table body
        output_file.writelines("\n".join(text_table_body))
        output_file.write("\n")
        
        # table total
        output_file.write(text_table_total1 + "\n")
        output_file.write(text_table_total2 + "\n")
        output_file.write("\n")
        output_file.write("\n")

        # payment method and summary
        output_file.writelines("\n".join(text_document_footer))


#[PART 3 - OFFER TO WRITE RECEIPT TO TERMINAL]
#==============================
    user_input = fValidate_User_Input(["Yes","No"],"Print receipt to terminal? ")
    if user_input == "Yes":

        # establish file object
        output_file = open("output.txt","r")

        # print notepad file
        for line in output_file:
            print(line)


#==========================================
#=================[OTHER]==================
#===============[FUNCTOINS]================
#==========================================


def fValidate_User_Input(user_can_only_type, input_message):
# process the user input and ensures it matches to a predefined list
    while True:
        try:
            user_input = input(input_message + ": ")
            if str(user_input).title() in user_can_only_type:
                return user_input
            raise ValueError()
        except ValueError:
            print("Error: You are required to enter one of the following: {}".format(user_can_only_type))


def get_item_name_list():
# returns a list of the ".Name" of every entry in the "Item" class
    list = []
    for a in range(10):
        list.append(all_items[a].Name)
    return list


def get_item_stats(item_name):
# dictionary to return a single entry in the "Item" class
    hardware_items =  {
        Hammer.Name      :   Hammer,
        Spanner.Name     :   Spanner,
        Wrench .Name     :   Wrench,
        Screwdriver.Name :   Screwdriver,
        Chainsaw.Name    :   Chainsaw,
        Lawnmower.Name   :   Lawnmower,
        Soil.Name        :   Soil,
        Shovel.Name      :   Shovel,
        Axe.Name         :   Axe,
        Hose.Name        :   Hose
    }
    Dictionary_Result = hardware_items[item_name]
    return Dictionary_Result


def increase_item_to_buy(item):
# indicates that a user purchased an item
    item.ToBuy += 1
    item.Total = item.Cost * item.ToBuy 


def check_if_afford(money_remaining, item_cost):
# boolean to check if user can afford item they inputted
    if money_remaining > item_cost:
        return True
    else:
        return False


#==========================================
#==============[ACTIVATE]==================
#================[CODE]====================
#==========================================

# display the welcome sign
fDisplay_Welcome()

# begin the loop for the user to buy items. return the total amount owing for the Payment Function
total_bill = fShopping_Time(money_starting)

# user to determine payment for cash or credit. Store payment type, and cash details (if applicable) for receipt
payment_method, total_bill, money_paid, change_given = fPayment_Time(total_bill)

# construct a notepad document 'receipt' and write it to "output.txt"
fIssue_Receipt(payment_method, total_bill, money_paid, change_given)
print("----------------------------")
print("Job Done. Output.txt created")

