__all__ = ['draw_pitch']


def draw_pitch(ax,linecolor='white',facecolor = '#e4c888'):
    '''
    ax : matplotlib axes for plotting
    linecolor : color for the pitch lines (crease) (optional)
    facecolor : color for the pitch (optional)
    '''
    ax.set_facecolor(facecolor)
    # linecolor = 'white'

    # ax.set_xlim([-1.22,1.22])
    # ax.set_ylim([0,22.56])
    ax.set_aspect(0.33)
    ax.invert_yaxis()

    #outer dimensions
    ax.plot([-1.83,1.83],[22.56,22.56],color = linecolor)
    ax.plot([-1.83,1.83],[0,0],color = linecolor)

    ax.plot([-1.83,-1.83],[0,22.56],color = linecolor)
    ax.plot([1.83,1.83],[0,22.56],color = linecolor)

    #popping crease
    ax.plot([-1.83,1.83],[2.44,2.44],color = linecolor)
    ax.plot([-1.83,1.83],[22.56-2.44,22.56-2.44], color= linecolor)

    #wid line
    ax.plot([-1.32,1.32],[1.22,1.22],color=linecolor)
    ax.plot([-1.32,1.32],[22.56-1.22,22.56-1.22],color=linecolor)

    ax.plot([-1.32,-1.32],[0,1.22*2],color=linecolor)
    ax.plot([1.32,1.32],[0,1.22*2],color=linecolor)
    ax.plot([-1.32,-1.32],[22.56-0,22.56-1.22*2],color=linecolor)
    ax.plot([1.32,1.32],[22.56-0,22.56-1.22*2],color=linecolor)

    ax.scatter([0,0.1143,-0.1143,0,0.1143,-0.1143],[1.22,1.22,1.22,22.56-1.22,22.56-1.22,22.56-1.22],c=linecolor)

    # ax.axvline(0)
    # ax.axvline(-0.1143)
    # ax.axvline(0.1143)

    ax.set_xlim([-1.83,1.83])

    for spine in ['top', 'right','left','bottom']:
            ax.spines[spine].set_visible(False)
