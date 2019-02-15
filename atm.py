'''
This program is written by sourabh agrawal
problem:
	user have some amount and user will give the type of notes in which he wants to get his currency gets converted. we have to give user minimum no of notes
	so, convert the amount given by the user effeciently so that all amount gets covered by lesser no of notes...
'''

#!/usr/bin/python3
def main():
    no = int(input("Enter how many type of notes you have with you?\t"))		#suppose no = 7
    print("Enter the value of those notes")									
    i = no				#i = no = 7
    notes = []			#initializing an empty list
    while i > 0:
        notes.append(int(input()))		#storing the input in list after getting it from the user and converting it into int
        i -= 1							#decrementing the value of i

    notes.sort(reverse=True)			#sorting the list in reverse order so that we can get bigger notes at the starting of the list
    amount = int(input("Enter the amount now\t"))			#taking the value of amount that the user has with him
    i = len(notes) - 1									#counting the length of the list(no of different types of notes)
    print("The distribution of notes will be")
    ans = {}
	#suppose amount is 1950 and notes are [500,400,300,200,100,30,20]
    for note in notes:
        n = amount // note			#in first iteration n = 1950//500=3		which tells us that 3 complete notes of 500 will get covered
        amount = amount - n * note		#now we can give 3 notes of 500 to the user so left amount is "total amount - 3*500"
        ans.update({note : n})			#updating the dictonary with "500:3"
        # print("notes of " + str(note) + " = " + str(n))
        if not amount:				#if amount is 0 then the if condition will get True and loop will get break
            break					
    print(ans)							#printing notes and their quantity
    print("Remaining amount {0}".format(amount))		#showing the remaining amount which can not be converted into notes 


if __name__ == '__main__':
    main()






