from cricplot.utils import rand_jitter
import numpy as np
import matplotlib as mpl

__all__ = ['plot_manhattan']


# # background = '#D7E5E5'
# mpl.rcParams['font.family']= 'Calibri'
# mpl.rcParams['font.size'] = 12
# mpl.rcParams['font.weight'] = 'bold'
# mpl.rcParams['legend.title_fontsize'] = 20
# mpl.rcParams['legend.fontsize'] = 17

def plot_manhattan(ax,max_overs,team1_rpo,team1_fow,team2_rpo = None,team2_fow=None,color1='#03a9f4',color2='#dd0000',xtick_interval=2): 
    '''
    ax: matplotlib axes to plot
    max_overs: max overs in an innings
    team1_rpo: list containing runs per over of team 1 
    team1_fow: list containing overs where wicket fell
    team2_rpo: list containing runs per over of team 2 (optional)
    team2_fow: list containing overs where wicket fell (optional)
    color1: color for team 1 (optional)
    color2: color for team 2 (optional)
    xtick_interval: interval for xtick (default = 2)
    '''

    # grid lines
    ax.grid(True, axis = 'y',ls='--', c='gray', alpha=0.5)
    
    #set x ticks
    ax.set_xticks([*range(1,max_overs+1,xtick_interval)])
    
    # turn off top and right spines
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    #set x limit
    ax.set_xlim([0,max_overs+1])
    
    #copy runs per over data
    rpo_team1 = team1_rpo.copy()
    if team2_rpo !=None:
        rpo_team2 = team2_rpo.copy()
    else:
        rpo_team2 = None

    # if innings finished before stipulated over limits, pad with dummy data
    if len(rpo_team1) < max_overs:
        rpo_team1.extend([0]*(max_overs - len(rpo_team1)))
        
    if rpo_team2 != None:
        if len(rpo_team2) < max_overs:
            rpo_team2.extend([0]*(max_overs - len(rpo_team2)))
    
    #set indices for x values
    indices = [*range(1,max_overs+1,1)]
    width = np.min(np.diff(indices))/3
    
    
    if len(team1_fow) >0:
        team1_scatter_y = [0.3+rpo_team1[i-1] for i in team1_fow]

    if rpo_team2!=None: #single plot or double plot check
        
        #plot double
        
        ax.bar(x=indices-width,width = width,height = rpo_team1,align='edge',color=color1)
        if len(team1_fow)>0:
            ax.scatter(x=team1_fow-width/2,y=rand_jitter(team1_fow,team1_scatter_y),edgecolor=color1,color='white',s=100)
        
        ax.bar(x=indices,width=width,height=rpo_team2,align='edge',color=color2)
        
        if len(team2_fow) >0:
            team2_scatter_y = [0.3+rpo_team2[i-1] for i in team2_fow]
            ax.scatter(x=team2_fow+width/2,y=rand_jitter(team2_fow,team2_scatter_y),edgecolor=color2,color='white',s=100)

        
    else:         
        
        ax.bar(x=indices,height = rpo_team1,color=color1)
        if len(team1_fow)>0:
            ax.scatter(x=team1_fow,y=rand_jitter(team1_fow,team1_scatter_y),edgecolor=color1,color='white',s=100)    
