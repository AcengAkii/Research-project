import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw  # Added missing import
import io


from matplotlib.patches import Rectangle

def table_results(df):
    # Assuming df has columns: 'Adjacency_Matrix', 'Graph_Image_1', 'Graph_Image_2'
    
    # Plotting the images along with the adjacency matrix values
    fig, axs = plt.subplots(len(df), 3, figsize=(15, len(df) * 5))  # 3 columns: adjacency matrix, first image, second image
    axs = axs.ravel()  # Flatten the 2D array of axes to iterate over it

    for i in range(len(df)):
        # Display adjacency matrix as an array
        adjacency_matrix = np.array(df['Adjacency_Matrix'][i])  # Convert to NumPy array
        axs[3*i].axis('off')  # Hide axes for cleaner display
        axs[3*i].text(0.5, 0.5, str(adjacency_matrix), fontsize=12, ha='center', va='center')  # Center text in the subplot
        
        # Set title based on the index
        if i == 0:
            axs[3*i].set_title("Graph Adjacency Matrix")
        else:
            axs[3*i].set_title("Complement Graph Adjacency Matrix")


        # Display first graph image
        axs[3*i+1].imshow(df['Graph_Image_1'][i])  # Image of the first graph
        if i == 0:
            axs[3*i+1].set_title("Graph visualization")
        else:
            axs[3*i+1].set_title("Complement graph Visualisation")

        axs[3*i+1].axis('off')  # Hide axes for cleaner display

        # Display second graph image
        axs[3*i+2].imshow(df['Graph_Image_2'][i])  # Image of the second graph
        if i == 0:
            axs[3*i+2].set_title("Clique identified")
        else :
            axs[3*i+2].set_title("Independent set identified")

        axs[3*i+2].axis('off')  # Hide axes for cleaner display

    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()
    
    


