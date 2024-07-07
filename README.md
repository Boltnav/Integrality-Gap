This is sort of a 2-part repo. 

1. Sweep Line using Bentley Ottman algorithm. Time complexity - O(nlogn + k). 'k' will be the number of intersection points / cells formed by the rectangles. Not sure how often this would go to O(n^2), on the basis of this specific use case.
    Reference for the 2D board of rectangles and how the cells would be labelled-
   ![Screenshot 2024-07-05 151215](https://github.com/Boltnav/Integrality-Gap/assets/119060148/458d94bf-692e-470d-80b0-d576d3ce3f98)

2. Using a CPLEX solve (on Python). 
   Two problems: - Integer Linear program
                 - Linear program

   
