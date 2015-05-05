#-*- coding: utf-8 -*-

import sys,subprocess
import json
from css import *
from html import *
from html_dom import *
from html_table import *

import random
import time


"""
css = css style [ dic ]
html = html tag [ list ]
"""


class create_html():
	tag_status = []
	html_text = "" # html text
	tag_text_buf = []
	def __init__(self):
		self.css = css_control()
		self.html = html_control()
		self.html_dom = html_dom_control(self.used_element_random_select,self.var_id_to_tag)
		self.html_table = html_table_control()
		self.body_bit = True
		self.head_bit = True
		self.style_bit = True
		self.table_bit = True
		self.frame_bit = True
		self.tag_count = 0
		self.var_count = 0
	def css_style_random_select(self):
		css = {}
		rand_css_style = random.choice(self.css.css.keys())
		css[rand_css_style] = self.css.css[rand_css_style]
		return css

	def html_tag_random_select(self):
		while 1:
			tag_name = random.choice(self.html.tag.keys())
			if self.body_bit == True and str(tag_name) == "body":
				continue
			if self.head_bit == True and str(tag_name) =="head":
				continue
			if self.table_bit == True and str(tag_name) == "tBody" or str(tag_name) == "tr" or str(tag_name) == "td" or str(tag_name) == "tFoot" or str(tag_name) == "th" or str(tag_name) == "tHead" or str(tag_name) == "caption" or str(tag_name) == "col" or str(tag_name) == "colGroup":
				continue
			if self.style_bit ==True and str(tag_name) == "style":
				continue
			if self.frame_bit == True and str(tag_name) == "frameSet" or str(tag_name) == "frame":
				continue
			if str(tag_name) == "plain Text":
				continue
			if str(tag_name) == "html":
				continue
			if str(tag_name) == "noScript":
				continue
			else:
				return tag_name

	def var_id_to_tag(self,TAG_ID):
		for status in self.tag_status:
			if str(status['tag_id']) == str(TAG_ID):
				return status
		return False




	def html_random_tag_create(self,tag_name,inner_text_value,attributes,event,attribute_value_ptr,option): #option is True = return, False tag_text_buf.append
		tag_status_dic = { #tag status
			"tag_id" : "",
			"tag_name" : "",
			"used_attributes" : [], # attribute 의 이름만 들어감 
			"all_attributes" : [],
			"used_event" : [],
			"all_event" : [],
			"css_info" : []
		}
		result = ""
		if tag_name == None:
			tag_name = create.html_tag_random_select()
		tag_status_dic['tag_name'] = tag_name
		tag_status_dic['tag_id'] = "a" + str(self.tag_count)
		self.tag_count += 1
		tag_status_dic['all_attributes'] = attributes
		if attributes == None:
			tag_status_dic['all_attributes'] = self.html.tag[tag_name]['attributes']
		if inner_text_value == None:
			inner_text_value = tag_status_dic['tag_id']
		tag_status_dic['used_event'] = event 
		# html_tag_start(self,tag_id,tag_name,attributes,event,attributes_value_ptr,inner_text_value,tag_status_dic)
		dic = self.html.html_tag_start(tag_status_dic['tag_id'],tag_status_dic['tag_name'],tag_status_dic['all_attributes'],None,None,inner_text_value,tag_status_dic) # <tag>
		if dic == {}:
			print "Create Fail!! : "
			print tag_name
			return False
		result = dic['text']
		if result == "":
			print "Create Fail!! : "
			print tag_name
			return False

		tag_status_dic = dic['tag_status_dic']
		if tag_status_dic == {}:
			print "Create Fail!! : "
			print tag_name
			return False
		del dic

		self.tag_status.append(tag_status_dic)
		if option == True:
			text_buf_dic = {}	
			text_buf_dic[tag_status_dic['tag_id']] = result
			self.tag_text_buf.append(text_buf_dic)
		else:
			return result



	def css_random_tag_create(self):
		if self.tag_status == []:
			return

		tag_status_dic = {}
		r = random.choice(self.tag_status)
		css_style = self.css_style_random_select()
		self.html_text += self.css.css_style_create(str(r['tag_name']),str(css_style.keys()[0]),css_style[css_style.keys()[0]])

		tag_status_dic = self.tag_status.pop(self.tag_status.index(r))
		tag_status_dic['css_info'].append(css_style)



		self.tag_status.append(tag_status_dic)

	def used_element_random_select(self):
		if self.tag_status == []:
			return None
		return random.choice(self.tag_status)


	def dom_random_attribute_set(self):
		html_text = ""
		use_element = self.used_element_random_select()
		if(use_element == None):
			return ""
		html_text += self.html_dom.set_html_attribute(use_element['tag_id'],use_element['all_attributes'],self.html.tag_attribute_type,self.html.tag_attribute_name)
		return html_text

	def dom_random_attribute_set2(self):
		html_text = ""
		use_element = self.used_element_random_select()
		if(use_element == None):
			return ""
		html_text += self.html_dom.set_html_attribute2(use_element['tag_id'],use_element['all_attributes'],self.html.tag_attribute_type,self.html.tag_attribute_name)
		return html_text

	"""
	def table_create(self):
		result = ""
		result += self.html_random_tag_create("table",None,None,False)
		result += self.html_random_tag_create("caption",None,None,False)
		result += self.html_random_tag_create("tHead",None,None,False)
		result += self.html_random_tag_create("")
	"""
	def create_var(self,var_id,var_type,array_size,array,tag_id):
		var = {
			"var_id" : "",
			"var_type" : "",
			"array_size" : "",
			"array" : [],
			"tag_id" : "",
			"parent_var" : [],
			"child_var" : [],

		}
		var['var_id'] = "v" + str(self.var_count)
		self.var_count = self.var_count + 1		
		if var_id != None:
			var['var_id'] = var_id
		if var_type != None:
			var['var_type'] = var_type
		if array_size != None:
			var['array_size'] = array_size
		if array != None:
			var['array'] = array
		if tag_id != None:
			var['tag_id'] = tag_id
		return var

	def dom_element_id_to_var(self,element_id):
		text = ""
		random_dic = {}
		var = {}
		random_dic['tag_id'] = element_id
		if element_id == None:
			random_dic = self.used_element_random_select()

		var = self.create_var(None,"element",None,None,random_dic['tag_id'])
		text = self.html_dom.tag_id_to_var(random_dic['tag_id'],var)
		return text

	def dom_create_array(self,array): # array = ["var_id1","var_id2","var_id3"]
		text = ""
		var = {}
		var = self.create_var(None,"array",None,None,None)
		if array == None:
			var['array'] = []
		var['array_size'] = len(var['array'])
		text = self.html_dom.create_array(var)
		return text


	def dom_create_element(self,tag_name):
		text = ""
		tag_status_dic = { #tag status
			"tag_id" : "",
			"tag_name" : "",
			"used_attributes" : [], # attribute 의 이름만 들어감 
			"all_attributes" : [],
			"used_event" : [],
			"all_event" : [],
			"css_info" : []
		}
		var = {}
		if tag_name == None:
			tag_name = create.html_tag_random_select()
		tag_status_dic['tag_name'] = tag_name
		tag_status_dic['tag_id'] = "a" + str(self.tag_count)
		tag_status_dic['all_attributes'] = self.html.tag[tag_name]['attributes']
		self.tag_count += 1
		var = self.create_var(None,"element",None,None,None)

		var['tag_id'] = tag_status_dic['tag_id']

		text += self.html_dom.create_element(var,tag_name)
		self.tag_status.append(tag_status_dic)

		return text

	def create_treewalker(self,target_var):
		text = ""
		if target_var == None:
			target_var = self.var_random_choice()
		var = {}
		var = self.create_var(None,"TreeWalker",None,None,None)
		text = self.html_dom.create_treewalker(var,target_var)
		return text
	def create_nodeiterator(self,target_var):
		text = ""
		if target_var == None:
			target_var = self.var_random_choice()
		var = {}
		var = self.create_var(None,"NodeIterator",None,None,None)
		text = self.html_dom.create_nodeiterator(var,target_var)
		return text
	def tag_id_match(self,tag_id):
		for tag in self.tag_status:
			if tag_id == tag['tag_id']:
				return tag
		return False

	def var_random_choice(self):
		var = random.choice(self.html_dom.var_list)
		return var

	def child_element_insert(self,p_var,c_var):
		text = self.html_dom.create_child_insert(p_var,c_var)
		return text
		

	def child_element_remove(self,p_var,c_var):
		text = self.html_dom.create_child_remove(p_var,c_var)
		return text
	def element_css_style_insert(self,var):
		pass
		

	def create_event(self,var):
		pass
	def focus_to_event(self,var):
		pass

	def random_var_method_call(self,target_var,method_name):
		text = ""
		if target_var == None:
			while(1):
				target_var = {}
				target_var = self.var_random_choice()
				if target_var['var_type'] == "element":
					break

		if method_name == None:
			method_name = {}
			method_name = random.choice(self.html_dom.DOM_all_method.keys())
		var = {}
		var = self.create_var(None,None,None,None,None)
		if target_var['var_type'] == "element":
			text = self.html_dom.element_all_method_call(method_name,target_var,var)

		return text


	

	def create_html(self,path):

		for x in range(1,10):
			#html_random_tag_create(self,tag_name,inner_text_value,attributes,event,attribute_value_ptr,option): #option is True = return, True tag_text_buf.append
			self.html_random_tag_create(None,None,None,None,None,True) # <tag> value </tag>


		self.html_text += self.html.html_start() # <html>
		self.html_text += self.html.html_head_start() # <head>
		self.html_text += self.css.css_style_start() # <style> 
		for x in range(1,30):
			self.css_random_tag_create()

		self.html_text += self.css.css_style_end() # </style>
		self.html_text += self.html.html_head_end() # </head>

		self.html_text += self.html.html_body_start() # <body>


		for buf in self.tag_text_buf:
			self.html_text += str(buf[buf.keys()[0]])
		self.tag_text_buf = []

		self.html_text += self.html_dom.javascript_start() # <script>
		self.html_text += self.html_dom.elementChecker()
		self.html_text += self.html_dom.garbage_collect() # CollectGarbage()

		#self.html_text += self.dom_random_attribute_set() # tag properties value setting ex) var a26=docmuent.getElementById("a26"); a26.setattibute("name","value");
		#self.html_text += self.dom_random_attribute_set2() # tag properties value setting ex) var a26=docmuent.getElementById("a26"); a26.defaultPlaybackRate="0xFF";
		for x in range(1,10):
			self.html_text += self.dom_element_id_to_var(None)
			self.html_text += self.dom_create_array(None)
			self.html_text += self.dom_create_element(None)
			self.html_text += self.child_element_insert(self.var_random_choice(),self.var_random_choice())
			#self.html_text += self.create_nodeiterator(None)
			self.html_text += self.random_var_method_call(None,None)
			self.html_text += self.child_element_remove(self.var_random_choice(),self.var_random_choice())
			#self.html_text += self.create_treewalker(None)

		self.html_text += self.html_dom.garbage_collect() # CollectGarbage()
		self.html_text += self.html_dom.javascript_end() # </script>

		self.html_text += self.html.html_body_end() # < /body>
		self.html_text += self.html.html_end() # </html>

		self.save_html(path)
		print "test.html Create Sucess!!"


	def save_html(self,path):
		if path == None:
			path = 'test.html'
		f = open(path,'w') # html document Create
		f.write(self.html_text)
		f.close()
		self.html_text = ""
		self.tag_count = 0
		self.tag_status = []
		self.tag_text_buf = []

if __name__=="__main__":
	create  = create_html()
	while(1):
		create.create_html('/Users/gimdong-wan/VM share/test.html')
		time.sleep(30)
