from tkinter import *
import requests
import re
import tkinter.filedialog
import tkinter.messagebox
import os
import webbrowser
root = Tk()
root.title("CARBON FOOTPRINT CALCULATOR")

root.geometry("790x700")
root.minsize(1500,1400)
root.wm_iconbitmap('main_icon.ico')

def air_quality_index_calculator():
    new_window = Toplevel(root)
    new_window.title("Air Quality Index Calculator")
    new_window.geometry("790x700")
    new_window.minsize(1500,1400)
    new_window.wm_iconbitmap('main_icon.ico')
    canvas_width=1000
    canvas_height=800

    can4=Canvas(new_window,height=canvas_height,width=canvas_width)
    can4.pack(fill='both',expand=True)

    can4.create_rectangle(0, 0, 1800,1700,fill="light green")

    heading2=Label(can4,text="AIR QUALITY INDEX CALCULATOR",font="cosmicsams 30 bold",fg="yellow",bg="black")
    heading2.place(x=21, y=22)

    label=Label(new_window,text="Calculate your air quality index and make a contribution to climate protection : ",font="cosmicsams 18",fg="black", bg="light green").place(x=30,y=120)
    
    def get_air_quality():
        url = "https://carbonfootprint1.p.rapidapi.com/AirQualityHealthIndex"
        querystring = {"O3": o3_entry.get(), "NO2": no2_entry.get(), "PM": pm_entry.get()}
        headers = {
            "X-RapidAPI-Key": "a6be1dba08msh73dcb1d6f23488cp136b1ajsnaf8adb09ef96",
            "X-RapidAPI-Host": "carbonfootprint1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        response_text = response.json()  # Assuming response.json() returns a string
        numeric_part = re.sub(r'\D', '', response_text)  # Extract only numeric characters
        result = int(numeric_part)
        print(result)
        result_label.config(text=numeric_part)

    # Create entry widgets for O3, NO2, and PM
    o3_label = Label(new_window, text="Enter O3:")
    o3_label.place(x=100, y=200)

    o3_entry = Entry(new_window)
    o3_entry.place(x=300, y=200)

    no2_label = Label(new_window, text="Enter NO2:")
    no2_label.place(x=100, y=250)

    no2_entry = Entry(new_window)
    no2_entry.place(x=300, y=250)

    pm_label = Label(new_window, text="Enter PM:")
    pm_label.place(x=100, y=300)

    pm_entry = Entry(new_window)
    pm_entry.place(x=300, y=300)

    # Create a button to get the air quality
    get_button = Button(new_window, text="Get Air Quality", command=get_air_quality, font="cosmicsams 20 italic", padx=1, pady=2, relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
    get_button.place(x=100, y=350)

    # Create a label to display the result
    result_label = Label(new_window)
    result_label.place(x=100, y=400)


def open_new_window():
    
    root.withdraw()
    new_window = Toplevel(root)
    new_window.title("FOOTPRINT CALCULATOR")
    new_window.geometry("790x700")
    new_window.minsize(1500,1400)
    new_window.wm_iconbitmap('main_icon.ico')
    canvas_width=1000
    canvas_height=800

    can2=Canvas(new_window,height=canvas_height,width=canvas_width)
    can2.pack(fill='both',expand=True)

    can2.create_rectangle(0, 0, 1800,1700,fill="light green")

    heading2=Label(can2,text="HOUSEHOLD CARBON FOOTPRINT CALCULATOR",font="cosmicsams 30 bold",fg="yellow",bg="black")
    heading2.place(x=21, y=22)

    
    Menubar = Menu(new_window)
    new_window.config(menu=Menubar)
    
    
    # more info main landing page
    calculating_options_menu = Menu(Menubar, tearoff=0)
    # calculating_options_menu.add_command(label="For Flights", font="cosmicsams 10 italic",accelerator='Ctrl+N', command=more_info)
    calculating_options_menu.add_command(label="For Cars", font="cosmicsams 10 italic",accelerator='Ctrl+Q', command=new_window2)
    calculating_options_menu.add_command(label="For Buses and Railways", font="cosmicsams 10 italic",accelerator='Ctrl+Q', command=new_window3)
    calculating_options_menu.add_command(label="For Motorbike", font="cosmicsams 10 italic",accelerator='Ctrl+Q', command=new_window4)
    calculating_options_menu.add_command(label="Calculate Air Quality Index", font="cosmicsams 10 italic",accelerator='Ctrl+Q', command=air_quality_index_calculator)
    calculating_options_menu.add_separator()
    calculating_options_menu.add_command(label="Exit", font="cosmicsams 10 italic",accelerator='Ctrl+N', command=exit_editor)


    #calculate footprint
    more_info_menu = Menu(Menubar, tearoff=0)
    more_info_menu.add_command(label="more information", font="cosmicsams 10 italic",accelerator='Ctrl+N', command=more_info)
    
    
    
   
    # About
    About_menu = Menu(Menubar, tearoff=0)
    About_menu.add_command(label="About", font="cosmicsams 10 italic",accelerator='Ctrl+N', command=about_us)
    About_menu.add_separator()
    About_menu.add_command(label="Exit", font="cosmicsams 10 italic",accelerator='Ctrl+N', command=exit_editor)


    # MAIN MENU

    Menubar.add_cascade(label='CALCULATING OPTIONS', menu=calculating_options_menu)  # Add corresponding FILE menu here
    Menubar.add_cascade(label='MORE INFO',menu=more_info_menu)# Add corresponding EDIT menu here
    
    Menubar.add_cascade(label='ABOUT',menu=About_menu)  # Add corresponding ABOUT menu here
    

    label=Label(new_window,text="Your individual footprint is calculated by dividing the amount of energy by the number of people in your house.\n\nHow many people are in your household? ",font="cosmicsams 18",fg="black", bg="light green").place(x=50,y=90)



   


    #slider
    myslider1 = Scale(new_window,from_=0,to=10,orient=HORIZONTAL,tickinterval=10,length=400,sliderlength=50, width=20,font="cosmicsams 10 italic",relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)

    # to set initial value of slider
    # AGAR GAP KE HISSAB SE SET KARNA HO
    myslider1.set(10)
    myslider1.place(x=650,y=200)


    label=Label(new_window,text="To calculate your full household footprint, select 1 ",font="cosmicsams 18",fg="black", bg="light green").place(x=100,y=230)

    Electricity=Label(new_window,text="# Electricity (kWh): ",font="cosmicsams 18",fg="black", bg="light green").place(x=100,y=330)
    
    Natural_Gas=Label(new_window,text="# Natural Gas (therms): ",font="cosmicsams 18",fg="black", bg="light green").place(x=100,y=380)

    Heating_Oil=Label(new_window,text="# Heating Oil (Litres): ",font="cosmicsams 18",fg="black", bg="light green").place(x=100,y=430)

    Coal=Label(new_window,text="# Coal (tons): ",font="cosmicsams 18",fg="black", bg="light green").place(x=100,y=470)

    LPG=Label(new_window,text="# LPG (Litres): ",font="cosmicsams 18",fg="black", bg="light green").place(x=100,y=520)

    Propane=Label(new_window,text="# Propane (Litres): ",font="cosmicsams 18",fg="black", bg="light green").place(x=100,y=570)

    Wood=Label(new_window,text="# Wood (cords): ",font="cosmicsams 18",fg="black", bg="light green").place(x=100,y=620)


    #entry box

    # Create Entry widgets
    Electricity_entry = Entry(new_window, font="cosmicsams 18", fg="black", bg="light blue")
    Electricity_entry.place(x=400, y=330)

    Natural_Gas_entry = Entry(new_window, font="cosmicsams 18", fg="black", bg="light blue")
    Natural_Gas_entry.place(x=400, y=380)

    Heating_Oil_entry = Entry(new_window, font="cosmicsams 18", fg="black", bg="light blue")
    Heating_Oil_entry.place(x=400, y=430)

    Coal_entry = Entry(new_window, font="cosmicsams 18", fg="black", bg="light blue")
    Coal_entry.place(x=400, y=470)

    LPG_entry = Entry(new_window, font="cosmicsams 18", fg="black", bg="light blue")
    LPG_entry.place(x=400, y=520)

    Propane_entry = Entry(new_window, font="cosmicsams 18", fg="black", bg="light blue")
    Propane_entry.place(x=400, y=570)

    Wood_entry = Entry(new_window, font="cosmicsams 18", fg="black", bg="light blue")
    Wood_entry.place(x=400, y=620)
        
    # button1 = Button(new_window, text="Calculate Household Footprint", command=open_new_window, font="cosmicsams 30 italic", padx=1, pady=2, relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
    # button1.place(x=100, y=675)

    Total_House_Footprint=Label(new_window,text="Total House Footprint : ",font="cosmicsams 21 bold",fg="black",bg="light blue")
    Total_House_Footprint.place(x=780,y=330)
    # Create a rectangular box around the label
    can2.create_rectangle(770, 310, 1470, 380, outline="black", width=2, fill="light blue")


    def clear_entries():
            # Clear the entry boxes
            Electricity_entry.delete(0, END)
            Natural_Gas_entry.delete(0, END)
            Heating_Oil_entry.delete(0, END)
            Coal_entry.delete(0, END)
            LPG_entry.delete(0, END)
            Propane_entry.delete(0, END)
            Wood_entry.delete(0, END)
            
            # Clear the total footprint label
            Total_House_Footprint.config(text="Total House Footprint: ")
            
            # Remove the image
            image_label.config(image="")
        
    # Create a button to clear the entries
    clear_button = Button(new_window, text="Clear Entries", command=clear_entries, font="cosmicsams 20 italic", padx=1, pady=2, relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
    clear_button.place(x=600, y=675)
        

    def calculate_footprint():
        # Get the value of myslider1
        myslider1_value = myslider1.get()
        
        # Display the retrieved value in the terminal
        print("Value of myslider1:", myslider1_value)
        
        # Get the values from the entry boxes
        electricity = float(Electricity_entry.get())
        natural_gas = float(Natural_Gas_entry.get())
        heating_oil = float(Heating_Oil_entry.get())
        coal = float(Coal_entry.get())
        lpg = float(LPG_entry.get())
        propane = float(Propane_entry.get())
        wood = float(Wood_entry.get())
        
        
        
        
        
        # Print the values from the entry boxes
        print("Electricity (kWh):", electricity)
        print("Natural Gas (therms):", natural_gas)
        print("Heating Oil (gallons):", heating_oil)
        print("Coal (tons):", coal)
        print("LPG (gallons):", lpg)
        print("Propane (gallons):", propane)
        print("Wood (cords):", wood)

        #electricity calculation
        carbon_emission_factor=0.4071

        electricity1=((electricity*carbon_emission_factor)/myslider1_value)/1000

        
        print("footprint per person is ",electricity1,"metric tons of CO2e")



        #natural gas 


        carbon_emission_factor=0.2 #(kgCO2e/kWh)
        natural_gas1=((natural_gas * 0.2)/myslider1_value)/1000

        print("footprint per person is " , natural_gas1,"metric tons of CO2e")




        #heating oil

        # carbon emissions factor for heating oil is 2.68kgCO2e per US gallon.
        carbon_emission_factor1=0.0103
        heating_oil1=(((heating_oil/myslider1_value)*carbon_emission_factor1))
        print("footprint per person is " ,heating_oil1,"metric tons of CO2e")

        #coal
        #Carbon Emissions Factor = 0.34 kgCO2e per kWh
        coal1 = (coal / myslider1_value) * 0.34
        print("footprint per person is ", coal1, "metric tons of CO2e")

        #lpg
        lpg1= (lpg / myslider1_value) * 0.34
        print("footprint per person is ", lpg1, "metric tons of CO2e")


        #Propane
        propane1 = (propane/ myslider1_value) * 0.34
        print("footprint per person is ", propane1, "metric tons of CO2e")

        #wood
        wood1 = (wood / myslider1_value) * 0.34
        print("footprint per person is ", wood1, "metric tons of CO2e")

        # Calculate the total footprint
        total_footprint = electricity1 + natural_gas1 + heating_oil1 + coal1 + lpg1 + propane1 + wood1

        # Display the total footprint
        Total_House_Footprint.config(text="Total House Footprint: {:.5f} metric tones".format(total_footprint))

        # return total_footprint
        # output = calculate_footprint()
        # Image handling (assuming "CarbonFootprint.png" is in the same directory)
        image_path2 = "D:\programming\evs project\img2.png"

        image_path3 = "D:\programming\evs project\img3.png"
        if total_footprint > 50.00:
            # Check if image file exists
            if os.path.isfile(image_path2):
                # Load image using PIL (assuming it's installed)
                image = Image.open(image_path2)
                photo_image = ImageTk.PhotoImage(image)

                # Create image label with loaded image
                image_label = Label(new_window, image=photo_image)
                image_label.image = photo_image  # Keep a reference to avoid garbage collection
                image_label.place(x=910, y=390)  # Desired placement
            else:
                # Handle case where image is not found
                print("Error: Image file not found:", image_path2)
                # You can display an error message or a placeholder image here
        else:
            # Check if image file exists
            if os.path.isfile(image_path3):
                # Load image using PIL (assuming it's installed)
                image = Image.open(image_path3)
                photo_image = ImageTk.PhotoImage(image)

                # Create image label with loaded image
                image_label = Label(new_window, image=photo_image)
                image_label.image = photo_image  # Keep a reference to avoid garbage collection
                image_label.place(x=910, y=390)  # Desired placement
            else:
                # Handle case where image is not found
                print("Error: Image file not found:", image_path3)
                # You can display an error message or a placeholder image here
            
    # Create a button to calculate the footprint
    calculate_button = Button(new_window, text="Calculate Household Footprint", command=calculate_footprint, font="cosmicsams 20 italic", padx=1, pady=2, relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
    calculate_button.place(x=100, y=675)

    
        
   
   


#more info
def more_info():

    

    print("More information")  
    more_info_window = Toplevel(root)
    more_info_window.title("MORE INFORMATION")
    more_info_window.geometry("790x700")
    more_info_window.minsize(1500,1400)
    more_info_window.wm_iconbitmap('main_icon.ico')
    canvas_width=1000
    canvas_height=800

    can6=Canvas(more_info_window,height=canvas_height,width=canvas_width)
    can6.pack(fill='both',expand=True)

    can6.create_rectangle(0, 0, 1800,1700,fill="light green")
    
    heading2=Label(can6,text="MORE INFORMATION",font="cosmicsams 30 bold",fg="yellow",bg="black")
    heading2.place(x=21, y=22)

    label1=Label(more_info_window,text="# In India ,Energy is responsible for the majority of climate change-causing greenhouse gas emissions, mostly from the burning of fossil fuels. Despite efforts to reduce these emissions, the trajectory of CO2 emissions globally remains far higher than what is needed to avoid the worst effects of climate change.Note that numbers shown below refer to CO2 emissions from fuel combustion in the energy sector. They do not include other important sources of energy-related greenhouse gas emissions such as methane leaks from oil and gas operations, which are more difficult to measure. The Greenhouse Gas Emissions from Energy Data Explorer has more complete estimates for most countries and regions.",bg="light green",font="cosmicsams 21",fg="black",wraplength=canvas_width-100)
    label1.place(x=0,y=100)

    label3=Label(more_info_window,text="India's Share of global emissions",bg="light green",font="cosmicsams 25",fg="black",wraplength=canvas_width-100)
    label3.place(x=10,y=450)

    label4=Label(more_info_window,text="6.8 %",font="cosmicsams 30",fg="black",bg="light blue",wraplength=canvas_width-100)
    label4.place(x=500,y=450)

    label2=Label(more_info_window,text="# Your donation will help us to protect and restore nature, and to support the communities that depend on it. You will be a member, funding urgent direct conservation and advocacy. The power to protect and restore nature—now and for the next generation—is in your hands.To Donate Click on the Donate Button.",bg="light green",font="cosmicsams 21",fg="black",wraplength=canvas_width-100)
    label2.place(x=5,y=550)

    label5=Label(more_info_window,text="for more info click the more info button",bg="light green",font="cosmicsams 25",fg="black",wraplength=canvas_width-100)
    label5.place(x=10,y=725)

    def open_website1():
        webbrowser.open("https://www.iea.org/countries/india/emissions#what-are-the-main-sources-of-co2-emissions-in-india")  # Replace "https://www.example.com" with the desired website URL
    More_info=Button(more_info_window,text="MORE INFO",font="cosmicsams 25 italic",padx=1,pady=2,relief=SUNKEN,bg="darkblue",fg="Yellow",border=5,command=open_website1)
    More_info.place(x=950,y=700)

    def open_website():
        webbrowser.open("https://www.tncindia.in/donate-india/")  # Replace "https://www.example.com" with the desired website URL

    Donate = Button(more_info_window, text="DONATE", font="cosmicsams 25 italic", padx=1, pady=2, relief=SUNKEN, bg="darkblue", fg="Yellow", border=5, command=open_website)
    Donate.place(x=950, y=600)

    image_path2 = "D:\programming\evs project\oture2.png"
    if os.path.isfile(image_path2):
        # Load image using PIL (assuming it's installed)
        image = Image.open(image_path2)
        photo_image = ImageTk.PhotoImage(image)

        # Create image label with loaded image
        image_label = Label(more_info_window, image=photo_image)
        image_label.image = photo_image  # Keep a reference to avoid garbage collection
        image_label.place(x=890, y=100)  # Desired placement
    else:
        # Handle case where image is not found
        print("Error: Image file not found:", image_path2)
        # You can display an error message or a placeholder image here

more_info_func = more_info
new_window = open_new_window

    

def new_window2():
    print("New window 2")
    new_window2 = Toplevel(root)
    new_window2.title("CAR FOOTPRINT CALCULATOR")
    new_window2.geometry("790x700")
    new_window2.minsize(1500,1400)
    new_window2.wm_iconbitmap('main_icon.ico')
    canvas_width=1000
    canvas_height=800

    can3=Canvas(new_window2,height=canvas_height,width=canvas_width)
    can3.pack(fill='both',expand=True)

    can3.create_rectangle(0, 0, 1800,1700,fill="light green")

    heading2=Label(can3,text="CARS CARBON FOOTPRINT CALCULATOR",font="cosmicsams 30 bold",fg="yellow",bg="black")
    heading2.place(x=21, y=22)

    label=Label(new_window2,text="Calculate your car emissions and make a contribution to climate protection : ",font="cosmicsams 18",fg="black", bg="light green").place(x=30,y=120)
    
    label2=Label(new_window2,text="Number of cars : ",font="cosmicsams 18 bold",fg="black", bg="light green").place(x=60,y=230)


    
    #slider
    myslider2 = Scale(new_window2, from_=1, to=5, orient=HORIZONTAL, tickinterval=10,length=400,sliderlength=50, width=20, font="cosmicsams 10 italic", relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
    myslider2.set(1)
    myslider2.place(x=270, y=200)


    Distance=Label(new_window2,text="# Distance Travelled(km): ",font="cosmicsams 18",fg="black", bg="light green").place(x=60,y=330)
    
    Fuel_Type=Label(new_window2,text="# Fuel type(therms): ",font="cosmicsams 18",fg="black", bg="light green").place(x=60,y=400)

    Fuel_Consumption=Label(new_window2,text="# Fuel Consumptions : ",font="cosmicsams 18",fg="black", bg="light green")
    Fuel_Consumption.place(x=60,y=540)
    
    Car_Type=Label(new_window2,text="# Car Type :",font="cosmicsams 18",fg="black", bg="light green").place(x=60,y=470)


    # Create three radio buttons for different car types
    var = StringVar()
    radio1 = Radiobutton(new_window2, text="Compact Car", variable=var, value="Compact_car", font="cosmicsams 15 bold", relief=SUNKEN,
                            bg="lightblue", fg="black")
    radio1.place(x=210, y=470)
    radio2 = Radiobutton(new_window2, text="Mid-range Car", variable=var, value="Mid_range_car", font="cosmicsams 15 bold", relief=SUNKEN,
                            bg="lightblue", fg="black")
    radio2.place(x=380, y=470)
    radio3 = Radiobutton(new_window2, text="Luxury/SUV Car", variable=var, value="Luxury_SUV", font="cosmicsams 15 bold", relief=SUNKEN,
                            bg="lightblue", fg="black")
    radio3.place(x=561, y=470)


    #radio buttons for fuel type/
    var1 = StringVar()
    radio4 = Radiobutton(new_window2, text="Deisel", variable=var1, value="Deisel", font="cosmicsams 15 bold", relief=SUNKEN,
                            bg="lightblue", fg="black")
    radio4.place(x=280, y=400)
    radio5 = Radiobutton(new_window2, text="Electric", variable=var1, value="Electric", font="cosmicsams 15 bold", relief=SUNKEN,
                            bg="lightblue", fg="black")
    radio5.place(x=380, y=400)
    radio6 = Radiobutton(new_window2, text="Natural gas", variable=var1, value="Natural gas", font="cosmicsams 15 bold", relief=SUNKEN,
                            bg="lightblue", fg="black")
    radio6.place(x=490, y=400)
    radio7 = Radiobutton(new_window2, text="Petrol", variable=var1, value="Petrol", font="cosmicsams 15 bold", relief=SUNKEN,
                            bg="lightblue", fg="black")
    radio7.place(x=635, y=400)

    Distance_entry = Entry(new_window2, font="cosmicsams 24", fg="black", bg="light blue")
    Distance_entry.place(x=335, y=330) 

    Fuel_Consumption_entry = Entry(new_window2, font="cosmicsams 24", fg="black", bg="light blue")
    Fuel_Consumption_entry.place(x=450, y=540)

    def update_fuel_consumption(*args):
        fuel_type = var1.get()
        car_type = var.get()
        
        if fuel_type == "Deisel":
            if car_type == "Compact_car":
                unit = "L/100 km"
                value = "5.23"
            elif car_type == "Mid_range_car":
                unit = "L/100 km"
                value = "6.27"
            elif car_type == "Luxury_SUV":
                unit = "L/100 km"
                value = "8.39"
        elif fuel_type == "Electric":
            if car_type == "Compact_car":
                unit = "kWh/100km"
                value = "16.14"
            elif car_type == "Mid_range_car":
                unit = "kWh/100km"
                value = "19.19"
            elif car_type == "Luxury_SUV":
                unit = "kWh/100km"
                value = "23.65"
        elif fuel_type == "Natural gas":
            if car_type == "Compact_car":
                unit = "kg/100 km"
                value = "4.94"
            elif car_type == "Mid_range_car":
                unit = "kg/100 km"
                value = "6.08"
            elif car_type == "Luxury_SUV":
                unit = "kg/100 km"
                value = "7.22"
        elif fuel_type == "Petrol":
            if car_type == "Compact_car":
                unit = "L/100 km"
                value = "6.83"
            elif car_type == "Mid_range_car":
                unit = "L/100 km"
                value = "8.42"
            elif car_type == "Luxury_SUV":
                unit = "L/100 km"
                value = "10.01"
        else:
            unit = ""
            value = ""

        Fuel_Consumption_entry.delete(0, END)

        Fuel_Consumption_entry.insert(0,value)
        Fuel_Consumption.config(text=f"# Fuel Consumption ({unit}): ")

    # Bind the update function to the <<ComboboxSelected>> event of the radio buttons
    var.trace_add("write", update_fuel_consumption)
    var1.trace_add("write", update_fuel_consumption)
    


    def calculate_footprint2():
        update_fuel_consumption()
        # Get the value of myslider1
        myslider2_value = myslider2.get()
        
        # Display the retrieved value in the terminal
        print("Value of myslider2:", myslider2_value)
        
        # Get the values from the entry boxes
        distance = float(Distance_entry.get())
        fuel_consumption = float(Fuel_Consumption_entry.get())
        
         # Print the values from the entry boxes
        print("Distance :",distance)
        print("fuel Consumption :",fuel_consumption)
        
        Total_fuel_consumption = (distance * fuel_consumption)/100
        emission_factor=2.64
        Total_carbon_emission = ((Total_fuel_consumption * 2.64)/1000)*myslider2_value
        Total_carbon_emission = round(Total_carbon_emission, 5)
        print("Total Carbon Emission: {:.5f} metric tons of CO2e".format(Total_carbon_emission))

        # Display the total footprint
        Total_Car_Footprint.config(text="Total Car Footprint: {:.5f} metric tons ".format(Total_carbon_emission))

        image_path2 = "D:\programming\evs project\img2.png"

        image_path3 = "D:\programming\evs project\img3.png"
        if Total_carbon_emission > 50.00:
            # Check if image file exists
            if os.path.isfile(image_path2):
                # Load image using PIL (assuming it's installed)
                image = Image.open(image_path2)
                photo_image = ImageTk.PhotoImage(image)

                # Create image label with loaded image
                image_label = Label(new_window2, image=photo_image)
                image_label.image = photo_image  # Keep a reference to avoid garbage collection
                image_label.place(x=910, y=390)  # Desired placement
            else:
                # Handle case where image is not found
                print("Error: Image file not found:", image_path2)
                # You can display an error message or a placeholder image here
        else:
            # Check if image file exists
            if os.path.isfile(image_path3):
                # Load image using PIL (assuming it's installed)
                image = Image.open(image_path3)
                photo_image = ImageTk.PhotoImage(image)

                # Create image label with loaded image
                image_label = Label(new_window2, image=photo_image)
                image_label.image = photo_image  # Keep a reference to avoid garbage collection
                image_label.place(x=910, y=390)  # Desired placement
            else:
                # Handle case where image is not found
                print("Error: Image file not found:", image_path3)
                # You can display an error message or a placeholder image here
        
    Total_Car_Footprint=Label(new_window2,text="Total Car Footprint : ",font="cosmicsams 21 bold",fg="black", bg="light blue")
    Total_Car_Footprint.place(x=780,y=330)   


    # Create a rectangular box around the label
    can3.create_rectangle(770, 310, 1470, 380, outline="black", width=2, fill="light blue")    
        
        
        
        
    # Create a button to calculate the footprint
    calculate_button = Button(new_window2, text="Calculate Car Footprint", command=calculate_footprint2, font="cosmicsams 20 italic", padx=1, pady=2, relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
    calculate_button.place(x=100, y=675)

    
    def clear_entries():
            # Clear the entry boxes
            Distance_entry.delete(0, END)
            Fuel_Consumption_entry.delete(0, END)
            
            # Clear the total footprint label
            Total_Car_Footprint.config(text="Total House Footprint: ")
            
            # Remove the image
            image_label.config(image="")
        
    # Create a button to clear the entries
    clear_button = Button(new_window2, text="Clear Entries", command=clear_entries, font="cosmicsams 20 italic", padx=1, pady=2, relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
    clear_button.place(x=600, y=675)


        

def new_window3():
    print("New window 3")
    new_window3 = Toplevel(root)
    new_window3.title("BUS/RAIL FOOTPRINT CALCULATOR")
    new_window3.geometry("790x700")
    new_window3.minsize(1500,1400)
    new_window3.wm_iconbitmap('main_icon.ico')
    canvas_width=1000
    canvas_height=800

    can4=Canvas(new_window3,height=canvas_height,width=canvas_width)
    can4.pack(fill='both',expand=True)

    can4.create_rectangle(0, 0, 1800,1700,fill="light green")

    heading2=Label(can4,text="BUS AND RAIL CARBON FOOTPRINT CALCULATOR",font="cosmicsams 30 bold",fg="yellow",bg="black")
    heading2.place(x=21, y=22)

    #labels
    label=Label(new_window3,text="Calculate your bus and rail emissions and make a contribution to climate protection : ",font="cosmicsams 18",fg="black", bg="light green").place(x=30,y=120)

    Bus=Label(new_window3,text="Bus Distance (miles): ",font="cosmicsams 18",fg="black", bg="light green")
    Bus.place(x=60,y=300)

    Local_train=Label(new_window3,text="Local Bus Distance (miles): ",font="cosmicsams 18",fg="black", bg="light green")
    Local_train.place(x=60,y=350)

    Rickshaw=Label(new_window3,text="Rickshaw Distance (miles): ",font="cosmicsams 18",fg="black", bg="light green")
    Rickshaw.place(x=60,y=400)

    Long_Train=Label(new_window3,text="Long-Distance Train (miles): ",font="cosmicsams 18",fg="black", bg="light green")
    Long_Train.place(x=60,y=450)

    Taxi=Label(new_window3,text="Taxi Distance (miles): ",font="cosmicsams 18",fg="black", bg="light green")
    Taxi.place(x=60,y=500)

    Metro=Label(new_window3,text="Metro Distance (miles): ",font="cosmicsams 18",fg="black", bg="light green")
    Metro.place(x=60,y=550)

    label2=Label(new_window3,text="Number of persons : ",font="cosmicsams 18 bold",fg="black", bg="light green").place(x=60,y=200)
     
    # #slider
    # myslider3 = Scale(new_window3, from_=1, to=10, orient=HORIZONTAL, tickinterval=10,length=400,sliderlength=50, width=20, font="cosmicsams 10 italic", relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
    # myslider3.set(1)
    # myslider3.place(x=300, y=200)

    #entries
    Bus_entry = Entry(new_window3, font="cosmicsams 24", fg="black", bg="light blue")
    Bus_entry.place(x=380, y=300)

    Local_train_entry = Entry(new_window3, font="cosmicsams 24", fg="black", bg="light blue")
    Local_train_entry.place(x=380, y=350)

    Rickshaw_entry = Entry(new_window3, font="cosmicsams 24", fg="black", bg="light blue")
    Rickshaw_entry.place(x=380, y=400)

    Long_Train_entry = Entry(new_window3, font="cosmicsams 24", fg="black", bg="light blue")
    Long_Train_entry.place(x=380, y=450)

    Taxi_entry = Entry(new_window3, font="cosmicsams 24", fg="black", bg="light blue")
    Taxi_entry.place(x=380, y=500)

    Metro_entry = Entry(new_window3, font="cosmicsams 24", fg="black", bg="light blue")
    Metro_entry.place(x=380, y=550)

    Total_BUS_Footprint=Label(new_window3,text="Total Bus/Rail Footprint : ",font="cosmicsams 21 bold",fg="black", bg="light blue")
    Total_BUS_Footprint.place(x=780,y=330)


    def calculate_footprint3():
        pass


    def clear_entries():
            # Clear the entry boxes
            Bus_entry.delete(0, END)
            Local_train_entry.delete(0, END)
            Rickshaw_entry.delete(0, END)
            Long_Train_entry.delete(0, END)
            Taxi_entry.delete(0, END)
            Metro_entry.delete(0, END)
            
            # Clear the total footprint label
            Total_BUS_Footprint.config(text="Total House Footprint: ")
            
            # Remove the image
            image_label.config(image="")

    
    
        
    # Create a button to clear the entries
    clear_button = Button(new_window3, text="Clear Entries", command=clear_entries, font="cosmicsams 20 italic", padx=1, pady=2, relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
    clear_button.place(x=600, y=675)
    
    # Create a button to calculate the footprint
    calculate_button = Button(new_window3, text="Calculate Bus/Rail Footprint", command=calculate_footprint3, font="cosmicsams 20 italic", padx=1, pady=2, relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
    calculate_button.place(x=100, y=675)




def new_window4():
    print("New window 4")
    new_window4 = Toplevel(root)
    new_window4.title("BUS & RAIL FOOTPRINT CALCULATOR")
    new_window4.geometry("790x700")
    new_window4.minsize(1500,1400)
    new_window4.wm_iconbitmap('main_icon.ico')
    canvas_width=1000
    canvas_height=800

    can5=Canvas(new_window4,height=canvas_height,width=canvas_width)
    can5.pack(fill='both',expand=True)

    can5.create_rectangle(0, 0, 1800,1700,fill="light green")

    heading2=Label(can5,text="MOTORBIKE CARBON FOOTPRINT CALCULATOR",font="cosmicsams 30 bold",fg="yellow",bg="black")
    heading2.place(x=21, y=22)

    #labels
    label=Label(new_window4,text="Calculate your motorbike emissions and make a contribution to climate protection : ",font="cosmicsams 18",fg="black", bg="light green")
    label.place(x=30,y=120)

    label2=Label(new_window4,text="Number of Bikes : ",font="cosmicsams 18 bold",fg="black", bg="light green")
    label2.place(x=60,y=200)

    #slider
    myslider4 = Scale(new_window4, from_=1, to=5, orient=HORIZONTAL, tickinterval=10,length=400,sliderlength=50, width=20, font="cosmicsams 10 italic", relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
    myslider4.set(1)
    myslider4.place(x=270, y=200)

    Mileage=Label(new_window4,text="Motorbike Distance (km): ",font="cosmicsams 18",fg="black", bg="light green")
    Mileage.place(x=60,y=300)
    
    Mileage_entry = Entry(new_window4, font="cosmicsams 24", fg="black", bg="light blue")
    Mileage_entry.place(x=380, y=300)

    Bike_type=Label(new_window4,text="Bike Type : ",font="cosmicsams 18",fg="black", bg="light green")
    Bike_type.place(x=60,y=400)

    efficiency=Label(new_window4,text="Efficiency (g/km): ",font="cosmicsams 18",fg="black", bg="light green")
    efficiency.place(x=60,y=550)

    # Create three radio buttons for different car types
    var = StringVar()
    radio1 = Radiobutton(new_window4, text="small bike/ scooter upto 125cc", variable=var, value="Scooter", font="cosmicsams 15 bold", relief=SUNKEN,
                            bg="lightblue", fg="black")
    radio1.place(x=230, y=400)
    radio2 = Radiobutton(new_window4, text="Medium bike over 125cc & upto 500cc", variable=var, value="Medium_bike", font="cosmicsams 15 bold", relief=SUNKEN,
                            bg="lightblue", fg="black")
    radio2.place(x=230, y=440)
    radio3 = Radiobutton(new_window4, text="Large bike over 500cc", variable=var, value="Large_bike", font="cosmicsams 15 bold", relief=SUNKEN,
                            bg="lightblue", fg="black")
    radio3.place(x=230, y=480)

    efficiency_entry = Entry(new_window4, font="cosmicsams 24", fg="black", bg="light blue")
    efficiency_entry.place(x=290, y=550)
    
    def update_efficiency(*args):
        selected_bike_type = var.get()
        
        if selected_bike_type == "Scooter":
            value = "83.19"
        elif selected_bike_type == "Medium_bike":
            value = "101.08"
        elif selected_bike_type == "Large_bike":
            value = "132.52"
        else:
            value = ""

        efficiency_entry.delete(0, END)
        efficiency_entry.insert(0, value)

    # Bind the update function to the <<ComboboxSelected>> event of the radio buttons
    var.trace_add("write", update_efficiency)

    Total_Motorbike_Footprint=Label(new_window4,text="Total Motorbike Footprint : ",font="cosmicsams 21 bold",fg="black", bg="light blue")
    Total_Motorbike_Footprint.place(x=780,y=330)


    def calculate_footprint4():
        pass


    def clear_entries():
            # Clear the entry boxes
            efficiency_entry.delete(0, END)
            Mileage_entry.delete(0, END)
          
            
            # Clear the total footprint label
            Total_Motorbike_Footprint.config(text="Total Motorbike Footprint: ")
            
            # Remove the image
            image_label.config(image="")

    
    
        
    # Create a button to clear the entries
    clear_button = Button(new_window4, text="Clear Entries", command=clear_entries, font="cosmicsams 20 italic", padx=1, pady=2, relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
    clear_button.place(x=600, y=675)
    
    # Create a button to calculate the footprint
    calculate_button = Button(new_window4, text="Calculate Motorbike Footprint", command=calculate_footprint4, font="cosmicsams 20 italic", padx=1, pady=2, relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
    calculate_button.place(x=100, y=675)

def exit_editor(event=None):
    if tkinter.messagebox.askokcancel("Quit?", "Really quit?"):
        root.destroy()




def about_us():
    print("About us")
    about_us_window = Toplevel(root)
    about_us_window.title("ABOUT US")
    about_us_window.geometry("790x700")
    about_us_window.minsize(1500,1400)
    about_us_window.wm_iconbitmap('main_icon.ico')
    canvas_width=1000
    canvas_height=800

    can7=Canvas(about_us_window,height=canvas_height,width=canvas_width)
    can7.pack(fill='both',expand=True)

    can7.create_rectangle(0, 0, 1800,1700,fill="light green")
    
    heading2=Label(can7,text="ABOUT US",font="cosmicsams 30 bold",fg="yellow",bg="black")
    heading2.place(x=21, y=22)

    label1=Label(about_us_window,text="# We are a group of students from VIT BHOPAL UNIVERSITY , Madhya Pradesh. We are working on this project to spread awareness about the carbon footprint and its impact on the environment. We aim to educate people about the importance of reducing their carbon footprint and provide them with tools to calculate and reduce it. Our goal is to help people make more sustainable choices and protect the planet for future generations.\n\nFor more information, please visit our website or contact us directly.",bg="light green",font="cosmicsams 21",fg="black",wraplength=canvas_width-100)
    label1.place(x=0,y=100)

    label2=Label(about_us_window,text="for more info click the more info button",bg="light green",font="cosmicsams 25",fg="black",wraplength=canvas_width-100)
    label2.place(x=875,y=650)

    label3=Label(about_us_window,text="Made By : Shreyas Desai",bg="light Blue",font="cosmicsams 28",fg="black",wraplength=canvas_width-100)
    label3.place(x=1080,y=5)

        
    # Image handling (assuming "CarbonFootprint.png" is in the same directory)
    image_path = "D:\programming\evs project\environment.png"

    # Check if image file exists
    if os.path.isfile(image_path):
        # Load image using PIL (assuming it's installed)
        from PIL import Image, ImageTk

        image = Image.open(image_path)
        photo_image = ImageTk.PhotoImage(image)

        # Create image label with loaded image
        image_label = Label(can7, image=photo_image)
        image_label.image = photo_image  # Keep a reference to avoid garbage collection
        image_label.place(x=50, y=350)  # Desired placement
    else:
        # Handle case where image is not found
        print("Error: Image file not found:", image_path)
        # You can display an error message or a placeholder image here


        
    # Image handling (assuming "CarbonFootprint.png" is in the same directory)
    image_path2 = "D:\programming\evs project\environment2.png"

    # Check if image file exists
    if os.path.isfile(image_path2):
        # Load image using PIL (assuming it's installed)
        from PIL import Image, ImageTk

        image = Image.open(image_path2)
        photo_image = ImageTk.PhotoImage(image)

        # Create image label with loaded image
        image_label = Label(can7, image=photo_image)
        image_label.image = photo_image  # Keep a reference to avoid garbage collection
        image_label.place(x=900, y=100)  # Desired placement
    else:
        # Handle case where image is not found
        print("Error: Image file not found:", image_path2)
        # You can display an error message or a placeholder image here



    def open_website1():
        webbrowser.open("https://vit.ac.in/about/sustainability")  # Replace "https://www.example.com" with the desired website URL
    More_info=Button(about_us_window,text="MORE INFO",font="cosmicsams 25 italic",padx=1,pady=2,relief=SUNKEN,bg="darkblue",fg="Yellow",border=5,command=open_website1)
    More_info.place(x=1030,y=700)


    

canvas_width=1000
canvas_height=800

can1=Canvas(root,height=canvas_height,width=canvas_width)
can1.pack(fill='both',expand=True)

can1.create_rectangle(0, 0, 1800,1700,fill="light green")

heading=Label(can1,text="CARBON FOOTPRINT ",font="cosmicsams 50 bold",fg="yellow",bg="black")
heading.place(x=21, y=22)

carbon_footprint = Label(can1, text="Carbon footprint refers to the total amount of greenhouse gases (GHG), mainly carbon dioxide (CO2), that are released into the atmosphere as a direct or indirect result of your activities. It's a way to measure your impact on climate change.\n\nImagine your footprint is the trace you leave behind as you walk. Your carbon footprint is similar, but instead of leaving a mark on the ground, it represents the amount of greenhouse gases linked to your actions.\n\nHere's a breakdown of what contributes to your carbon footprint:\n\nDirect Emissions: These are the greenhouse gases you release through your daily activities. This includes driving a car, using electricity at home, or burning fossil fuels for heating.\n\nIndirect Emissions: These are emissions generated along the entire life cycle of the goods and services you consume. For example, when you buy a new shirt, there are emissions from manufacturing the fabric, transporting it, and selling it in stores.\n\n click below to find your carbon footprint!!!!!",font="cosmicsams 18",fg="black", bg="light green", wraplength=canvas_width-40)
carbon_footprint.place(x=21, y=130)


button1 = Button(root, text="Calculate Carbon Footprint", command=open_new_window, font="cosmicsams 30 italic", padx=1, pady=2, relief=SUNKEN, bg="darkblue", fg="Yellow", border=5)
button1.place(x=270, y=675)



# Image handling (assuming "CarbonFootprint.png" is in the same directory)
image_path = "D:\programming\evs project\CarbonFootprint1.png"

# Check if image file exists
if os.path.isfile(image_path):
    # Load image using PIL (assuming it's installed)
    from PIL import Image, ImageTk

    image = Image.open(image_path)
    photo_image = ImageTk.PhotoImage(image)

    # Create image label with loaded image
    image_label = Label(can1, image=photo_image)
    image_label.image = photo_image  # Keep a reference to avoid garbage collection
    image_label.place(x=980, y=180)  # Desired placement
else:
    # Handle case where image is not found
    print("Error: Image file not found:", image_path)
    # You can display an error message or a placeholder image here


root.mainloop()