def calRun():
	while True:
		try:
			s_name = input("\nEnter Students Name: ")
			reg_num = input("Enter Registration Number: ")
			math_marks = int(input("Enter Math marks: "))
			eng_marks = int(input("Enter English marks: "))
			science_marks = int(input("Enter science marks: "))
			humanity_marks = int(input("Enter Humanities marks: "))

			average = (math_marks + eng_marks + science_marks + humanity_marks) / 4

			if 90 <= average <= 100:
				grade = 'A'
			elif 80 <= average < 90:
				grade = 'B'
			elif 70 <= average < 80:
				grade = 'C'
			elif 60 <= average < 70:
				grade = 'D'
			elif average <= 60:
				grade = 'E'
			else:
				print("Invalid")
				grade = None

			print(f"\nStudent Name: {s_name}"
				  f"\nRegistration Number: {reg_num}"
				  f"\nAverage score is: {average:.2f}"
				  f"\nFinal Grade: {grade}\n")

		except ValueError:
			print("Error: Please enter valid numerical values for marks")
calRun()