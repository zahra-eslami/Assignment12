import os
from media import *
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip

PRODUCTS = []
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, "dataset.txt")

''' ------------------------------------------------------------------------------------------------ '''     

def choice(ch):
    if ch == 1:
        Add()
    elif ch == 2:
        Edit()
    elif ch == 3:
        Remove()
    elif ch == 4:
        name=input("Please enter the name you are looking for: ")
        Show_Info(name)
    elif ch == 5:
        min_duration=input("please enter the minimum duration you want: ")
        max_duration=input("please enter the maximum duration you want: ")
        advanced_search(min_duration, max_duration)
    elif ch == 6:
        name=input("Please enter the name you are looking for: ")
        download(name)
    elif ch == 7:
        write_to_database()
        exit(0)
    else:
        print("Your choice is not in the list, please choose again")
        Show_menu()

''' ------------------------------------------------------------------------------------------------ '''     

def Show_menu():
        print("1- Add")
        print("2- Edit")
        print("3- Remove")
        print("4- Show Info")
        print("5- Search by time")
        print("6- Download Trailer")
        print("7- Exit")

''' ------------------------------------------------------------------------------------------------ '''        

"""
strip() method in Python removes leading and trailing whitespace (spaces, tabs, newline characters, etc.)
from a string. It returns a copy of the string with these characters removed.
"""

def read_from_database():

    type_to_class = {
        "film": {"class": Film, "variable": "genre"},
        "series": {"class": Series, "variable": "num_episodes"},
        "documentary": {"class": Documentary, "variable": "topic"},
        "clip": {"class": Clip, "variable": "category"}
    }
   
    with open(file_path, 'r') as f:
        for line in f:
            result = line.strip().split(",")
            
            # Check if the line is not empty or contains only whitespace
            if result and result[0].strip():
                obj_type = result[0].strip().lower()  

                if obj_type in type_to_class:
                    media_info = type_to_class[obj_type]
                    media_class = media_info["class"]
                    variable_name = media_info["variable"]      

                    my_object = media_class(
                        obj_type,
                        name=result[1],
                        director=result[2],
                        imdb_score=result[3],
                        url=result[4],
                        duration=result[5],
                        casts=result[6],
                        **{variable_name: result[7]}
                    )

                    PRODUCTS.append(my_object)
                else:
                    print(f"Unsupported type: {obj_type}")

''' ------------------------------------------------------------------------------------------------ '''     
"""
In Python, **{ variable_name: additional_info } is used to pass a variable number of keyword arguments to a function 
as a dictionary. The double asterisks (**) are used for unpacking the dictionary so that each key-value pair becomes
a separate keyword argument in the function call.
"""

def Add():
    obj_type = input("Enter object type (film, series, documentary, clip): ").strip().lower()

    type_to_class = {
        "film": {"class": Film, "variable": "genre", "type": "film"},
        "series": {"class": Series, "variable": "num_episodes", "type": "series"},
        "documentary": {"class": Documentary, "variable": "topic", "type": "documentary"},
        "clip": {"class": Clip, "variable": "category", "type": "clip"}
    }

    obj_type = obj_type.strip().lower()

    if obj_type in type_to_class:
        name = input("Enter name: ")
        director = input("Enter director: ")
        imdb_score = input("Enter IMDB score: ")
        url = input("Enter URL: ")
        duration = input("Enter duration: ")
        casts = input("Enter casts (& for separated): ")

        media_info = type_to_class[obj_type]
        media_class = media_info["class"]
        variable_name = media_info["variable"]
        media_type = media_info["type"] 

        additional_info = input(f"Enter {variable_name} information: ")

        my_object = media_class(
            media_type,
            name,
            director,
            imdb_score,
            url,
            duration,
            casts,
            **{variable_name: additional_info}
        )

        PRODUCTS.append(my_object)
        print("Item added successfully.")
    else:
        print(f"Unsupported type: {obj_type}")

''' ------------------------------------------------------------------------------------------------ '''     

def show_edit_menu():
    print("1- Edit name")
    print("2- Edit director")
    print("3- Edit IMDB score")
    print("4- Edit URL")
    print("5- Edit duration")
    print("6- Edit Casts")

def Edit():
    name = input("Enter the name of the media you want to edit: ").strip()

    found = False
    for product in PRODUCTS:
        if product.name.lower() == name.lower():
            found = True
            Show_Info(name)
            
            if isinstance(product, Film):
                show_edit_menu()
                print("7- Edit genre")
                choice = input("Enter your choice: ")
                if choice == '1':
                    new_name = input("Enter new name: ")
                    product.name = new_name
                elif choice == '2':
                    new_director = input("Enter new director: ")
                    product.director = new_director
                elif choice == '3':
                    new_imdb_score = input("Enter new IMDB score: ")
                    product.imdb_score = new_imdb_score
                elif choice == '4':
                    new_url = input("Enter new URL: ")
                    product.url = new_url
                elif choice == '5':
                    new_duration = input("Enter new duration: ")
                    product.duration = new_duration
                elif choice == '6':
                    new_casts = input("Enter new casts (& for separated): ")
                    product.casts = new_casts
                elif choice == '7':
                    new_genre = input("Enter new genre: ")
                    product.genre = new_genre
                else:
                    print("Invalid choice!")

            elif isinstance(product, Series):
                show_edit_menu()
                print("7- Edit num_episodes")
                choice = input("Enter your choice: ")
                if choice == '1':
                    new_name = input("Enter new name: ")
                    product.name = new_name
                elif choice == '2':
                    new_director = input("Enter new director: ")
                    product.director = new_director
                elif choice == '3':
                    new_imdb_score = input("Enter new IMDB score: ")
                    product.imdb_score = new_imdb_score
                elif choice == '4':
                    new_url = input("Enter new URL: ")
                    product.url = new_url
                elif choice == '5':
                    new_duration = input("Enter new duration: ")
                    product.duration = new_duration
                elif choice == '6':
                    new_casts = input("Enter new casts (& for separated): ")
                    product.casts = new_casts
                elif choice == '7':
                    new_num_episodes = input("Enter new num_episodes: ")
                    product.num_episodes = new_num_episodes
                else:
                    print("Invalid choice!")
                
            elif isinstance(product, Documentary):
                show_edit_menu()
                choice = input("Enter your choice: ")
                if choice == '1':
                    new_name = input("Enter new name: ")
                    product.name = new_name
                elif choice == '2':
                    new_director = input("Enter new director: ")
                    product.director = new_director
                elif choice == '3':
                    new_imdb_score = input("Enter new IMDB score: ")
                    product.imdb_score = new_imdb_score
                elif choice == '4':
                    new_url = input("Enter new URL: ")
                    product.url = new_url
                elif choice == '5':
                    new_duration = input("Enter new duration: ")
                    product.duration = new_duration
                elif choice == '6':
                    new_casts = input("Enter new casts (& for separated): ")
                    product.casts = new_casts
                elif choice == '7':
                    new_topic = input("Enter new topic: ")
                    product.topic = new_topic
                else:
                    print("Invalid choice!")
                
            elif isinstance(product, Clip):
                show_edit_menu()
                print("7- Edit category")
                choice = input("Enter your choice: ")
                if choice == '1':
                    new_name = input("Enter new name: ")
                    product.name = new_name
                elif choice == '2':
                    new_director = input("Enter new director: ")
                    product.director = new_director
                elif choice == '3':
                    new_imdb_score = input("Enter new IMDB score: ")
                    product.imdb_score = new_imdb_score
                elif choice == '4':
                    new_url = input("Enter new URL: ")
                    product.url = new_url
                elif choice == '5':
                    new_duration = input("Enter new duration: ")
                    product.duration = new_duration
                elif choice == '6':
                    new_casts = input("Enter new casts (& for separated): ")
                    product.casts = new_casts
                elif choice == '7':
                    new_category = input("Enter new category: ")
                    product.category = new_category
                else:
                    print("Invalid choice!")
                
            else:
                print("Unsupported product type!")

            print("Product edited successfully!")
            break

    if not found:
        print(f"Product with name '{name}' not found.")

''' ------------------------------------------------------------------------------------------------ '''     

def Remove():
    name = input("Enter the name of the product you want to delete: ").strip()

    found = False
    for product in PRODUCTS:
        if product.name.lower() == name.lower():
            found = True
            Show_Info(name)
            
            confirmation = input("Do you want to delete this product? (y/n): ").lower()
            if confirmation == 'y':
                PRODUCTS.remove(product)
                print(f"Product '{name}' deleted successfully!")
            else:
                print("Deletion canceled.")
            break

    if not found:
        print(f"Product with name '{name}' not found.")

''' ------------------------------------------------------------------------------------------------ '''     

"""
In Python, isinstance() is a built-in function used to check if an object is an instance of a specified class or any of its subclasses.
It returns True if the object is an instance of the class or subclass, and False otherwise. 
This function is commonly used for type checking and polymorphism in object-oriented programming.
"""
def Show_Info(name):
    
    found = False
    for product in PRODUCTS:
        if product.name.lower() == name.lower():
            found = True
            if isinstance(product, Film):
                print(f"Name: {product.name}")
                print("Type: Film")
                print(f"Director: {product.director}")
                print(f"IMDB Score: {product.imdb_score}")
                print(f"URL: {product.url}")
                print(f"Duration: {product.duration} minutes")
                print(f"Genre: {product.genre}")
                print("Casts:")
                casts=product.casts.split("&")
                for actor in casts:
                    print(f"- {actor.title()}")
                
            elif isinstance(product, Series):
                print(f"Name: {product.name}")
                print("Type: Series")
                print(f"Director: {product.director}")
                print(f"IMDB Score: {product.imdb_score}")
                print(f"URL: {product.url}")
                print(f"Duration: {product.duration} minutes")
                print(f"Number of Episodes: {product.num_episodes}")
                print("Casts:")
                casts=product.casts.split("&")
                for actor in casts:
                    print(f"- {actor.title()}")

            elif isinstance(product, Documentary):
                print(f"Name: {product.name}")
                print("Type: Documentary")
                print(f"Director: {product.director}")
                print(f"IMDB Score: {product.imdb_score}")
                print(f"URL: {product.url}")
                print(f"Duration: {product.duration} minutes")
                print(f"Topic: {product.topic}")
                print("Casts:")
                casts=product.casts.split("&")
                for actor in casts:
                    print(f"- {actor.title()}")

            elif isinstance(product, Clip):
                print(f"Name: {product.name}")
                print("Type: Clip")
                print(f"Director: {product.director}")
                print(f"IMDB Score: {product.imdb_score}")
                print(f"URL: {product.url}")
                print(f"Duration: {product.duration} minutes")
                print(f"Category: {product.category}")
                print("Casts:")
                casts=product.casts.split("&")
                for actor in casts:
                    print(f"- {actor.title()}")

    if not found:
        print(f"Media with name '{name}' not found.")

''' ------------------------------------------------------------------------------------------------ '''     

def advanced_search(min_duration, max_duration):
    found = False
    for product in PRODUCTS:
        if min_duration <= product.duration <= max_duration:
            found = True
            Show_Info(product.name)

    if not found:
        print(f"No Media found with duration between {min_duration} and {max_duration} minutes.")

''' ------------------------------------------------------------------------------------------------ '''     

def download(name):
    found = False
    for product in PRODUCTS:
        if product.name.lower() == name.lower():
            found = True
            Show_Info(name)
            user_choice=input("Do you want to download this movie? (y/n): ")
            if user_choice.lower() == 'y':
                if isinstance(product, Film):
                    product.download()
                else:
                    print("Error: This is not a film.")
            break

    if not found:
        print(f"Product with name '{name}' not found.")

''' ------------------------------------------------------------------------------------------------ '''     

def write_to_database():
    with open(file_path, 'w') as f:
        for product in PRODUCTS:
            if isinstance(product, Film):
                data = f"{product.type},{product.name},{product.director},{product.imdb_score},{product.url},{product.duration},{product.casts},{product.genre}"
            elif isinstance(product, Series):
                data = f"{product.type},{product.name},{product.director},{product.imdb_score},{product.url},{product.duration},{product.casts},{product.num_episodes}"
            elif isinstance(product, Documentary):
                data = f"{product.type},{product.name},{product.director},{product.imdb_score},{product.url},{product.duration},{product.casts},{product.topic}"
            elif isinstance(product, Clip):
                data = f"{product.type},{product.name},{product.director},{product.imdb_score},{product.url},{product.duration},{product.casts},{product.category}"
            else:
                print(f"Unsupported product type: {type(product)}")
                continue

            f.write(str(data)+"\n" )

''' ------------------------------------------------------------------------------------------------ '''       

print('Welcome to Py Store 🛒')
read_from_database()
print('Loading... Data is loaded successfully.')

while True:
    Show_menu()
    choice(int(input('Enter your choice: ')))
