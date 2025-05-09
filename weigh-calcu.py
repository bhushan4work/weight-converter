# weight calculator

weight = int(input( "enter ur weight: "))
unit = input(" kilograms or pounds (K or L) ?")

if unit == "K":
   weight = weight * 2.205
   unit = "Lbs."
   print(f"ur weight is: {round(weight,1)} {unit}")

elif unit == "L":
     weight = weight / 2.205
     unit = "Kgs."
     print(f"ur weight is: {round(weight,1)} {unit}")

else: 
    print( f"{weight} is invalid input")     