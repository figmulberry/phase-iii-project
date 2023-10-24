# Data Dictionary

This file gives the documentation about the dataset used for our prediction and the problem we are trying to solve.

The [data folder](https://github.com/figmulberry/phase-iii-project/tree/main/data) contains all the data used in this project. The files included are `` Training set values`` - the dataset containing the characteristics of each water pump, and `` Training set labels`` - the functionality status of each water pump.

### Data Features and Explanation

The dataset was obtained from the [Driven Data site](https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/data/) and has been attributed to the [Taarifa](http://taarifa.org/) which aggregates the data from the [Tanzanian Ministry of Water](http://maji.go.tz/).
The dataset supplied contains 59,400 records and 40 features (where 30 are categorical, 8 are numerical and the remaining 2 are date features).

The table below gives the information on the features that are contained in the dataset:

| Data Column                                           | Explanation          |
| --------------------------------------------------------- | -------------- |
| ``amount_tsh`` |Total static head (amount water available to waterpoint)|
| ``date_recorded`` |The date the row was entered|
| ``funder`` | Who funded the well |
| ``gps_height`` | Altitude of the well |
| ``installer`` | Organization that installed the well |
| ``longitude`` | GPS coordinate |
| ``latitude`` | GPS coordinate |
| ``wpt_name`` | Name of the waterpoint if there is one |
| ``num_private`` |  |
| ``basin`` | Geographic water basin |
| ``subvillage`` | Geographic location |
| ``region`` | Geographic location|
| ``region_code`` | Geographic location (coded) |
| ``district_code`` | Geographic location (coded)
| ``lga`` | Geographic location |
| ``ward`` | Geographic location |
| ``population`` | Population around the well |
| ``public_meeting`` | True/False |
| ``recorded_by`` | Group entering this row of data |
| ``scheme_management`` | Who operates the waterpoint |
| ``scheme_name`` | Who operates the waterpoint |
| ``permit`` | If the waterpoint is permitted |
| ``construction_year`` | Year the waterpoint was constructed |
| ``extraction_type`` | The kind of extraction the Waterpoint uses |
| ``extraction_type_group`` | The kind of extraction the Waterpoint uses |
| ``extraction_type_class`` | The kind of extraction the Waterpoint uses |
| ``management`` | How the waterpoint is managed |
| ``management_group`` | How the waterpoint is managed |
| ``payment`` | What the water costs |
| ``payment_type`` | What the water costs |
| ``water_quality`` | The quality of the water |
| ``quality_group`` | The quality of the water |
| ``quantity`` | The quantity of water |
| ``quantity_group`` | The quantity of water |
| ``source`` | The source of the water |
| ``source_type`` | The source of the water |
| ``waterpoint_type`` | The kind of waterpoint |
| ``waterpoint_type_group`` | The kind of waterpoint |

### Labels

The labels in this dataset have three possible values:

| Waterpoint Status                                         | Description         |
| --------------------------------------------------------- | -------------- |
| ``functional`` |The waterpoint is operational and there are no repairs needed|
| ``functional needs repair`` |The waterpoint is operational, but needs repairs|
| ``non-functional`` |The waterpoint is not operational|
