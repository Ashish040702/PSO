import matplotlib.pyplot as plt
from g_main import *
from pso_main import *
from g_text import *
if __name__ == "__main__":
    # create graph
    graph = Graph(amount_vertices=11, starting_vertex=0)
    graph.generate_random_complete_graph()

    # create a PSO instance
    iterations = 49
    pso = PSO(graph, iterations=iterations, size_population=14, beta=1, alpha=0.9)
    pso.run()  # runs the PSO algorithm

        #plot the outcome of running pso over the graph and save to fig
    plt.plot(range(len(pso.annotatedEvolutions)), pso.annotatedEvolutions, color="y")
    plt.savefig("fig.png")

    # show the GUI
    gui = GUI_G(
        ncount=graph.amount_vertices,
        edges=graph.edges,
        particles=pso.particles,
        gbest_evolutions=pso.evolutions,
        gbest_evolutions_annotations=pso.annotatedEvolutions,
    )
    gui.run_path()   
    gui.run()
    # print the personal best of all particles
    print("After " + str(iterations) + " iterations :")
    print("---------------------------------------------------------------")
    pso.show_particles()  # shows the particles

    # print the global best parameters after completion of iterations
    print(
        "gbest: %s | cost: %d\n"
        % (pso.get_gbest().get_pbest(), pso.get_gbest().get_cost_pbest()))
     
