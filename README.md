# Examining the correlation between mutation intensity and fitness values of population

- The work's ***goal*** was to check what effects different values of this single mutation parameter have on the efficiency of evolution. In other words, how different values of mutation intensity reflect on the fitness of a population.

Note: Vertical position was chosen as the optimization criterion.

- The initial ***prediction*** of the result of conducting such an experiment was as follows:

The mutation intensity was indeed found to be significantly affecting the final results (i.e., overall fitness values and how they change with increase of the amount of evaluated individuals). The assumption was in favor of low intensity providing better outcome since higher mutation intensity might distribute more of the "bad" or "low-fitness" individuals by replacing too large fraction of genes randomly and becoming random search.

- The program was run using following command: 

```
for %%M in (0,005,010,020,030,040,050) do (
    python FramsticksEvolution.py -path %DIR_WITH_FRAMS_LIBRARY% -sim eval-allcriteria.sim;deterministic.sim;sample-period-2.sim;f9-mut-%%M.sim -opt vertpos -max_numparts 30 -max_numgenochars 50 -initialgenotype /*9*/BLU -popsize 50 -generations 1000 -tournament 10 -hof_size 1 >"C:\PATH\TO\FOLDER\final-results-%%M.txt"
)
```

where the used ***parameters*** can be found, i.e.:

  - generations 1000
  - popsize 50
  - tournament 10 - *(20% of popsize)*

# Results

<img src="https://github.com/allsuitablenamesarealreadytaken/evolution-and-mutation-intensity/blob/main/plots/plot%20all%20mutation%20intensities%20together.png" width="750" height="500">

## Interpretation:

- From the plot above, it can be seen that even low mutation intensity values (i.e., 5%, 10%) lead to better results than the absense of mutation at all (i.e., 0%).

- From the fact that the intensity of 5% provides generally better results than 10%, it can be concluded that in our case the fitness landscape is rather smooth, therefore, it does not require that high mutation intensity to prevent the algorithm from converging to local optima (since there is not that many of ragged solutions).

- Whereas, in opposite, with the further increase of matutation intensity value fitness values gradually decrease (i.e., 20%-50% with the step = 10), which happens due to its tendency of becoming too random or even "random" searched.

- Which leads to the conclusion that high mutation intensities may be found usefull in cases of ragged solution space to avoid stucking in local optima.

### To sum up:

- The predictions turned out to be true, apart from the 5% mutation intensity results providing better solutions than 10% ones.

#### P.S.: 

- Separate plots can be found here: [Plots](https://github.com/allsuitablenamesarealreadytaken/evolution-and-mutation-intensity/blob/main/plots/)
- Code for plotting the results can be found here: [Code To Plot](https://github.com/allsuitablenamesarealreadytaken/evolution-and-mutation-intensity/blob/main/plotResults.py)
