# AQA-Population-Model
Computer Science GCSE Coursework

# The Population Model Rules
1. The population consists only of females

2. At any one time there are three types of individual in the population:
  - Seniles (Old Greenfly that do not reproduce)
  - Adults (Greenfly that are reproducing)
  - Juviniles (Greenfly that are too young to reproduce)

3. The model lasts for a set number of new generations. At the end of each generation:
  - All surviving senile greenfly remain as seniles
  - All surviving adult greenfly change from adults to seniles
  - All surviving juvinile greenfly change from juviniles to adults

4. Each type of individual has a survival rate. The survival rate is used to calculate the number of individuals that survive at the end of each generation.

5. Adult greenfly have a birth rate. The birth rate is used to calculate the number of juviniles that adults produce each generation. This number can be a fraction, so a birth rate of 1.5 means that, on average, each adult produces 1.5 juviniles each generation.

6. Numbers of individuals in the model are measured in thousands

7. The following values must be set before the model is run:
  - The initial numbers (called Generation 0) of juviniles, adults and seniles
  - The birth rate and survival rates
  - The number of new generation over which the model runs. This must be between 5 and 25
