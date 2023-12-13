# Function with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
    print("This is dead code") # DEAD CODE

output = format_name("angelo", "")

print(output)