file = open('AviationData.txt', 'r')
file_read = file.read()
aviation_data = reader.split('\n')

aviation_list = []
for line in aviation_data:
    aviation_list.append(line.split('|'))

lax_code = []
for item in aviation_list:
    if 'LAX94LA336' in item:
        lax_code.append(item)
