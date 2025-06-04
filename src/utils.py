import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Component
Attrition_Flag_map = {"Existing Customer": 1, "Attrited Customer": 0}
Gender_map = {"M": 1, "F": 0}
Education_Level_map = {
    "Unknown": -1,
    "Uneducated": 0,
    "High School": 1,
    "College": 2,
    "Graduate": 3,
    "Post-Graduate": 4,
    "Doctorate": 5
}
Marital_Status_map = {
    "Unknown": -1,
    "Single": 0,
    "Married": 1,
    "Divorced": 2
}
Income_Category_map = {
    "Unknown": -1,
    "Less than $40K": 0,
    "$40K - $60K": 1,
    "$60K - $80K": 2,
    "$80K - $120K": 3,
    "$120K +": 4
}
Card_Category_map = {
    "Blue": 0,
    "Gold": 1,
    "Silver": 2,
    "Platinum": 3
}

# Functions
def view_columns(data):
    for index, col in enumerate(data.columns):
        print(f"{index + 1}. {col}")
        
def simple_bar_plot(data, x, y, ax):
    plt.rcParams["font.size"] = 9
    sns.countplot(
        data=data,
        x=f"{x}",
        hue=f"{y}",
        ax=ax,
        palette="YlGnBu",
        legend="full"
    )

    ax.set(xlabel=None, ylabel=None)
    ax.spines[["top", "right", "bottom", "left"]].set_visible(False)

    legend = ax.get_legend()
    if legend:
        legend.set_loc('upper right')
        legend.set_bbox_to_anchor((1.2, 0.9))
        legend.set_frame_on(False)
        legend.set_title("")

    for container in ax.containers:
        for bar in container:
            bar_color = bar.get_facecolor()
            ax.bar_label(
                container=container, 
                fmt="%d", 
                padding=3, 
                color=bar_color
            )
            
    max_height = max([bar.get_height() for container in ax.containers for bar in container])
    ax.set_ylim(top=max_height * 1.25)

def simple_hist_plot(data, x, y, ax):
    for label in sorted(data[y].dropna().unique()):
        if label != 0:
            continue
        subset = data[data[y] == label]
        ax.hist(
            subset[x],
            label=f"{y} = {label}",
            color="#327BA5",
            bins=10
        )
    
    ax.set(xlabel=None, ylabel=None)
    ax.spines[["top", "right", "bottom", "left"]].set_visible(False)
    
    legend = ax.get_legend()
    if legend:
        legend.set_loc("upper right")
        legend.set_bbox_to_anchor((1.2, 0.9))
        legend.set_frame_on(False)
        legend.set_title("")
        
    for container in ax.containers:
        for bar in container:
            bar_color = bar.get_facecolor()
            ax.bar_label(
                container=container,
                fmt="%d",
                padding=3,
                color=bar_color
            )
            
    max_height = max([bar.get_height() for container in ax.containers for bar in container])
    ax.set_ylim(top=max_height * 1.25)
    
def simple_scatter_plot(
    data, 
    x, 
    y, 
    ax=None,
    hue="Attrition_Flag", 
    color="#327BA5",
    alpha=0.3
):
    max_x = data[f"{x}"].max()
    max_y = data[f"{y}"].max()
    
    if ax is None:
        fig, ax = plt.subplots()

    if hue is not None:
        sns.scatterplot(
            data=data,
            x=f"{x}",
            y=f"{y}",
            hue=f"{hue}",
            palette="YlGnBu",
            alpha=alpha
        )
    else:
        sns.scatterplot(
            data=data,
            x=f"{x}",
            y=f"{y}",
            color=f"{color}",
            alpha=alpha
        )

    ax.set(xlabel="", ylabel="")
    ax.spines[["top", "right", "bottom", "left"]].set_visible(False)

    legend = ax.get_legend()
    if legend:
        legend.set_loc("upper right")
        legend.set_bbox_to_anchor((1.3, 1.0))
        legend.set_frame_on(False)
        legend.set_title(False)
        
    ax.set_ylim(top=max_y*1.05)
    ax.set_xlim(right=max_x*1.05)

    plt.show()
    