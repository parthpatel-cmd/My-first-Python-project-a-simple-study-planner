print("╔════════════════════════════════╗")
print("║       📚 STUDY PLANNER         ║")
print("╚════════════════════════════════╝")




name = input("what is your name? ")
hours = float(input("how many hours can you study? " ))

subject1 = input("enter your first subject: ")
subject2 = input("enter your second subject: ")
subject3 = input("enter your third subject: ")

priority1 = int(input(f"how important is {subject1}? "))
priority2 = int(input(f"how important is {subject2}? ")) 
priority3 = int(input(f"how important is {subject3}? ")) 

total_priority = priority1 + priority2 + priority3 

sub1_time = (priority1 / total_priority) * hours
sub2_time = (priority2 / total_priority) * hours
sub3_time = (priority3 / total_priority) * hours


print("─────────────────────────────────")

print(f"{subject1} study time:{sub1_time} hours ")
print(f"{subject2} study time:{sub2_time} hours ")
print(f"{subject3} study time:{sub3_time} hours ")

print("─────────────────────────────────")


print(f"Total study hour: {total_priority}")

print("good luck")