# AutoGraph
# Purpose
Automatically graph airline data, in particular incoming arrivals, one month at a time. See example.png in this repo for a demo of what the output looks like.

# Inputs
* csv file path location
* output name ("x.png")

# Outputs
* graph ("x.png")

# Technologies
* Python
* Seaborn (and MatPlotLib)
* Pandas

# Manual data wrangling process
1. go here: https://www.harryreidairport.com/Business/Finance/FlightActivityReports
2. click on the current year flight report link
3. download excel spread for current month
4. go to arriving seats by day+hour
5. copy paste the top section, which is the combined total, to a new spreadsheet
6. delete 2nd row that says total in it
7. to transpose, do the following:

* Select the cell range that you want to transpose.
* Choose Edit - Cut.
* Click the cell that is to be the top left cell in the result.
* Choose Edit - Paste Special.
* In the dialog, mark Paste all and Transpose.
* If you now click OK the columns and rows are transposed.
* Make sure that the numbers are only numbers, with no commas.

8. Type date in the top left corner, lowercase only 
9. save as a text csv
10. open AutoGraph code, and edit the read_csv line with the proper csv you just created, along with your desired name (last line, "myname.png")
11. run the AutoGraph

# Possible Additions
* Automate the data wrangling. Should only take 1 input, which is the target website for excel source. (might not even need that if dynamic url is predictable)
* Create text prompt upon running, that asks for a name of the output file, or dynamically creates the name based on the month

