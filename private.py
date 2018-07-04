#python 

with open("container.yaml","r") as stream :
	try :
		yaml_data = yaml_load(stream)
		download = yaml_data['Download']
	except yaml.YAMLERROR as exc:
		print(exc) 