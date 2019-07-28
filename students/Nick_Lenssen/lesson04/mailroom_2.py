from sys import exit

from operator import itemgetter

def get_donation_amount():
    while True:
        amount = input("\nPlease enter in the amount you want to donate or c to go to original prompt: ")
        if amount == 'c':
            main()
            #donor_db.pop()
        else:
            amount = int(amount)
        return amount

def create_report():
    print("\n{:<18}{:<6}{:<20}{}{:<25}{}{:<15}".format(*('Donor Name','|','Total Given','|','Num Gifts','|','Average Gift')))
    print ('-'*90)
    #donor_db_c = sorted(donor_db, key=itemgetter(1))
    for key, value in sorted(donor_db.items(), key=itemgetter(1), reverse = True):
        print ("{:<20} {:>2} {:>12} {:>17}{:>17}{:>12}".format(*(key, '$', round(sum(donor_db[key]),2), 
                        len(donor_db[key]), '$',round(sum(donor_db[key])/len(donor_db[key]),1))))

def send_thanks():
    while True:
        full_name = input("\n\nPlease enter a name for a Thank You to go out or c to go to orginal prompt: ")
        if full_name == 'list':
            for key in donor_db:
                print (key)
        elif full_name == 'c':
            main()
        else:
            for key in donor_db:
                if key == full_name:
                    donor_db[key].append(get_donation_amount())
                    break
            else:
                donor_db[full_name] = [get_donation_amount()]
                #donor_db.append((full_name, [get_donation_amount()]))
            print ("Thank you {} for your donation amount of {}$. We thank you for your support".format(full_name, donor_db[full_name][-1]))
            #couldn't figure out how to do **dict formating with a key in string form and value

            #main()

def exit_program():
    print ('Goodbye')
    exit()

def main():
    while True:
        num = input(prompt)
        if num =='a':
            send_thanks()
        elif num == 'b':
            create_report()
        elif num == 'c':
            exit_program()
        else:
            print ('Not a valid option')

donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0]
            }

prompt = "\n".join(("Please choose from below options:",
          "a - Send a Thank you",
          "b - Create a report",
          "c - Exit",
          ">>> "))

if __name__ == "__main__":
    main()