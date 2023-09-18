# AHP_Industrial_Eng.

Under Operations Management in Mechanical and Industrial Engineering, there exist many decions making methods that aid management to make the best decision out of many alternatives. It is a structured decision-making framework and a mathematical method used to solve complex problems involving multiple criteria or attributes.

AHP was developed by Thomas L. Saaty in the 1970s and is widely used in various fields, including business, engineering, environmental science, and social sciences.

The AHP code is written in python, and it is capable of carryout the AHP algorith by inputing the pairwise comparison matrix of the criteria and the parwise comparison matrices of alternatives, under each criteria. These are the only input the user is requied to feed into the code. The rest of the AHP analysis, including consistency checks, ranking of alternatives and selecting the best alternative, is all done by the written program.

Pre-requisite for using this AHP code is having knowledge of:
* the number of criteria and alternatives: It is not adviceable to have less than 3 criteria and/or alternatives and hence, the code is designed to handle 3 or more criteria and/or alternatives. Note also that, the higher the number of criteria and alternatives, the more difficult it is to achieve consistency. Hence, do not perform AHP ananlysis over more then 10 criteria and/or alternatives. The code is limited to 10 criteria or alternatives (you might get an error when you use more than 10).
* the pairwise comparison matrix: The user must perform/construct the pairwise comparison matrix himself. The following could be used as a guide:
  _________________________________________________________________
  | Compared to the first alternative,    |                       |
  | the seocond alternative is:           |    Numerical Rating   |
  |_______________________________________|_______________________|
  |  extremely prefferred                 |        9              |
  |  very very strongly preferred         |        8              |
  |  very strongly preferred              |        7              |
  |  strongly preferred                   |        5              |
  |  very moderately preferred            |        4              |
  |  moderately preferred                 |        3              |
  |  equally preferred                    |        1              |
  _________________________________________________________________

  - Note that, alternative A, compared to itself is always equally prefered (thus the value 1).
  - If Alternative A, compared to alternative B is moderatelly preferred (thus a value of 3), then Alternative B, compared to alternative A on the peacewise comparison matrix will be the reciprocal of the value ( thus, 1/3). This how a pairwise comparison matrix is contructed.
 
    An example of pairwise comparison matrix
         A    B    C    D
    A    1    3    5    1/4
    B    1/3  1    1/5  2
    C    1/5  5    1    7
    D    4    1/2  1/7  1

    Pairwise comparison matrix for criteria and alternatives may look like that matrix above, and will always     be a square matrix. A, B, C and D could be the comparing criteria or the comparing alternatives under         each criteria.
