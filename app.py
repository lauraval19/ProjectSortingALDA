from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from sortalgorithms import execution_time_gathering


def main():
    """
    create figure process for selection_sort,merge_sort and insertion_sort
    @return: graph with time comparasion
    """
    times = [0]
    select = [0]
    insertion = [0]
    merge = [0]
    figure, axes = plt.subplots(1, 1)
    axes.plot(times, select, color="pink", label="select_sort")
    axes.plot(times, insertion, color="green", label="insertion_sort")
    axes.plot(times, merge, color="blue", label="merge_sort")
    plt.rcParams["figure.autolayout"] = True
    plt.legend("upper left")

    def init():
        pass

    def func(frame):
        """
        Replicate the figure with a animation
        """
        table = execution_time_gathering.take_execution_time(1000, 2500 + frame * 50, 500, 5)
        for row in table:
            print(row)
        times.append(500 + frame * 50)
        select.append(row[0])
        insertion.append(row[1])
        merge.append(row[2])
        axes.plot(times, select, color="pink", label="select_sort")
        axes.plot(times, insertion, color="green", label="insertion_sort")
        axes.plot(times, merge, color="blue", label="merge_sort")

    animation = FuncAnimation(figure, func, repeat=True, init_func=init)
    plt.show()


if __name__ == "__main__":
    main()
