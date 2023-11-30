# Even or odd ?
number = int(input("Which number do you want to check? "))

remainder = number % 2 # modulo operator

if remainder == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
