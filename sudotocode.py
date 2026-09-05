#START
 #   INPUT n
  #  SET total = 0
   # SET passed = 0
    #FOR i FROM 1 TO n
     #   INPUT mark
      #  SET total = total + mark
       # IF mark >= 40 THEN
        #    SET passed = passed + 1
        #ENDIF
    #ENDFOR
    #OUTPUT total
    #OUTPUT passed
#END

n=float(input("Enter the number of students: "))
total = 0
passed = 0
for i in range(int(n)):
    mark = float(input(f"Enter the mark for student {i + 1}: "))
    total += mark
    if mark >= 40:
        passed += 1
        break
print(f"Total marks: {total}")
print(f"Number of students who passed: {passed}")