# Investigating Airplane Accidents

In this project, we'll look at a dataset of airplane accident statistics and analyze patters to see if there are any common threads.

We're going to work with a dataset of 77,282 avviation accidents that occured in the U.S. The data in our `AviationData.txt` file comes from the National Transportation Safety Board (NTSB), and can be downloaded [here](https://www.ntsb.gov/Pages/default.aspx).

## Reading in the Data


`file = open('AviationData.txt', 'r')
file_read = file.read()
aviation_data = reader.split('\n')
aviation_list = []
for line in aviation_data:
aviation_list.append(line.split('|'))
lax_code = []
for item in aviation_list:
if 'LAX94LA336' in item:
lax_code.append(item)`
