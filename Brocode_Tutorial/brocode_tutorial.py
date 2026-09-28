import matplotlib.pyplot as plt  
import numpy as np
import pandas as pd

# #******************************CREATE A BASIC PLOT**************************************

# # x = [2023,2024,2025,2026]
# # y = [15,25,30,20]

# #using numpy
# x = np.array([2023,2024,2025,2026])
# y = np.array([15,25,30,20])
# y1 = np.array([45,7,18,1])
# y2 = np.array([39,47,35,54])


# # plt.plot(x,y)

# #******************************PLOT CUSTOMIZATION*********************************

# # plt.plot(x,y , marker=".", 
# #          markersize=20,  #or ms=20
# #          markerfacecolor="blue", #or mfc="blue"
# #          markeredgecolor="black" , #or mec="black"
# #          linestyle="--", #or dashed, dotteed , dashdot , None--> no line, solid
# #          linewidth=4,
# #          color="red" )  

# #or use dictionary
# line_style =dict(
#         # marker=".", 
#          markersize=20,  #or ms=20
#          markerfacecolor="blue", #or mfc="blue"
#          markeredgecolor="black" , #or mec="black"
#         #  linestyle="--", #or dashed, dotteed , dashdot , None--> no line, solid
#          linewidth=4,
#         #  color="red" 
# )  

# #plot using dict
# plt.plot(x,y,color="red", **line_style)
# plt.plot(x,y1, color = "green", **line_style)
# plt.plot(x,y2, color ="yellow", **line_style)

# #***************************LABELS***********************************

# plt.title("Class Size" , fontsize=20,
#                          family="Arial",
#                          fontweight = "bold",
#                          color="#2d4cfc"
# )
# plt.xlabel("Year" , fontsize=20,
#                     family="Arial",
#                     fontweight = "bold",
#                     color="#2d4cfc"
#           )
# plt.ylabel("Students" , fontsize=20,
#                         family="Arial",
#                         fontweight = "bold",
#                         color="#2d4cfc"
#           )
# plt.xticks(x)
# plt.tick_params(axis="both",
#                 colors="#2d4cfc"
#                 )


#***************************GRID LINES*********************************
#grid() = helps make plots easy to read by adding reference lines

# x = [1,2,3,4,5]
# y = [5,10,15,20,25]

# plt.plot(x,y)

# plt.grid(axis="x",
#          linewidth =2,
#          color="lightgray",
#          linestyle = "dashed"
#          )

#**************************BARCHARTS***********************************

# categories =np.array( ["Grains","Fruits","Vegetables","Protien","Dairy","Sweets"])
# values = np.array([4,3,2,5,3,1])

# # plt.bar(categories,values , color="red")

# #horizontal barchart
# plt.barh(categories,values , color="red")

# plt.title("Daily consumption")

# plt.xlabel("Food")
# plt.ylabel("Qunatity")


#**********************PIECHARTS*************************************

# categories =np.array( ["Freshmans", "Sophomores" ,"Juniors","Seniors"])
# values =np.array ([300,250,275,225])
# colors = ["red", "yellow" ,"blue", "green"]

# plt.pie(values, labels = categories,
#                 autopct ="%1.1f%%",
#                 colors =colors,
#                 explode=[0,0,0,0.1],
#                 shadow =True,
#                 startangle=90
#                 )
# plt.title("Bro Code College")


#**********************SCATTER GRAPHS*******************************
#s_graphs= shows relationship blw 2 variables

# x = [0,1,1,2,3,4,5,6,7,7,8] #Hours studied
# y =[55,60,65,62,68,70,75,78,82,85,87] #Marks

# x1 = [0,3,2,4,5,3,10,6,7,1] 
# y1 =[39,40,38,47,35,54,34,50,11,45]

# plt.scatter(x,y, color="red",
#             alpha =0.5, # transparency
#             s=100 ,#size 
#             label="Class A"
#             )
# plt.scatter(x1,y1, color="blue",
#             alpha =0.5, # transparency
#             s=100 ,#size 
#           label="Class B"  
#           )


# plt.title("Test Scores")

# plt.xlabel("Hours studied")
# plt.ylabel("Marks")

# plt.legend()

#************************Histograms***************************************
#a graphical chart that shows how numerical data is distributed by grouping values into continuous ranges, or "bins"

# scores = np.random.normal(loc=80, scale=10, size=100)
# scores = np.clip(scores , 0, 100)

# plt.hist(scores, bins=10,
#          color="lightgreen",
#          edgecolor="black"
#          )
# plt.title("Exams Scores")
# plt.xlabel("Score")
# plt.ylabel("No.of Students")

#**********************SUBPLOTS*********************************
#figure= entire canvas
#Ax= single plot (subplot)



# x = np.array([1,2,3,4,5])

# figure , axes = plt.subplots(2,2)
# # print(plt.subplots(2,2))

# axes[0,0].plot(x,x*2,color="red") #row=0, col=0
# axes[0,0].set_title("x*2")

# axes[0,1].bar(x,x**2, color="blue")
# axes[0,1].set_title("x**2")

# axes[1,0].hist(x,x**3, color="green")
# axes[1,0].set_title("x**3")

# axes[1,1].plot(x,x**4, color="purple")
# axes[1,1].set_title("x**4")
# plt.tight_layout()


#*********************Matplotlib + Pandas*************************

df = pd.read_csv("pokemon_data.csv")

type_count = (df["Type1"].value_counts(ascending=True))

plt.barh(type_count.index, type_count.values, color="lightgreen",
                                   edgecolor="black"
                                   )
plt.title("No of Pokemon by primary type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()

plt.show()