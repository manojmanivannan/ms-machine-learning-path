from matplotlib import pyplot as plt
import scipy.stats as stats

# Create a function that we can re-use
def show_distribution(var_data,title,figsize=(10,6)):
    '''
    This function will make a distribution (graph) and display it
    '''

    # Get statistics
    min_val = var_data.min()
    max_val = var_data.max()
    mean_val = var_data.mean()
    med_val = var_data.median()
    mod_val = var_data.mode()[0]

    print('Minimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'.format(min_val,
                                                                                            mean_val,
                                                                                            med_val,
                                                                                            mod_val,
                                                                                            max_val))

    # Create a figure for 2 subplots (2 rows, 1 column)
    fig, ax = plt.subplots(2, 1, figsize = figsize)

    # Plot the histogram   
    ax[0].hist(var_data)
    ax[0].set_ylabel('Frequency')

    # Add lines for the mean, median, and mode
    ax[0].axvline(x=min_val, color = 'gray', linestyle='dashed', linewidth = 2, label='Min:'+str(round(min_val,2)))
    ax[0].axvline(x=mean_val, color = 'cyan', linestyle='dashed', linewidth = 2, label='Mean:'+str(round(mean_val,2)))
    ax[0].axvline(x=med_val, color = 'red', linestyle='dashed', linewidth = 2, label='Median:'+str(round(med_val,2)))
    ax[0].axvline(x=mod_val, color = 'yellow', linestyle='dashed', linewidth = 2, label='Mode:'+str(round(mod_val,2)))
    ax[0].axvline(x=max_val, color = 'gray', linestyle='dashed', linewidth = 2, label='Max:'+str(round(max_val,2)))
    ax[0].legend()

    # Plot the boxplot   
    ax[1].boxplot(var_data, vert=False)
    ax[1].set_xlabel('Value')
    
    # Add a title to the Figure
    fig.suptitle(f'Data Distribution of {title}')
    ax[0].legend()

def show_density(var_data,title):
    fig = plt.figure(figsize=(10,4))

    # Plot density
    var_data.plot.density()

    # Add titles and labels
    plt.title(f'Data Density of {title}')

    # Show the mean, median, and mode
    plt.axvline(x=var_data.mean(), color = 'cyan', linestyle='dashed', linewidth = 2, label='Mean:'+str(round(var_data.mean(),2)))
    plt.axvline(x=var_data.median(), color = 'red', linestyle='dashed', linewidth = 2, label='Mean:'+str(round(var_data.median(),2)))
    plt.axvline(x=var_data.mode()[0], color = 'yellow', linestyle='dashed', linewidth = 2, label='Mean:'+str(round(var_data.mode()[0],2)))
    plt.legend()
    # Show the figure
    plt.show()
    
def show_distribution_curve(col, title):
    # get the density
    density = stats.gaussian_kde(col)

    # Plot the density
    col.plot.density(label=f'{title} dist. curve')

    # Get the mean and standard deviation
    s = col.std()
    m = col.mean()

    # Annotate 1 stdev
    x1 = [m-s, m+s]
    y1 = density(x1)
    plt.plot(x1,y1, color='magenta')
    plt.annotate('1 std (68.26%)', (x1[1],y1[1]))

    # Annotate 2 stdevs
    x2 = [m-(s*2), m+(s*2)]
    y2 = density(x2)
    plt.plot(x2,y2, color='green')
    plt.annotate('2 std (95.45%)', (x2[1],y2[1]))

    # Annotate 3 stdevs
    x3 = [m-(s*3), m+(s*3)]
    y3 = density(x3)
    plt.plot(x3,y3, color='orange')
    plt.annotate('3 std (99.73%)', (x3[1],y3[1]))

    # Show the location of the mean
    plt.axvline(col.mean(), color='cyan', linestyle='dashed', linewidth=1, label='Mean:'+str(round(col.mean(),2)))
    plt.legend()
    plt.axis('off')
    plt.suptitle(f'Distrubution of {title}')

    plt.show()