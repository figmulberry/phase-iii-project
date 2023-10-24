# Phase III Project: A Classification Model to Smartly Predict Which Waterpoints Need Maintenance in Tanzania

## Introduction

This repository contains all the information (data, presentation, and other materials) for the Phase III Project. In this project, a classification model is utilized to predict which water pumps will need maintenance to ensure that clean, and potable water is available to communities across the United Republic of Tanzania.

## 1.0 Project Overview

This project investigates the data provided and produces a classification model that helps predict the water pumps that need maintenance.

## Business Problem Statement

Access to safe water, sanitation, and hygiene is a basic human need for good health and well-being. In this context, we are looking at access to safe water in three contexts: Globally, Global South, and in Tanzania. This will help us to lay a solid foundation for what we are about to do for the analysis.

To  address the water access issue in Tanzania, water pumps have been installed over time (since the 90s) to allow the residents to have access to potable water. However, some of these water pumps are not always functioning at 100%. Therefore, the non-functioning and those that are functioning but need repair water pumps need to be checked. Maintaining these water pumps can be challenging due to many factors such as their location in remote areas and many more thus making it difficult to monitor.

### 1.1 World Context

Water is an indispensable commodity for existence. The Sustainable Development [SDG  Goal 6: Clean Water and Sanitation](https://www.un.org/sustainabledevelopment/water-and-sanitation/) – calls for all countries to ensure access to safe water, sanitation, and hygiene which is the most basic human need for health and well-being.
With the rapidly increasing global population, water demand keeps on rising and it is predicted that billions of people will lack access to this basic commodity by 2030 unless progress is quadrupled.
According to the [World Research Institute’s]( https://www.wri.org/insights/highest-water-stressed-countries) [WRI’s Aqueduct Water Risk Atlas]( https://www.wri.org/aqueduct), 25 Countries, Housing One-quarter of the Population, Face Extremely High Water Stress.
A recently released [Global Water Security 2023 Assessment]( https://inweh.unu.edu/wp-content/uploads/2023/03/Global-Water-Security-Assessement-2023_F.pdf) by the United Nations University Institute for Water, Environment and Health finds that out of nearly 7.8 billion people in 186 countries, 5.2 billion (72%) are water insecure. That includes 1.3 billion Africans—Africa’s entire population.

### 1.2 Global South Context

The Global South continues to face a growing water crisis. The [Global Water Security – 2023 Assessment](https://www.un.org/africarenewal/magazine/april-2023/water-insecure-africa-gets-some-wins-un-water-conference) report indicates that the least water-secure regions are Africa, including the Sahel, the Horn of Africa, and parts of West Africa, in addition to South Asia, and Small Island Developing States (SIDS) across the world.”
Nevertheless, there are some ongoing and already implemented water generation programs in the region, but many countries continue to face poor progress in water and sanitation hygiene [WASH]. As reported by the UN’s African Renewal magazine in April 2023, [18 countries made progress reducing WASH-related deaths]( https://shorturl.at/jvyV2). Among the 18 countries that have made progress are Burundi, Ethiopia, Kenya, Uganda, and Tanzania.

### 1.3 Tanzania Context

Tanzania, formally – the United Republic of Tanzania, faces a water crisis. As per [Water.org]( https://water.org/our-impact/where-we-work/tanzania/), out of Tanzania’s population of 59 million people, 16 million people (28% of the population) lack access to safe water, and 44 million people (73%) lack access to safely managed household sanitation facilities. The natural freshwater sources such as rivers and streams, lakes, dams, and groundwater are unevenly distributed. The surface and groundwater face a major challenge since the drainage system is poorly maintained or constructed which leaks into the water system thus contaminating the water. The water supply is also wasted through leaks only servicing a small percentage of the population.
The main group affected by these challenges are mainly the women and young school-going girls who travel long distances to collect water. This, in return, causes a decrease in sustainability in future generations in Tanzania thus resulting in the furtherance of the water crisis.
![Water Pumps in Tanzania](https://github.com/figmulberry/phase-iii-project/blob/main/images/Tanzania%20Water%20Pumps%20Distribution.png)

## Business Understanding

Our goal in this project is to ``predict the operating condition of a waterpoint`` for each record in the dataset. 

Many studies have shown that the primary causes of water pumps failures are:

1.	Shortage of skilled labor for maintenance.
2.	Poor quality of material used in water pumps construction.
3.	Inaccurate placement of groundwater extraction boreholes.

With the completion of this project, we shall manage to note the major causes of water pumps malfunctioning and therefore help to document them for the proper future address of such issues.


### Main Objective

The main objective of this project is to build a Model that will help us to predict by understanding the maintenance requirements of the water pumps that need repair so that they can continue supplying water to the residents of Tanzania. 
The Model will greatly help to inform the management of the water pumps on where the technicians need to be dispatched for repairs. The result of this is that the allocation of resources will be optimized to ensure an increase in the population’s access to safe water across Tanzania.

### Research Question:

How possible is it to predict whether a water pump is either functional, functional but in need of maintenance, or non-functional given the data for this analysis?

#### 3.1 Specific Objectives

1. To smartly predict the functional state of Tanzanian water pumps.
2. To establish what impact data cleaning has on the overall success of our model
3. Identify the feature importance in our data for analysis

#### 3.2 Success Criteria

This project will be deemed successful if it achieves a high prediction percentage (%) of all the water pumps that need repair of some way so that they can continue to supply the residents across Tanzania with safe water.

### The Data

The data used in this analysis comes from [Taarifa](http://taarifa.org/) and the [Tanzanian Ministry of Water](http://maji.go.tz/). The task is to predict ``which pumps are functional``, ``which need some repairs``, and ``which don't work at all``. We shall seek to predict one of these *three classes* based on a number of variables about *what kind of pump is operating*, *when it was installed*, and *how it is managed*. 
A smart understanding of which water points will fail will in return help us to improve maintenance operations and ensure that clean, potable water is available to communities across Tanzania.

We are provided with the following set of information about the water points:

## Methodology

This included the following:

1. **Data Exploration**: For each water pump we were provided with 39 attributes (excluding a unique record identifier) that could potentially be used as predictor variables. The response variable can assume one of three possible values:

- ``functional``: The pump is operational and not in need of maintenance
- ``functional needs repair``: The pump is operational but is in need of repair
- ``non functional``: The pump is inoperable
- 
54.3% of all pumps in the data set were found to be functional, while 38.4% were non functional and 7.3% had a status of functional needs repair.
  
2. **Data Preparation**: As discussed above, more than 53% of the records in the data set contain either missing or invalid data values. Our data exploration efforts allowed us to uncover relationships between various independent variables that could serve as the basis of statistically valid imputation algorithms for the missing values of the ``amount_tsh``, ``gps_height``, ``construction_year``, ``latitude`` and ``longitude`` variables.
   
3. **Classification Modeling**: Seven types of classification models were constructed for the purposes of predicting the current status of a given water pump:
   
   - Baseline Decision Tree
   - Second Decision Tree
   - Baseline Random Forest Classifier
   - Baseline Gradient Boost
   - XGBoost Classifier
   - Random Forest Classifier-Grid Search
   - XGBoost Classifier-Grid Search
   - Final Model-Random Forest Classifier
     
4. **Model Selection**: 

We ended up choosing the Random Forest Classifier and tuned it for prediction of the water pump status.
The confusion matrix for the model is represented as follows:
|    |   0  | 1   |   2  |
|----|------|-----|------|
|  0 | 5497 | 426 |  583 |
|  1 |  342 | 373 |   98 |
|  2 |  880 | 125 | 3556 |

## Conclusions

Our final classification model achieved an accuracy score of 0.7941, corresponding to approximately 79.41%. This means that the model accurately predicts the water pump functionality status 79.41% of the time. 

Furthermore, our analysis identified several important features that strongly influence the model's predictions. These key features include `permit`, `public_meeting`, `district_code`, `region_code`, `water_type`, and `source_class`. The stakeholders, such as the government of the United Republic of Tanzania, can utilize these findings to enhance their maintenance and repair operations for water pumps in the various locations where there are non funcitonal water pumps.

By considering these critical features, stakeholders can make informed decisions and take proactive measures to ensure efficient functionality of the water pump systems.

## Recommendations

1. When gathering the data, it is important to use, among other reliable instruments, high-precision GPs. This would help the technical team visiting the water pump have an easy time getting their way around.
2. Data cleaning and verification while in the field would be crucial to ensure that valid results are taken back to the office for analysis.
3. The government or the responsible agencies (e.g., the Ministry of Water) should put up a task force that ensures periodic data update to stay up-to-date with the requirements of all the water pumps and the type of care they need.
4. The data collection should be focused more on the nonfunctional water pumps.
5. A research to understand what mainly caused breakage.

### Study Limitations

1. The data had a lot of gaps that were either not filled or got filled but in a very general way.
2. For such a dataset, there was a high number (about 3%) of water pumps that had not been mapped in Tanzania. This brought a challenge in determining where they were spatially supposed to be located. If these results are to be relied upon, such water pumps are supposed to be accurately located.

### Future Research

Since this analysis only focused on the water pumps from the United Republic of Tanzania, specifically using the data from the [DriventData.org](https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/data/) site. If this can be extended to other countries of the region and have a more reusable model in their context.

### References

1. [DrivenData.org](https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/data/)
2. [Taarifa](http://taarifa.org/)
3. [Tanzanian Ministry of Water](http://maji.go.tz/)
4. [World Research Institute]( https://www.wri.org/insights/highest-water-stressed-countries)
5. [UN.org - SDG  Goal 6: Clean Water and Sanitation](https://www.un.org/sustainabledevelopment/water-and-sanitation/)
6. [Water.org]( https://water.org/our-impact/where-we-work/tanzania/)
7. [Africa Renewal Magazine](https://www.un.org/africarenewal/magazine/april-2023/water-insecure-africa-gets-some-wins-un-water-conference#:~:text=18%20countries%20made%20progress%20reducing%20WASH%2Drelated%20deaths)
