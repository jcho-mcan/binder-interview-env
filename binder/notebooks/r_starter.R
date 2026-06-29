library(tidyverse)

df <- tibble(
  x = rnorm(100),
  y = rnorm(100)
)

ggplot(df, aes(x, y)) +
  geom_point()
