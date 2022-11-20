counter=0
secret_word= " Ananyalp"
while counter<7:
    word=input("Enter the secreat word")

    counter=counter+1

    if word==secret_word:
        print("you guessed it right")
        break
else:
    print("Better luck next time")
