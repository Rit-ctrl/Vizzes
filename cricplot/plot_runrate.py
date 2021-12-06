import matplotlib as mpl
import numpy as np

from cricplot.utils import rand_jitter

__all__ = ['plot_runrate']

# background = '#D7E5E5'
# mpl.rcParams['font.family']= 'Calibri'
# mpl.rcParams['font.size'] = 12
# mpl.rcParams['font.weight'] = 'bold'
# mpl.rcParams['legend.title_fontsize'] = 20
# mpl.rcParams['legend.fontsize'] = 17

def plot_runrate(ax,max_overs,team1_rpo,team1_fow,team2_rpo = None,team2_fow=None,color1='#03a9f4',color2='#dd0000',xtick_interval=2): 
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
    
    ax.grid(True, axis = 'y',ls='--', c='gray', alpha=0.5)
    
    #set x ticks
    ax.set_xticks([*range(1,max_overs+1,xtick_interval)])
    
    # turn off top and right spines
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    #set x limit
    ax.set_xlim([0,max_overs+1])
    
    #calc cumsum and run rate
    rr_team1 = team1_rpo.copy()
    rr_team1 = [run/(i+1) for i,run in enumerate(np.cumsum(rr_team1))]
    
    
    if team2_rpo !=None:
        rr_team2 = team2_rpo.copy()
        rr_team2 = [run/(i+1) for i,run in enumerate(np.cumsum(rr_team2))]
    else:
        rr_team2 = None
        
    
    if len(team1_fow) >0:
        team1_scatter_y = [+rr_team1[i-1] for i in team1_fow]
        #scatter the wickets
        ax.scatter(x=team1_fow,y=rand_jitter(team1_fow,team1_scatter_y),edgecolor=color1,color='white',s=100)    

    #plot team 1
    
    ax.plot(range(1,len(rr_team1)+1),rr_team1)
    

    if rr_team2!=None: #single plot or double plot check
        
        #plot team 2
#         ax.bar(x=indices,width=width,height=rpo_team2,align='edge',color=color2)
        ax.plot(range(1,len(rr_team2)+1),rr_team2)
    
        if len(team2_fow) >0:
            team2_scatter_y = [rr_team2[i-1] for i in team2_fow]
            ax.scatter(x=team2_fow,y=rand_jitter(team2_fow,team2_scatter_y),edgecolor=color2,color='white',s=100)         
        

    