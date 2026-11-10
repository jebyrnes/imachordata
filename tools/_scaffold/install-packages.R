# R packages used by the posts that run R code (the five 2020-2025 R posts).
# Run once:  source("install-packages.R")
cran <- c(
  "knitr", "rmarkdown", "remotes",
  "dplyr", "tidyr", "purrr", "readr", "ggplot2", "patchwork", "ggrepel", "geofacet",
  "palmerpenguins", "arm", "DHARMa", "bayesplot", "rstanarm", "mgcv", "modelr", "broom",
  "kableExtra", "htmltools",
  "insight", "performance", "see", "modelbased"
)
missing <- setdiff(cran, rownames(installed.packages()))
if (length(missing)) install.packages(missing)

# not on CRAN
github <- c("christophergandrud/coreSim", "Covid19R/covid19R", "Covid19R/covid19mobility")
remotes::install_github(github, upgrade = "never")
