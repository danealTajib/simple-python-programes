bangla =input("Bangla Subject Marks :")
English =input("English Subject Marks :")
Math=input("Math Subject Marks :")

bangla = int(bangla)
English = int(English)
Math = int(Math)

Grade= ""
Avg_Grade= ""
Avg_Marks= ""

if bangla>=80 and bangla <=100:
        Grade="A"
elif bangla>=70 and bangla <79:
       Grade="B"
elif bangla>=60 and bangla <69:
       Grade="C"
elif bangla>=50 and bangla <59:
       Grade="D"
elif bangla>=40 and bangla <49:
       Grade="E"
elif bangla>=0 and bangla <39:
       Grade="F"
print("Bangla Subject Marks :",Grade)

if English>=80 and English <=100:
        Grade="A"
elif English>=70 and English <79:
       Grade="B"
elif English>=60 and English <69:
       Grade="C"
elif English>=50 and English <59:
       Grade="D"
elif English>=40 and English <49:
       Grade="E"
elif English>=0 and English <39:
       Grade="F"
print("English Subject Marks :",Grade)

if Math>=80 and Math <=100:
        Grade="A"
elif Math>=70 and Math <79:
       Grade="B"
elif Math>=60 and Math <69:
       Grade="C"
elif Math>=50 and Math <59:
       Grade="D"
elif Math>=40 and Math <49:
       Grade="E"
elif Math>=0 and Math <39:
       Grade="F"
print("Math Subject Marks :",Grade)

Avg_Marks=(bangla+English+Math)/3
print("Avg_Marks:",Avg_Marks)

if Avg_Marks>=80 and Avg_Marks <=100:
        Grade="A"
elif Avg_Marks>=70 and Avg_Marks <79:
       Grade="B"
elif Avg_Marks>=60 and Avg_Marks <69:
       Grade="C"
elif Avg_Marks>=50 and Avg_Marks <59:
       Grade="D"
elif Avg_Marks>=40 and Avg_Marks <49:
       Grade="E"
elif Avg_Marks>=0 and Avg_Marks <39:
       Grade="F"
print("Avg_Grade:",Grade)
