def gen_diff(data_a, data_b):
	data_a = dict(sorted(data_a.items()))
 	data_b = dict(sorted(data_b.items()))
	diff = []
	for key in data_a.keys():
    	if key in data_b:
        	if data_a[key] == data_b[key]:
            	diff.append('  ' + key + ' : ' + str(data_a[key]))
        	else:
            	diff.append('- ' + key + ' : ' + str(data_a[key]))
            	diff.append('+ ' + key + ' : ' + str(data_b[key]))
    	else:
        	diff.append('- ' + key + ' : ' + str(data_a[key]))
	for key in data_b.keys():
    	if key not in data_a:
        	diff.append('+ ' + key + ' : ' + str(data_b[key]))
	res = '{\n' + '\n'.join(diff) + '\n}'
	return res