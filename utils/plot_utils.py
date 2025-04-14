import matplotlib.pyplot as plt

def save_plot(fig, filename):
    fig.savefig(f'outputs/figures/{filename}.png', bbox_inches='tight')
    plt.close(fig)
