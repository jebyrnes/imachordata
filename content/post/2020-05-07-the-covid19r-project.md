---
title: The Covid19R Project
author: Jarrett Byrnes
date: '2020-05-07'
slug: the-covid19r-project
categories:
  - R
  - covid19R
tags: []
---
<script src="/rmarkdown-libs/kePrint/kePrint.js"></script>
<link href="/rmarkdown-libs/lightable/lightable.css" rel="stylesheet" />
<script src="/rmarkdown-libs/kePrint/kePrint.js"></script>
<link href="/rmarkdown-libs/lightable/lightable.css" rel="stylesheet" />

We want our coronavirus data! We want it now! We want it TIDY!  

tl;dr Go check out the [Covid19R project](https://covid19r.github.io/covid19R/) and it's [documentation](https://covid19r.github.io/documentation/) - a way for many people to bring their unique data harvesting efforts of Covid-19 data into a single tidy data format, and then be redistributed through a single low-dependency package, [covid19R](https://covid19r.github.io/covid19R/). It's all one big work-in-progress, but check it out!  
  
## OK, the story!  
  
Back in February (remember February), while teaching [data science](http://biol355.github.io), I was trying to think of ways to spice up the class with more relevant data. We were in the midst of data tidying, when I saw a tweet from [Rami Krispin](https://twitter.com/Rami_Krispin/) about starting a Covid R data package (whose account as of 2022-11-27 is suspended?)

<!-- #`htmltools::HTML("{{< tweet 1227613923462877188 >}}")` -->

Cool! A coronavirus data package. I went on to make a neat [data tidying lab](https://biol355.github.io/Labs/coronavirus.html) - well, I think it's neat - as well as weaving the data into other parts of the course. I also made a few pull requests on the repo to add features....as did [Amanda Dobbyn](https://twitter.com/dobbleobble). Rami contacted both of us, and thus a collaboration was born!

## Tidy Covid-19 Data

We had been pulling from many different data sources, and found lots of difficulty in bringing them together. I had used [rnaturalearth](https://docs.ropensci.org/rnaturalearth/) to get at unique place identifiers, but the proliferation of data sets and data aggregation efforts was bewildering. How to get a handle on the wide variety of data types, spatial location types, and more?

So, we began designing a very simple long format data specification and agreed to make our data packages create data in that format. I wrote up a package to harvest the updated [New York Times data](https://covid19r.github.io/covid19nytimes/) as an example.

<table class="table table-striped table-bordered table-condensed" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;"> date </th>
   <th style="text-align:left;"> location </th>
   <th style="text-align:left;"> location_type </th>
   <th style="text-align:left;"> location_code </th>
   <th style="text-align:left;"> location_code_type </th>
   <th style="text-align:left;"> data_type </th>
   <th style="text-align:right;"> value </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> 2021-01-23 </td>
   <td style="text-align:left;"> Alabama </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> 01 </td>
   <td style="text-align:left;"> fips_code </td>
   <td style="text-align:left;"> cases_total </td>
   <td style="text-align:right;"> 439442 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 2021-01-23 </td>
   <td style="text-align:left;"> Alabama </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> 01 </td>
   <td style="text-align:left;"> fips_code </td>
   <td style="text-align:left;"> deaths_total </td>
   <td style="text-align:right;"> 6657 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 2021-01-23 </td>
   <td style="text-align:left;"> Alaska </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> 02 </td>
   <td style="text-align:left;"> fips_code </td>
   <td style="text-align:left;"> cases_total </td>
   <td style="text-align:right;"> 52820 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 2021-01-23 </td>
   <td style="text-align:left;"> Alaska </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> 02 </td>
   <td style="text-align:left;"> fips_code </td>
   <td style="text-align:left;"> deaths_total </td>
   <td style="text-align:right;"> 250 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 2021-01-23 </td>
   <td style="text-align:left;"> Arizona </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> 04 </td>
   <td style="text-align:left;"> fips_code </td>
   <td style="text-align:left;"> cases_total </td>
   <td style="text-align:right;"> 717593 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> 2021-01-23 </td>
   <td style="text-align:left;"> Arizona </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> 04 </td>
   <td style="text-align:left;"> fips_code </td>
   <td style="text-align:left;"> deaths_total </td>
   <td style="text-align:right;"> 12170 </td>
  </tr>
</tbody>
</table>

## One Package to Rule Them All

This was good - but, how would people get data? 

We noticed that with nearly every different data set, we needed a different approach to data manipulation. If we threw all of our efforts into a single package, the dependency tree would rapidly spiral out of control. This seemed not good.

Many small packages, each specializing in unique data sets or collections of data sets seemed good, but.... how to make all of that searchable? Did we really want to make people have to install a bazillion different small packages? This seemed inefficient.  

So, we took a cue from the many excellent packages by the good folk at [ropensci](https://ropensci.org/) and created a master package - [covid19R](https://covid19r.github.io/covid19R/). This package wouldn't do anything, save redistribute data files. Moreover, so it didn't have to depend on all of those little packages, and thus have all of those same problems as above, we built a separate [covid19Rdata](https://github.com/Covid19R/covid19Rdata) package/repo that updates once daily to refresh all of the data from any package that is part of the project.

So, you can get the information about what data is part of this Tidy Covid-19 data project, choose a relevant data set, and grab it, all without racking having to download tons of packages, satisfy weird dependencies, or otherwise pull your hair out!

Here's what's part of the project at time of writing

<table class="table table-striped table-bordered table-condensed" style="margin-left: auto; margin-right: auto;">
 <thead>
  <tr>
   <th style="text-align:left;"> data_set_name </th>
   <th style="text-align:left;"> package_name </th>
   <th style="text-align:left;"> function_to_get_data </th>
   <th style="text-align:left;"> data_details </th>
   <th style="text-align:left;"> data_url </th>
   <th style="text-align:left;"> license_url </th>
   <th style="text-align:left;"> data_types </th>
   <th style="text-align:left;"> location_types </th>
   <th style="text-align:left;"> spatial_extent </th>
   <th style="text-align:left;"> has_geospatial_info </th>
   <th style="text-align:left;"> get_info_passing </th>
   <th style="text-align:left;"> refresh_status </th>
   <th style="text-align:left;"> last_refresh_update </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;"> covid19nytimes_states </td>
   <td style="text-align:left;"> covid19nytimes </td>
   <td style="text-align:left;"> refresh_covid19nytimes_states </td>
   <td style="text-align:left;"> Open Source data from the New York Times on distribution of confirmed Covid-19 cases and deaths in the US States. For more, see https://www.nytimes.com/article/coronavirus-county-data-us.html or the readme at https://github.com/nytimes/covid-19-data. </td>
   <td style="text-align:left;"> https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv </td>
   <td style="text-align:left;"> https://github.com/nytimes/covid-19-data/blob/master/LICENSE </td>
   <td style="text-align:left;"> cases_total, deaths_total </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> country </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 16:57:46 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> covid19nytimes_counties </td>
   <td style="text-align:left;"> covid19nytimes </td>
   <td style="text-align:left;"> refresh_covid19nytimes_counties </td>
   <td style="text-align:left;"> Open Source data from the New York Times on distribution of confirmed Covid-19 cases and deaths in the US by County. For more, see https://www.nytimes.com/article/coronavirus-county-data-us.html or the readme at https://github.com/nytimes/covid-19-data. </td>
   <td style="text-align:left;"> https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv </td>
   <td style="text-align:left;"> https://github.com/nytimes/covid-19-data/blob/master/LICENSE </td>
   <td style="text-align:left;"> cases_total, deaths_total </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> country </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 16:58:02 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> covid19france </td>
   <td style="text-align:left;"> covid19france </td>
   <td style="text-align:left;"> refresh_covid19france </td>
   <td style="text-align:left;"> Open Source data from opencovid19-fr on distribution of confirmed Covid-19 cases and deaths in the US States. For more, see https://github.com/opencovid19-fr/data. </td>
   <td style="text-align:left;"> https://raw.githubusercontent.com/opencovid19-fr/data/master/dist/chiffres-cles.csv </td>
   <td style="text-align:left;"> https://github.com/opencovid19-fr/data/blob/master/LICENSE </td>
   <td style="text-align:left;"> confirmed, dead, icu, hospitalized, recovered, discovered </td>
   <td style="text-align:left;"> county, region, country, overseas collectivity </td>
   <td style="text-align:left;"> country </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 16:58:07 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> CanadaC19_cases </td>
   <td style="text-align:left;"> CanadaC19 </td>
   <td style="text-align:left;"> refresh_CanadaC19_cases </td>
   <td style="text-align:left;"> Open Source data from multiple public reporting data throughout Canada. For more, see https://github.com/ishaberry/Covid19Canada. </td>
   <td style="text-align:left;"> https://raw.githubusercontent.com/ishaberry/Covid19Canada/master/cases.csv </td>
   <td style="text-align:left;"> https://github.com/debusklaneml/CanadaC19/blob/master/LICENSE </td>
   <td style="text-align:left;"> cases_new </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 16:58:17 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> covid19us </td>
   <td style="text-align:left;"> covid19us </td>
   <td style="text-align:left;"> refresh_covid19us </td>
   <td style="text-align:left;"> Open Source data from COVID Tracking Project on the distribution of Covid-19 cases and deaths in the US. For more, see https://github.com/opencovid19-fr/data. </td>
   <td style="text-align:left;"> https://covidtracking.com/api </td>
   <td style="text-align:left;"> https://github.com/aedobbyn/covid19us/blob/master/LICENSE.md </td>
   <td style="text-align:left;"> positive, negative, pending, total_test_results_source, total_test_results, hospitalized_currently, hospitalized_cumulative, in_icu_currently, in_icu_cumulative, on_ventilator_currently, on_ventilator_cumulative, recovered, death, hospitalized, total_tests_viral, positive_tests_viral, negative_tests_viral, positive_cases_viral, death_confirmed, death_probable, total_test_encounters_viral, total_tests_people_viral, total_tests_antibody, positive_tests_antibody, negative_tests_antibody, total_tests_people_antibody, positive_tests_people_antibody, negative_tests_people_antibody, total_tests_people_antigen, positive_tests_people_antigen, total_tests_antigen, positive_tests_antigen, positive_increase, negative_increase, total, total_test_results_increase, death_increase, hospitalized_increase, negative_regular_score, negative_score, positive_score </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> country </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 16:58:33 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> VirginiaC19 </td>
   <td style="text-align:left;"> VirginiaC19 </td>
   <td style="text-align:left;"> refresh_VirginiaC19 </td>
   <td style="text-align:left;"> Open Source data from Virginia Department of Health. For more information, see https://www.vdh.virginia.gov/coronavirus/. </td>
   <td style="text-align:left;"> https://www.vdh.virginia.gov/content/uploads/sites/182/2020/03/VDH-COVID-19-PublicUseDataset-Cases.csv </td>
   <td style="text-align:left;"> https://github.com/debusklaneml/VirginiaC19/blob/master/LICENSE </td>
   <td style="text-align:left;"> cases_new,deaths_new,hosp_new </td>
   <td style="text-align:left;"> county </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 16:58:33 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> covid19tunisia </td>
   <td style="text-align:left;"> covid19tunisia </td>
   <td style="text-align:left;"> refresh_covid19tunisia </td>
   <td style="text-align:left;"> Open Source data on distribution of confirmed Covid-19 cases, recovered ones and deaths in Tunisia.
    For more, https://github.com/MounaBelaid/covid19datatunisia </td>
   <td style="text-align:left;"> https://raw.githubusercontent.com/MounaBelaid/covid19datatunisia/master/dist/data.csv </td>
   <td style="text-align:left;"> https://github.com/MounaBelaid/covid19datatunisia/blob/master/LICENSE </td>
   <td style="text-align:left;"> cases_new, deaths_new, recovered_new </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> country </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 16:58:33 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> covid19mobility_apple_country </td>
   <td style="text-align:left;"> covid19mobility </td>
   <td style="text-align:left;"> refresh_covid19mobility_apple_country </td>
   <td style="text-align:left;"> Data reflects relative volume of directions requests compared to a baseline volume on January 13th, 2020 for multiple transportation modes aggregated at the country level. </td>
   <td style="text-align:left;"> https://www.apple.com/covid19/mobility </td>
   <td style="text-align:left;"> https://www.apple.com/covid19/mobility </td>
   <td style="text-align:left;"> driving, walking, transit </td>
   <td style="text-align:left;"> country </td>
   <td style="text-align:left;"> global </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 16:58:36 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> covid19mobility_apple_subregion </td>
   <td style="text-align:left;"> covid19mobility </td>
   <td style="text-align:left;"> refresh_covid19mobility_apple_subregion </td>
   <td style="text-align:left;"> Data reflects relative volume of directions requests compared to a baseline volume on January 13th, 2020 for multiple transportation modes aggregated at the subregion (state) level. </td>
   <td style="text-align:left;"> https://www.apple.com/covid19/mobility </td>
   <td style="text-align:left;"> https://www.apple.com/covid19/mobility </td>
   <td style="text-align:left;"> driving, walking, transit </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> global </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 16:58:59 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> covid19mobility_apple_city </td>
   <td style="text-align:left;"> covid19mobility </td>
   <td style="text-align:left;"> refresh_covid19mobility_apple_city </td>
   <td style="text-align:left;"> Data reflects relative volume of directions requests compared to a baseline volume on January 13th, 2020 for multiple transportation modes aggregated at the city level. </td>
   <td style="text-align:left;"> https://www.apple.com/covid19/mobility </td>
   <td style="text-align:left;"> https://www.apple.com/covid19/mobility </td>
   <td style="text-align:left;"> driving, walking, transit </td>
   <td style="text-align:left;"> city </td>
   <td style="text-align:left;"> global </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 16:59:11 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> covid19mobility_google_country </td>
   <td style="text-align:left;"> covid19mobility </td>
   <td style="text-align:left;"> refresh_covid19mobility_google_country </td>
   <td style="text-align:left;"> Changes for each day are compared to a baseline value for that day of the week as compared to  the 5-week period Jan 3-Feb 6, 2020 for visits to places falling in to certain categories. </td>
   <td style="text-align:left;"> https://www.google.com/covid19/mobility/ </td>
   <td style="text-align:left;"> https://www.google.com/covid19/mobility/ </td>
   <td style="text-align:left;"> retail_and_recreation_percent_change_from_baseline,grocery_and_pharmacy_percent_change_from_baseline,parks_percent_change_from_baseline,transit_stations_percent_change_from_baseline,workplaces_percent_change_from_baseline,residential_percent_change_from_baseline </td>
   <td style="text-align:left;"> country </td>
   <td style="text-align:left;"> global </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 16:59:31 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> covid19mobility_google_subregions </td>
   <td style="text-align:left;"> covid19mobility </td>
   <td style="text-align:left;"> refresh_covid19mobility_google_subregions </td>
   <td style="text-align:left;"> Changes for each day are compared to a baseline value for that day of the week as compared to  the 5-week period Jan 3-Feb 6, 2020 for visits to places falling in to certain categories. Data is aggregated at the state or subdivision level. </td>
   <td style="text-align:left;"> https://www.google.com/covid19/mobility/ </td>
   <td style="text-align:left;"> https://www.google.com/covid19/mobility/ </td>
   <td style="text-align:left;"> retail_and_recreation_percent_change_from_baseline,grocery_and_pharmacy_percent_change_from_baseline,parks_percent_change_from_baseline,transit_stations_percent_change_from_baseline,workplaces_percent_change_from_baseline,residential_percent_change_from_baseline </td>
   <td style="text-align:left;"> state </td>
   <td style="text-align:left;"> global </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 17:00:12 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> covid19mobility_google_us_counties </td>
   <td style="text-align:left;"> covid19mobility </td>
   <td style="text-align:left;"> refresh_covid19mobility_google_us_counties </td>
   <td style="text-align:left;"> Changes for each day are compared to a baseline value for that day of the week as compared to  the 5-week period Jan 3-Feb 6, 2020 for visits to places falling in to certain categories. Data is aggregated at the county level for the USA only. </td>
   <td style="text-align:left;"> https://www.google.com/covid19/mobility/ </td>
   <td style="text-align:left;"> https://www.google.com/covid19/mobility/ </td>
   <td style="text-align:left;"> retail_and_recreation_percent_change_from_baseline,grocery_and_pharmacy_percent_change_from_baseline,parks_percent_change_from_baseline,transit_stations_percent_change_from_baseline,workplaces_percent_change_from_baseline,residential_percent_change_from_baseline </td>
   <td style="text-align:left;"> county </td>
   <td style="text-align:left;"> country </td>
   <td style="text-align:left;"> FALSE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 17:02:45 </td>
  </tr>
  <tr>
   <td style="text-align:left;"> coronavirus_jhu </td>
   <td style="text-align:left;"> coronavirus </td>
   <td style="text-align:left;"> refresh_coronavirus_jhu* </td>
   <td style="text-align:left;"> The 2019 Novel Coronavirus COVID-19 (2019-nCoV) Dataset from the Johns Hopkins University Center for Systems Science and Engineering </td>
   <td style="text-align:left;"> https://systems.jhu.edu/research/public-health/ncov/ </td>
   <td style="text-align:left;"> https://github.com/CSSEGISandData/COVID-19/ </td>
   <td style="text-align:left;"> cases_new, recovered_new, deaths_new </td>
   <td style="text-align:left;"> country, state </td>
   <td style="text-align:left;"> global </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> TRUE </td>
   <td style="text-align:left;"> Passed </td>
   <td style="text-align:left;"> 2021-01-24 17:02:48 </td>
  </tr>
</tbody>
</table>

## What is a Covid19R Project Package?

We have a few requirements for a package to be added to our project. First, [file an issue](https://github.com/Covid19R/covid19R/issues) that you're creating one! Then, take a gander at our [documentation on building packages](https://covid19r.github.io/documentation/building-a-new-data-package.html). We've provided a [template](https://github.com/Covid19R/covid19_package_template) for you to use, if you're new to package building.

We then ask that you provide at least [two functions in your package](https://covid19r.github.io/documentation/standardized-package-functions.html) - a `get_info_*()` function, where * is the package name, that supplies standard information that we chonk into the table y'all see above. And for each data set a `refresh_*()` function, where * is the data set name, that pulls in tasty fresh data and reformats it into our [tidy Covid-19 data standard](https://covid19r.github.io/documentation/data-format-standard.html) using an ever-expanding [standardized vocabulary](https://covid19r.github.io/documentation/standardized-vocabulary.html) - and you can file issues to keep expanding it.

## Our request to the community

We'd love this to become a much larger community - have existing Covid-19 data package developers implement our two simple functions so we can add their data to the project, provide support for people interested in creating data distribution packages - maybe their first package ever - to use our format so that data is good and tidy. We're very interested in conversation - [start one up here](https://github.com/Covid19R/covid19R/issues) for the moment!

## Our Hope

What we hope is that, with many datasets going in using common best practices, we'll be able to facilitate discovery. Data cleaning and joining is sometimes 80-90% of the effort of any data science project. With a standard format, a standardized vocabulary, and the usage of standard geospatial codes, we hope to seriously reduce that time in order to speed up other work.

Won't you join us?
