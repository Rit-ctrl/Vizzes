__all__ = ['draw_stumpview']

def draw_stumpview(ax,linecolor = 'white',facecolor = '#e4c888'):
    '''
    ax : matplotlib axes for plotting
    linecolor : color for the pitch lines (crease) (optional)
    facecolor : color for the pitch (optional)
    '''
    
    ax.set_facecolor(facecolor)
    ax.set_aspect(1)
    # ax.set_xlim([-2,2])

    #horizontal line
    ax.plot([-1.83,1.83],[0,0],color = linecolor)

    #stumps
    ax.plot([-0.1143,-0.1143],[0,0.711],color=linecolor)
    ax.plot([0,0],[0,0.711],color=linecolor)
    ax.plot([0.1143,0.1143],[0,0.711],color=linecolor)

    #bails
    ax.plot([0,0.1095],[0.711,0.711],color=linecolor)
    ax.plot([0,-0.1095],[0.711,0.711],color=linecolor)

