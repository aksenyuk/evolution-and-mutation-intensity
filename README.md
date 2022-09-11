# Examining the correlation between mutation intensity and fitness values of population

- The work's ***goal*** was to check what effects different values of this single mutation parameter have on the efficiency of evolution. In other words, how different values of mutation intensity reflect on the fitness of a population.

Note: Vertical position was chosen as the optimization criterion.

- The initial ***prediction*** of the result of conducting such an experiment was as follows:

The mutation intensity was indeed found to be significantly affecting the final results (i.e., overall fitness values and how they change with increase of the amount of evaluated individuals). The assumption was in favor of low intensity providing better outcome since higher mutation intensity might distribute more of the "bad" or "low-fitness" individuals by replacing too large fraction of genes randomly.

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

### Further observations can be found here: [Plots interpretation](https://github.com/allsuitablenamesarealreadytaken/evolution-and-mutation-intensity/blob/main/plots/README.md)
