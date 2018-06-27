#!/usr/bin/env python
import tensorflow as tf
import sys
import os
import argparse
import json

# speicherorte fuer trainierten graph und labels in train.sh festlegen ##

# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

parser = argparse.ArgumentParser()
parser.add_argument("local", help="local path to image")
parser.add_argument("-l","--local", action="store_true", help="path to local file")
args = parser.parse_args()





image_path = args.local


#bilddatei readen
image_data = tf.gfile.FastGFile(image_path, 'rb').read()


# holt labels aus file in array 
label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("/home/legion/Documents/project/tf_files/retrained_labels.txt")] #values to be changed during paths
# !! labels befinden sich jeweils in eigenen lines -> keine aenderung in retrain.py noetig -> falsche darstellung im windows editor !!
				   
# graph einlesen, wurde in train.sh -> call retrain.py trainiert
with tf.gfile.FastGFile("/home/legion/Documents/project/tf_files/retrained_graph.pb", 'rb') as f:
 
    graph_def = tf.GraphDef()	## The graph-graph_def is a saved copy of a TensorFlow graph; objektinitialisierung
    graph_def.ParseFromString(f.read())	#Parse serialized protocol buffer data into variable
    _ = tf.import_graph_def(graph_def, name='')	# import a serialized TensorFlow GraphDef protocol buffer, extract objects in the GraphDef as tf.Tensor
	

with tf.Session() as sess:

    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
	

    predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': image_data})
    
	
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    nest_dict = {}
    n=0
    l=[]		
	# output
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        human_string1 = human_string.split()
        
        l.append(human_string1)

        n+=1
n=0
cat_heads = []
arr = []
main_arr = []
p = l

for n in range (len(l)):
			
			#print(p[n][0])
			g = p[n][1]
			#print (g)

for m in range(len(l)):
	if l[m][0] in cat_heads:
		print ("")
		#print ("booozzz!!!")	


	elif l[m][0] not in cat_heads:
		arr =[]
		for n in range (len(l)):
			x = 0
			t = l[m][0]
			if p[n][0] == t :
				g = p[n][1]
				#print (g)
				arr.append(g)
				#print (arr)
				x+=1
				
		cat_heads.append((l[m][0]))		
		main_arr.append(arr)
	


#print (main_arr)
#print (cat_heads)

sihal = []
for m in range(len(cat_heads)):
	di = {}
	di['type'] = cat_heads[m]
	di['order'] = main_arr[m]
	sihal.append(di)

#print (sihal)	

final_dic = {}

final_dic['result'] = sihal

#print ( final_dic )

"""
req_json = Request( 'http://localhost/tete/hello.php' , headers)
jsondata = json.dumps(final_dic)
	

resp = urlopen(req_json, jsonenc)
"""

jsondata = json.dumps(final_dic)

#request = requests.get("http://192.168.1.245:8521/pro/hello.php" , data = jsondata)

print (jsondata)
"""
with open('data.txt', 'w') as ouputt:
	json.dump(final_dic, ouputt)
"""
json_l = json.loads(jsondata)

