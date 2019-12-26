# AQA-Population-Model
Computer Science GCSE Coursework

# About the model
When studying the environment, scientists sometimes look at how population sizes of animals and plants change overtime. The scientists can use this information to find out which species are in danger of becoming extinct, to predict the effect of introducing a foreign species of animal into the countryside or to discover the effect of a pollutant.

Studying populations of animals and plants in the wild can take a very long time, so scientists use computer models to help them in their studies.

This population model has been made to investigate how a greenfly population changes. Greenflies are a common insect that are considered to be a pest by gardeners because they damage roses and other garden plants.

The life cycle of greenfly is complex and the model will only deal with some aspects of the greenfly life cycle. In the summer, the population consists only of females and each female gives birth to only females.

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
