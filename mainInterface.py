# Name: Disaster Booklet
# Created for the MEC 2025
# Team Name: B1UE M00N
# Description: This app allows users to select the type of natural disaster they believe they are experiencing. 
# After that, it provides them with the typical warning signs and tips on what to do depending on the scenario.

# - Importing the module
import tkinter as tk

# Creating the first window
root = tk.Tk()
root.title("Natural Disasters")
root.geometry("400x450+550+135")
root['bg'] = "#9DBAE6"

# Title for the first window
title_label = tk.Label(root, text="Pick a Natural Disaster", font=("Arial", 18, "bold"), bg="#9DBAE6")
title_label.pack(pady=20)

# List of disasters for the first window
disasters = [
    "Floods",
    "Wildfire",
    "Hailstorm",
    "Hurricane",
    "Blizzard",
    "Thunderstorms",
    "Tornados"
]

# Function to open a the second window
def open_info_window(disaster):
    #List for storing the information about the warning signs of each disaster
    TextSigns=[
        '• Heavy rainfall\n• Water accumulating on roads\n• Loud roaring sound',
        '• Fire moving at a high rate and spreading fast\n• Presence of fire swirls\n• Watch alerts',
        '• Rapid temperature drop\n• Strong winds\n• Lumps of ice falling from the sky',
        '• Thunderstorms that produce strong winds\n• Flooding',
        '• Heavy snow\n• Windy',
        '• Strong, high winds moving branches and debris\n• Poor visibility from heavy rain or dust\n• Flash flooding in low-lying areas\n• If you can hear thunder, you are within striking distance of lightning',
        '• Very dark clouds, sometimes green or yellow skies\n• Rotating, funnel-shaped cloud at the base of a storm\n• Loud rumbling or roaring, like a train\n• Strong winds lifting debris '
    ]
    #List for storing the information about the actions to take of each disaster
    TextTips=[
        "• If a flood warning is issued for your area, go to higher ground\n• Wear protective clothing - including rubber boots\n• Avoid walking through puddles - they could be deeper than you think\n• Keep children and pets away from the water",
        "You're inside your home:\n• Choose a room you can close off from outside air and set up a portable air filter to filter out smoke\n• Seal any gaps and wet down towels and put them around you "
        "\n\nEvacuating:\n• Stay up to date on any information about the wildfires\n• Pack an emergency to-go bag\n• Secure your home by closing windows and doors and get flammable materials away from the house. ",
        "If driving:\n• Pull over\n• Face away from the windows\n\nIf outdoors:\n• Seek shelter and stay away from windows\n• If you cannot find a shelter\n• Face away from the wind, crouch down, protect your head\n• Stay away from trees, towers and poles",
        "You're inside your home:\n• Install shutters to cover any glass windows or doors to prevent glass from shattering everywhere. Make sure all windows and doors are shut.\n• Use sandbags to divert the water away and elevate electrical systems. "
        "\n\nEvacuating:\n• Know the area where the shelters are and use GPS to help avoid road closures.\n• Make sure you have your essential documents. ",
        "You're in your car:\n• Keep an emergency kit inside your car and make sure you have a full tank of gas in case anything happens\n• Pull over if necessary and wait till visibility improves. If not slow down when driving."
        "\n\nInside your home and if heat goes out:\n• Wear layers of clothes to stay warm if the heat\n• Close off unwanted rooms and stuff towels in cracks in doors\n• Eat food and drink water. Food provides energy for the body to produce its own heat.",
        "• Stay indoors, away from windows and anything that conducts electricity\n• Avoid using electrical appliances or metal objects\n• If in a vehicle, stay inside a fully enclosed metal "
        "car and avoid floodwaters\n• Do not exit the vehicle if there are fallen power lines nearby; wait for help\n• If outdoors, seek shelter in a building or low-lying area, avoiding open areas, high locations, and water ",
        "• Go to the lowest floor, away from windows\n• Get under something sturdy and don't take shelter where there are heavy objects on the floor directly above you\n• Always protect your head and neck with arms or a helmet\n• If outside, lie flat in a ditch or low area and cover your head; don't try to outrun a tornado\n• Avoid mobile homes, vehicles, trees, large objects, bridges, and overpasses "
    ]

    # Extract plain name and extract the informations for warning signs and tips for each disaster
    disaster_name = disaster.split()[0]
    i = disasters.index(disaster)
    dataSigns = TextSigns[i]
    dataTips = TextTips[i]

    # Creating the second window
    info_window = tk.Toplevel(root)
    info_window.title(disaster_name)
    info_window.geometry("1000x525+250+135")
    info_window['bg'] = "#E6EEF8"

    # Title for second window
    title = tk.Label(info_window, text=disaster_name, font=("Arial", 20, "bold"), bg="#E6EEF8")
    title.pack(pady=15)

    # Creating the main content frame (Left + Right sections)
    content_frame = tk.Frame(info_window, bg="#E6EEF8")
    content_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Creating the left frame
    left_frame = tk.Frame(content_frame, bg="#E6EEF8")
    left_frame.pack(side="left", padx=30)

    # Load image (use try/except to skip missing ones)
    try:
        img_name = disaster_name.lower() + "Image.png"   # e.g. "floodImage.png"
        disaster_img = tk.PhotoImage(file=img_name)
        img_label = tk.Label(left_frame, image=disaster_img, bg="#E6EEF8")
        img_label.image = disaster_img  # keep a reference
        img_label.pack()
    except:
        img_label = tk.Label(left_frame, text="[Image Missing]", font=("Arial", 12), bg="#E6EEF8")
        img_label.pack()

    # Creating the right frame (Signs + Tips)
    right_frame = tk.Frame(content_frame, bg="#E6EEF8")
    right_frame.pack(side="left", fill="both", expand=True, padx=20)

    # Section 1: Warning Signs
    signs_title = tk.Label(right_frame, text="Warning Signs:", font=("Arial", 14, "bold"), anchor="w", bg="#E6EEF8")
    signs_title.pack(anchor="w", pady=(10, 5))
    signs_text = tk.Label(right_frame, text=dataSigns,
                          justify="left", wraplength=400, bg="#E6EEF8", font=("Arial", 12))
    signs_text.pack(anchor="w", pady=(0, 20))

    # Section 2: Actions to take
    tips_title = tk.Label(right_frame, text="What to do:", font=("Arial", 14, "bold"), anchor="w", bg="#E6EEF8")
    tips_title.pack(anchor="w", pady=(5, 5))
    tips_text = tk.Label(right_frame, text=dataTips,
                         justify="left", wraplength=425, bg="#E6EEF8", font=("Arial", 12))
    tips_text.pack(anchor="w", pady=(0, 20))

    # Create the close button
    close_btn = tk.Button(info_window, text="Close", command=info_window.destroy, bg="#A4B9E0")
    close_btn.pack(pady=10)

    # When X is clicked, destroy this window (but keep main open)
    info_window.protocol("WM_DELETE_WINDOW", info_window.destroy)

# Create buttons for each disaster
for disaster in disasters:
    frame = tk.Frame(root, borderwidth=2, relief="ridge", pady=5, bg="#C7D6EE")
    frame.pack(padx=10, pady=5, fill="x")

    name_label = tk.Label(frame, text=disaster, font=("Arial", 12), bg="#C7D6EE")
    name_label.pack(side="left")

    select_button = tk.Button(frame, text="Select", command=lambda d=disaster: open_info_window(d))
    select_button.pack(side="right", padx=10)

root.mainloop()