for %%M in (0, 005, 010,020,030,040,050) do (
    for /L %%N in (1,1,200) do (
        python FramsticksEvolution.py -path %DIR_WITH_FRAMS_LIBRARY%  -sim eval-allcriteria.sim;deterministic.sim;sample-period-2.sim;f9-mut-%%M.sim  -opt vertpos -max_numparts 30 -max_numgenochars 50 -initialgenotype /*9*/BLU   -popsize 50    -generations %%N -hof_size 1 -hof_savefile results.txt -save_results %%M
    ))
