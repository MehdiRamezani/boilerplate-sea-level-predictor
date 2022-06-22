import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv(r"./epa-sea-level.csv")
    # print(r"df",df)

    ## there are Nan values, we drop them using .dropna()
    # df.dropna(how="all")
    df.dropna()

    
    # print(r"df",df)
  
    # print(type(df["Year"]))
  
    # print(type(df["CSIRO Adjusted Sea Level"]))
  
    
  
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.plot(df["Year"] , df["CSIRO Adjusted Sea Level"] , 'o', label=r'Original Data') #
  
    
    # Create first line of best fit
    ## linear regression:
    # res= linregress(df["Year"], df["CSIRO Adjusted Sea Level"] )
   
    slope, intercept, r, p, se = linregress(df["Year"].to_numpy(), df["CSIRO Adjusted Sea Level"].to_numpy() )

    new_x = np.arange(df["Year"][0], 2051)
  
    ax.plot(new_x, intercept+slope*new_x , 'r', label=r"1st fit")  

    print(intercept+slope*new_x)

    # Create second line of best fit
    new_x_2 = df[df["Year"] >= 2000]["Year"]

    new_y_2 = np.round_(df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"].to_numpy() , 7)
  
    slope_2, intercept_2, r_2, p_2, se_2 = linregress(new_x_2 , new_y_2 )

    new_x_2_new = np.arange(2000, 2051)
    ax.plot(new_x_2_new, intercept_2+slope_2*new_x_2_new , 'g', label=r"2nd fit") 

    # Add labels and title
    ax.legend(loc= 'best')
    ax.set(xlabel=r"Year", ylabel=r"Sea Level (inches)", title= r"Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
