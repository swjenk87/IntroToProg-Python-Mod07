# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Understanding and applying the concepts
#              of pickling and error handling within
#              Python, through a multi-faceted script
#              that read and writes to a file.
# ChangeLog (Who,When,What):
# SJenkins,2023-08-27,Script framework created for Assignment 07
# SJenkins,2023-09-05,Completed coding work to complete Assignment 07
# ---------------------------------------------------------------------------- #

#  Modules - Import

#  The Pickle module implements binary protocols for serializing and de-serializing
import pickle

#  Data---------------------------------------------------------------------- #
#  Declare variables and constants
binary_file_name_str = "MathEquationsBinary.dat"  # Name of the binary file for storing equations
equation_list = []  # Placeholder list variable for equation storage
str_warning = "Warning: Your Equations List Doesn't Exist!"  # Create a warning message and check if it is being used
sum_final_equation = ""  # Equation string for adding to a list


#  Processing--------------------------------------------------------------- #

class Processor:
    """ Processing of file data """

    @staticmethod
    def read_data_from_binary(file_name, equation_list_rows):
        """ Reads data from a file into a list

        :param file_name: (string) with name of file:
        :param equation_list_rows: (list) you want filled with file data:
        :return: (list) list items
        """

        try:
            equation_list_rows.clear()  # clear current data
            obj_file = open(file_name, "rb")
            obj_file_data = pickle.load(obj_file)
            for line in obj_file_data:
                equation_list_rows.append(line)
            obj_file.close()
            print("Previous Data has been Loaded!")
            print("-" * 50)

            return equation_list_rows

        except:
            print(str_warning)
            print("Creating One for You Now!\n")

            obj_file = open(file_name, "wb")
            obj_file.close()
            print("Your Equations List has been Created!")
            print("-" * 50)

    @staticmethod
    def write_data_to_binary(file_name, equation_list_rows):
        """ List data is saved out to the dat file, overriding previous revisions

        :param file_name: (string) with name of file:
        :param equation_list_rows: (list) you want filled with file data:
        :return: nothing
        """
        obj_file = open(file_name, "wb")
        pickle.dump(equation_list_rows, obj_file)
        obj_file.close()

        return  # Return nothing

    @staticmethod
    def add_equation_list(list_of_rows, final_equation):
        """ Add equation to list

        :param list_of_rows: (list) List of equations:
        :param final_equation: (string) Final equation:
        :return: (list) of dictionary rows
        """

        item = [str(final_equation).strip()]
        list_of_rows.append(item)
        print("You're Equation has been Added! Remember to Save Before Exiting!")
        print("-" * 50)

        return list_of_rows


class MathProcessor:
    """ Performs math actions and operations """

    @staticmethod
    def numbers_addition(val01_sum, val02_sum):
        """ Performs a sum operation on two values

        :param val01_sum: (float) First input float value:
        :param val02_sum: (float) Second input float value:
        :return: (string) String operation
        """

        val_final_sum = float(round((val01_sum + val02_sum), 2))  # Sum rounded to two decimal places
        print("-" * 50)
        val_sum_str = str(val01_sum) + " + " + str(val02_sum) + " = " + str(val_final_sum)
        print("Your Equation is: ", val_sum_str)

        return val_sum_str

    @staticmethod
    def numbers_subtraction(val01_sub, val02_sub):
        """ Performs a subtraction operation on two values

        :param val01_sub: (float) First input float value:
        :param val02_sub: (float) Second input float value:
        :return: (string) String operation
        """

        val_final_dif = float(round((val01_sub - val02_sub), 2))  # Difference rounded to two decimal places
        print("-" * 50)
        val_dif_str = str(val01_sub) + " - " + str(val02_sub) + " = " + str(val_final_dif)
        print("Your Equation is: ", val_dif_str)

        return val_dif_str

    @staticmethod
    def numbers_multiplication(val01_mult, val02_mult):
        """ Performs a multiplication operation on two values

        :param val01_mult: (float) First input float value:
        :param val02_mult: (float) Second input float value:
        :return: (string) String operation
        """

        val_final_prod = float(round((val01_mult * val02_mult), 2))  # Difference rounded to two decimal places
        print("-" * 50)
        val_prod_str = str(val01_mult) + " * " + str(val02_mult) + " = " + str(val_final_prod)
        print("Your Equation is: ", val_prod_str)

        return val_prod_str

    @staticmethod
    def numbers_division(val01_div, val02_div):
        """ Performs a division operation on two values

        :param val01_div: (float) First input float value:
        :param val02_div: (float) Second input float value:
        :return: (string) String operation
        """

        try:
            val_final_div = float(round((val01_div / val02_div), 2))  # Difference rounded to two decimal places
            print("-" * 50)
            val_quo_str = str(val01_div) + " / " + str(val02_div) + " = " + str(val_final_div)
            print("Your Equation is: ", val_quo_str)

            return val_quo_str

        except ZeroDivisionError:
            print("You Cannot Divide by Zero, Please Enter Different Values!")
            div_zero = True

            return div_zero # Back to main with Div Bool

#  Presentation-------------------------------------------------------------- #

class IO:
    """ Display interactive menus and gather user input """

    @staticmethod
    def user_options_menu():
        """  Main menu for users to select operations to perform

        :return: nothing
        """

        print("Choose One of the Following Options: ")
        print("""
        1: Show Recent Calculations
        2: Perform a New Calculation
        3: Clear List
        4: Save to File 
        5: Exit Program
        """)

    @staticmethod
    def math_equation_menu():
        """  Selection of math operations

        :return: nothing
        """

        print("Select a Math Operation to Perform: ")
        print("""
        1: Addition (Sum)
        2: Subtraction (Difference)
        3: Multiplication (Product)
        4: Division (Quotient)
        5: Exit Menu
        """)

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: (string) String Selection:
        """

        menu_user_choice = str(input("What would you like to do? [1 to 5]: ")).strip()
        print()  # Formatting

        return menu_user_choice

    @staticmethod
    def user_value_input():
        """ Gets two float values from the user

        :return: (float) Float value 01, 02:
        """

        while (True):
            try:
                val01 = float(input("Enter One Float Value: ").strip())  # Attempt first float value from user

                break  # End loop

            except ValueError:
                print("Not a Number, Try Again")

                continue  # Back to the top of the loop

        while (True):
            try:
                val02 = float(input("Enter a Second Float Value: ").strip())  # Attempt second float value from user
                print()  # Formatting space

                break  # End loop

            except ValueError:
                print("Not a Number, Try Again")

                continue  # Back to the top of the loop

            print()  # Formatting

        return val01, val02

    @staticmethod
    def input_math_menu_choice():
        """ Gets the math equation menu choice from the user

        :return: (string) String Selection:
        """

        math_menu_user_choice = input("Which Math Equation would you like to Perform? [1 to 4]: ").strip()
        print()  # Formatting

        return math_menu_user_choice

    @staticmethod
    def print_recent_equations(list_of_equations):
        """ Displays

        :param list_of_equations: (list) Each Equation as List items
        :return: nothing
        """
        print("******* Recent Math Equations *******")
        if(len(list_of_equations) == 0):
            print("Your Recent Equations List is Empty, Try Adding Some!")

        else:
            for item in range(len(list_of_equations)):
                print(list_of_equations[item])

        print("*******************************************")
        print()  # Add an extra line for looks

#  Main ---------------------------------------------------------------------- #

#  Load any existing data from file
Processor.read_data_from_binary(file_name=binary_file_name_str, equation_list_rows=equation_list)

#  Process the user choices to perform actions and operations
while(True):
    IO.user_options_menu()  # Display the menu options to the user.
    user_choice_str = IO.input_menu_choice()  # Return a user's menu choice.

    if user_choice_str.strip() == '1':  # Show recent calculations (if they exist)
        IO.print_recent_equations(list_of_equations=equation_list)

        continue  # Back to menu

    elif user_choice_str.strip() == '2':  # Perform Math Calculations
        while(True):
            IO.math_equation_menu()  # Display the math equations menu
            math_menu_choice = IO.input_math_menu_choice()

            if math_menu_choice == '1':  # Sum Operation
                print("******* Enter Two Values Below *******")
                val01, val02 = IO.user_value_input()  # Receive two values from the user

                sum_final = MathProcessor.numbers_addition(val01_sum=val01, val02_sum=val02)  # Additional operation with user input values
                equation_list = Processor.add_equation_list(final_equation=sum_final, list_of_rows=equation_list)

                continue  # Back to menu

            elif math_menu_choice == '2':  # Difference Operation
                print("******* Enter Two Values Below *******")
                val01, val02 = IO.user_value_input()  # Receive two values from the user

                sub_final = MathProcessor.numbers_subtraction(val01_sub=val01, val02_sub=val02)  # Additional operation with user input values
                equation_list = Processor.add_equation_list(final_equation=sub_final, list_of_rows=equation_list)

                continue  # Back to menu

            elif math_menu_choice == '3':  # Multiplication Operation
                print("******* Enter Two Values Below *******")
                val01, val02 = IO.user_value_input()  # Receive two values from the user

                mult_final = MathProcessor.numbers_multiplication(val01_mult=val01, val02_mult=val02)  # Additional operation with user input values
                equation_list = Processor.add_equation_list(final_equation=mult_final, list_of_rows=equation_list)

                continue  # Back to menu

            elif math_menu_choice == '4':  # Division Operation
                print("******* Enter Two Values Below *******")
                val01, val02 = IO.user_value_input()  # Receive two values from the user
                div_final = MathProcessor.numbers_division(val01_div=val01, val02_div=val02)  # Additional operation with user input values

                if(div_final != True):
                    equation_list = Processor.add_equation_list(final_equation=div_final, list_of_rows=equation_list)

                else:
                    print("-" * 50)

                continue  # Back to menu

            elif math_menu_choice == '5':  # Exit operation menu
                print("Back to Main Menu!")
                print("-" * 50)

                break  # by exiting loop

    elif user_choice_str.strip() == '3':  # Clear List

        try:
            equation_list.clear()  # clear current data

        except:
            print("Your List is Already Empty!")

        continue  # Back to menu

    elif user_choice_str.strip() == '4':  # Save List to Dat File
        Processor.write_data_to_binary(file_name=binary_file_name_str, equation_list_rows=equation_list)
        print("The Equations Have Been Successfully Saved to the File!")
        print("-" * 50)

        continue  # Back to menu

    elif user_choice_str.strip() == '5':  # Exit Program
        print("Thanks for Using the Calculator!")

        break  # by exiting loop