# An Agent-Based Model of ants' recruitment strategies compared to their colony size

This repo holds the codebase for ['An Agent-Based Model of ants' recruitment strategies compared to their colony size' paper](TODO).
The idea for this project came from the paper by [Planqué et al.](https://www.ncbi.nlm.nih
.gov/pmc/articles/PMC2915909/pdf/pone
.0011664.pdf) on Recruitment Strategies and Colony Size in Ants.
This project was conducted for the course Agent-Based Modelling by Michael Lees and Debraj Roy, University of Amsterdam.

While writing this codebase, contributions where made to the [Mesa](https://github.com/projectmesa/mesa) ABM framework:
- [[Feature Implemented] Multiprocessing BatchRunner](https://github.com/projectmesa/mesa/pull/456)
- [[Bugfix] iter_neighborhood() now gives correct neighborhoods for both von Neumann and Moore](https://github.com/projectmesa/mesa/pull/459)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Prerequisite libraries, frameworks, and modules can be installed through:

```
pip install -r requirements.txt
```

This will install the correct versions of:
- matplotlib (2.0.2)
- numpy (1.12.1)
- tqdm (4.19.5)
- pandas (0.20.3)
- pathos (0.2.1)
- Mesa (0.8.2)
- SALib (1.1.3)

### Repository
The following list describes the most important files in the project and where to find them:
- **/Code**: contains all of the codebase of this project.
  - **/Code/ant.py**: contains the Ant class that implements the ant's properties and updates.
  - **/Code/batchrunner.py**: an adapted version of the [mesa batchrunner](https://github.com/projectmesa/mesa/blob/master/mesa/batchrunner.py). Adds multiprocessing, adds the ability to specify your own parameter windows, and fixes [a bug](https://github.com/projectmesa/mesa/issues/454) where the model will immediately reach max_steps after one run of a parameter combination.
  - **/Code/model.py**: contains the Environment class that implements the Environment's properties and updates.
  - **/Code/parameter_sweep.py**: does a parameter sweep with the values set in the file.
  - **/Code/plot.py**: contains functions that show either animations for real-time viewing of the environment, or plots that show specific passed values.
  - **/Code/roles.py**: contains the role modules. These objects can be used to specify roles for agents.
- **/Data**: contains csv's generated by the code.
- **/Results**: contains mainly images generated by the code.

The /Code folder also includes some iPython notebooks that explain the code and show how to perform analysis methods
 on the data that is generated:
- **/Code/examples.ipynb**: notebook that shows how to use the model, view the model, and create plots.
- **/Code/lda.ipynb**: shows how to perform LDA.
- **/Code/ofat.ipynb**: shows how to perform One Factor At a Time (OFAT) analysis.
- **/Code/sobol.ipynb**: shows how to perform a Sobol sensitivity analysis.

### Examples
To create an environment, simply do the following:
```
from model import Environment

env = Environment()
```
This creates an environment with all the default values. The values that can be set are:
- N (int): number of ants
- g (float): the max group size of an Ant relative to N
- size(int): the size of the system (size * size)
- p_uf (float): the probability that Unassigned changes to Follower
- p_pu (float): the probability that Pheromone changes to Unassigned
- p_up (float): the probability that Unassigned changes to Pheromone
- p_fl (float): the probability that Follower changes to Leader
- p_lu (float): the probability that Leader changes to Unassigned
- ratio (float): the start ratio of leaders (1 - ratio is the start nr of pheromone)
- moore (bool): True/False whether Moore/von Neumann is used
- grow (bool): True/False whether the system grows over time or not

It is now possible to progress the environment (one hundred timesteps), by executing the following:
```
for _ in range(100):
    env.step()
```
To visualise the steps, one can use the plot module:
```
from model import Environment
from plot import plot_continuous

steps = 100
env = Environment()

plot_continuous(env, steps)
```

For an interactive version of this example, see [example.ipynb](https://github.com/WouterVrielink/recruitment_strategies_ABM/blob/master/Code/examples.ipynb).

For examples on how to do [Linear Discriminant Analysis (LDA)](https://github.com/WouterVrielink/recruitment_strategies_ABM/blob/master/Code/lda.ipynb), [Sobel](https://github.com/WouterVrielink/recruitment_strategies_ABM/blob/master/Code/sobol.ipynb), and [One Factor At the Time (OFAT)](https://github.com/WouterVrielink/recruitment_strategies_ABM/blob/master/Code/ofat.ipynb), take a look at the respective ipython notebooks.

## Built With

* [Mesa](https://github.com/projectmesa/mesa) - ABM framework
* [SALib](https://github.com/SALib/SALib) - Library for Sensitivity Analysis methods
* [Matplotlib](https://matplotlib.org/) - A Python 2D plotting library

## Contributing

Please read [CONTRIBUTING.md](https://github.com/WouterVrielink/recruitment_strategies_ABM/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **W. Klijnsma** - *Initial work*
* **F. van Overeem** - *Initial work*
* **M. van der Sande** - *Initial work*
* **T. van der Veen** - *Initial work*
* **W. Vrielink** - *Initial work*

See also the list of [contributors](https://github.com/WouterVrielink/recruitment_strategies_ABM/graphs/contributors) who participated in this project.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](https://github.com/WouterVrielink/recruitment_strategies_ABM/LICENSE.md) file for details

## Acknowledgments

* [Mesa](https://github.com/projectmesa/mesa)
* [Michael Lees](https://mhlees.com/)
* [Debraj Roy](http://www.uva.nl/profiel/r/o/d.roy/d.roy.html)
