#-*- coding: utf-8 -*-
import random


class html_dom_control:
	var_list = []
	DOM_document_method = {
		"adoptNode" : {
			"return" : ["element"],
			"argument" : ["element"]
		},
		"clear" : {
			"return" : [],
			"argument" : []
		},
		"createAttribute" : {
			"return" : ["attributeNode"],
			"argument" : ["attributeName"]
		},
		"createAttributeNS" : {
			"return" : ["attributeNode"],
			"argument" : ["String","attributeName"]
		},
		"createComment" : {
			"return" : ["element"],
			"argument" : ["String"],
		},
		"createDocumentFragment" : {
			"return" : ["element"],
			"argument" : []
		},
		"createElement" : {
			"return" : ["element"],
			"argument" : ["Tagname"]
		},
		"createElementNS" : {
			"return" : ["element"],
			"argument" : ["String","Tagname"]
		},
		"createNodeIterator" : {
			"return" : ["NodeIterator"],
			"argument" : ["element","NodeFilter.SHOW_ELEMENT","ElementChecker","Bool"]
		},
		"createNSResolver" : {
			"return" : ["document_element"],
			"argument" : ["String"]
		},
		"createTextNode" : {
			"return" : ["TextNode"],
			"argument" : ["String"]
		},
		"createTreeWalker" : {
			"return" : ["TreeWalker"],
			"argument" : ["element","NodeFilter.SHOW_ELEMENT","ElementChecker","Bool"]
		},
		"elementFromPoint" : {
			"return" : ["TextNode"],
			"argument" : ["Integer","Integer"]
		},
		"getElementById" : {
			"return" : ["element"],
			"argument" : ["element_id"]
		},
		"getElementsByName" : {
			"return" : ["NodeList"],
			"argument" : ["attributeName"]
		},
		"hasFocus" : {
			"return" : ["Bool"],
			"argument" : []
		},
		"importNode" : {
			"return" : ["Bool"],
			"argument" : ["element","Bool"]
		},
		"open" : {
			"return" : ["document_element"],
			"argument" : [{"String" : ["text/html","text/plain","image/gif","image/jpeg","image/xbm","plugin"]}]
		},
		"recalc" : {
			"return" : [],
			"argument" : ["Bool"]
		},
		"write" : {
			"return" : [],
			"argument" : ["String"]
		},
		"writeln" : {
			"return" : [],
			"argument" : ["String"]
		}
	}

	DOM_all_method = {
		"appendChild" : {
			"return" : ["element"],
			"argument" : ["element"]
		},
		"applyElement": {
			"return" : ["element"],
			"argument" : ["element", {"String" : ["outside","inside"] } ]
		},
		"clearAttributes" : {
			"return" : [],
			"argument" : []
		},
		"cloneNode" : {
			"return" : ["element"],
			"argument" : ["Bool"]
		},
		"compareDocumentPosition" : {
			"return" : ["Integer"],
			"argument" : ["element"]
		},
		"componentFromPoint" : {
			"return" : ["String"],
			"argument" : ["Integer","Integer"]
		},
		"contains" : {
			"return" : ["Bool"],
			"argument" : ["element"]
		},
		"getAdjacentText" : {
			"return" : ["element"],
			"argument" : [{"String":["before","afterBegin","beforeEnd","afterEnd"]}]
		},
		"getAttribute" : {
			"return" : ["String"],
			"argument" : ["attributeName",{"flags" : [0,1,2,3]}]
		},
		"getAttributeNode" : {
			"return" : ["attributeNode"],
			"argument" : ["attributeName"]
		},
		"getAttributeNodeNS" : {
			"return" : ["attributeNode"],
			"argument" : ["String","attributeName"]
		},
		"getAttributeNS" : {
			"return" : ["String"],
			"argument" : ["String","attributeName"]
		},
		"getElementsByClassName" : {
			"return" : ["NodeList"],
			"argument" : ["className"]
		},
		"getElementsByTagName" : {
			"return" : ["NodeList"],
			"argument" : ["Tagname"]
		},
		"getElementsByTagNameNS" : {
			"return" : ["NodeList"],
			"argument" : ["String","Tagname"]
		},
		"hasAttribute" : {
			"return" : ["Bool"],
			"argument" : ["attributeName"]
		},
		"hasAttributeNS" : {
			"return" : ["Bool"],
			"argument": ["attributeName"]
		},
		"hasAttributes" : {
			"return" : ["Bool"],
			"argument" : []
		},
		"hasChildNodes" : {
			"return" : ["Bool"],
			"argument" : []
		},
		"insertAdjacentElement" : {
			"return" : ["element"],
			"argument" : [{"String" : ["beforeBegin","afterBegin","afterEnd","beforeEnd"]},"element"]
		},
		"insertAdjacentHTML" : {
			"return" : ["element"],
			"argument" : [{"String" : ["beforeBegin","afterBegin","afterEnd","beforeEnd"]},"String"]
		},
		"insertAdjacentText" : {
			"return" : ["element"],
			"argument" : [{"String" : ["beforeBegin","afterBegin","afterEnd","beforeEnd"]},"TextNode"]
		},
		"insertBefore" : {
			"return" : ["element"],
			"argument" : ["element"]
		},
		"isEqualNode" : {
			"return" : ["Bool"],
			"argument" : ["element"]
		},
		"isSameNode" : {
			"return" : ["Bool"],
			"argument" : ["element"]
		},
		"mergeAttributes" : {
			"return" : [],
			"argument" : ["element","Bool"]
		},
		"normalize" : {
			"return" : [],
			"argument" : []
		},
		"removeAttribute" : {
			"return" : ["Bool"],
			"argument" : ["attributeName",{"Integer" : [0,1]}]
		},
		"removeAttributeNode" : {
			"return" : ["attributeNode"],
			"argument" : ["attributeNode"]
		},
		"removeAttributeNS" : {
			"return" : [],
			"argument" : ["String","attributeName"]
		},
		"removeChild" : {
			"return" : ["element"],
			"argument" : ["element"]
		},
		"removeNode" : {
			"return" : ["element"],
			"argument" : ["Bool"]
		},
		"replaceAdjacentText" : {
			"return" : ["String"],
			"argument" : [{"String" : ["beforeBegin","afterBegin","afterEnd","beforeEnd"]},"String"]
		},
		"replaceChild" : {
			"return" : ["element"],
			"argument" : ["element","element"]
		},
		"replaceNode" : {
			"return" : ["element"],
			"argument" : ["element"]
		},
		"scrollByLines" : {
			"return" : [],
			"argument" : ["Integer"]
		},
		"scrollByPages" : {
			"return" : [],
			"argument" : ["Integer"]
		},
		"scrollIntoView" : {
			"return" : [],
			"argument" : ["Bool"]
		},
		"setAttribute" : {
			"return" : [],
			"argument" : ["attributeName","String",{"Integer" : [0,1]}]
		},
		"setAttributeNode" : {
			"return" : ["attributeNode"],
			"argument" : ["attributeNode"]
		},
		"setAttributeNodeNS" : {
			"return" : ["attributeNode"],
			"argument" : ["attributeNode"]
		},
		"setAttributeNS" : {
			"return" : [],
			"argument" : ["String","attributeName","String"]
		},
		"swapNode" : {
			"return" : ["element"],
			"argument" : ["element"]
		}
	}
	DOM_nodeIterator_method = {
		"detach" : {
			"return" : [],
			"argument" : []
		},
		"nextNode" : {
			"return" : ["element"],
			"argument" : []
		},
		"previousNode" : {
			"return" : ["element"],
			"argument" : []
		}

	}
	DOM_TreeWalker_method = {
		"firstChild" : {
			"return" : ["element"],
			"argument" : []
		},
		"lastChild" : {
			"return" : ["element"],
			"argument" : []
		},
		"nextNode" : {
			"return" : ["element"],
			"argument" : []
		},
		"nextSibling" : {
			"return" : ["element"],
			"argument" : []
		},
		"parentNode" : {
			"return" : ["element"],
			"argument" : []
		},
		"previousNode" : {
			"return" : ["element"],
			"argument" : []
		},
		"previousSibling" : {
			"return" : ["element"],
			"argument" : []
		}

	}
	def __init__(self,used_element_random_select,var_id_to_tag):
		self.used_element_random_select = used_element_random_select
		self.var_id_to_tag = var_id_to_tag
	"""
	keyword_value : argument 및 return 리스트
	type_bit : return , argument 인가?
	 [{"String" : ["beforeBegin","afterBegin","afterEnd","beforeEnd"]},"TextNode"]
	"""
	def var_type_select(self,var_type):
		if var_type == None:
			return False
		var_list = self.var_list
		random.shuffle(var_list)
		for var in var_list:
			if str(var['var_type']) == str(var_type):
				return var
			return False

	def DOM_keyword(self,keyword_value,var,keyword_type): #keyword_type == True:return , False:argument
		if keyword_value == []:
			return False
		tag = {}
		if var['var_type'] == 'element' and var['tag_id'] != None:
			tag = self.var_id_to_tag(var['tag_id'])
		else:
			tag = False
		value = keyword_value
		
		if value != None:	
			if type(value) == dict:
				if keyword_type == True:
					return str(value[value.keys()[0]])
				else:
					return '"' + str(random.choice(value.values()[0])) + '"'
			if "element" in keyword_value: # html element
				if keyword_type == True:
					print var['var_id']
					return "element"
				else:
					dic = {}
					dic = self.var_type_select("element")
					if dic == False:
						return False
					return dic['var_id']
			if "array" in keyword_value: # javscript array
				if keyword_type == True:
					return "array"
				else:
					dic = {}
					dic = self.var_type_select("array")
					return dic['var_id']
				
			if "Bool" in keyword_value: # true and false
				if keyword_type == True:
					return "Bool"
				else:
					dic = ["true","false"]
					return str(random.choice(dic))

			if "Integer" in keyword_value: # number
				if keyword_type == True:
					return "Integer"
				else:
					return str("3")
				
			if "attributeName" in keyword_value: #html tag Attribute
				if keyword_type == True:
					return "attributeName"
				else:
					if tag == False:
						return False
					if tag['used_attributes'] == []:
						key = '"' + random.choice(tag['all_attributes'].keys()) + '"'
						return key
					return '"' + random.choice(tag['used_attributes']) + '"'


			if "attributeNode" in keyword_value: #html tag Attribute Node
				if keyword_type == True:
					return "attributeNode"
				else:
					return self.var_type_select("attributeNode")

			if "String" in keyword_value: #String 
				if keyword_type == True:
					return "String"
				else:
					return '"AA"'
				
			if "Tagname" in keyword_value: #html tag name
				if keyword_type == True:
					return "Tagname"
				else:
					if tag == False:
						return False
					return '"' + str(tag['tag_name']) + '"'
				
			if "NodeIterator" in keyword_value: #xml type document도 가능
				if keyword_type == True:
					return "NodeIterator"
				else:
					return self.var_type_select("NodeIterator")
				
			if "document_element" in keyword_value: # dcument pointer
				if keyword_type == True:
					return "document_element"
				else:
					return "document"
			if "TreeWalker" in keyword_value: #xml type document도 가능
				if keyword_type == True:
					return "TreeWalker"
				else:
					return self.var_type_select("TreeWalker")
			if "element_id" in keyword_value: #html tag id
				if keyword_type == True:
					return "element_id"
				else:
					return var['tag_id']
			if "NodeList" in keyword_value: #html tag list
				if keyword_type == True:
					return "NodeList"
				else:
					return self.var_type_select("NodeList")
			else:
				return '"'+ str(keyword_value) + '"'
		else:
			return True
	def javascript_start(self):
		return '\n<script type="text/javascript">\n'
	def javascript_end(self):
		return "\n</script>\n"

	def element_all_method_call(self,method_name,target_var,var):
		text = ""
		
		_return = self.DOM_keyword(self.DOM_all_method[method_name]['return'],target_var,True)
		if _return != False:
			var['var_type'] = str(_return)
			text += "\nvar " + str(var['var_id']) + ' = '
		text += str(target_var['var_id']) + '.' + str(method_name) + '('
		count = 0
		for arg in self.DOM_all_method[method_name]['argument']:
			count += 1
			_argument = self.DOM_keyword(arg,target_var,False)
			if _argument == False:
				return ""
			if _argument != True:
				text += _argument
			if count < len(self.DOM_all_method[method_name]['argument']):
				text += ','
		text += ');'
		self.var_list.append(var)
		return text


	def set_html_attribute(self,element_id,attribute,fuzz_ptr,attibute_name_select):
		if attribute == []:
			return ""
		text = ""
		attribute_name = attibute_name_select(attribute.keys())

		attribute_value = fuzz_ptr(attribute[attribute_name])
		text += '\nvar ' + str(element_id) + '=' + 'document.getElementById("' + str(element_id) + '");\n'
		text += str(element_id) + '.' + "setAttribute" + '("' + attribute_name + '",' + '"' + attribute_value  +'");' 
		#text += str(element_id) + '.' + attribute_name + '="'+ attribute_value +'";\n'
		return text

	def set_html_attribute2(self,element_id,attribute,fuzz_ptr,attibute_name_select):
		if attribute == []:
			return ""
		text = ""
		attribute_name = attibute_name_select(attribute.keys())

		attribute_value = fuzz_ptr(attribute[attribute_name])
		text += '\nvar ' + str(element_id) + '=' + 'document.getElementById("' + str(element_id) + '");\n'
		text += str(element_id) + '.'  + attribute_name + '=' + '"' + attribute_value  +'";' 
		#text += str(element_id) + '.' + attribute_name + '="'+ attribute_value +'";\n'
		return text


	def tag_id_to_var(self,TAG_ID,var):
		text = ""
		var['var_type'] = "element"
		var['tag_id'] = TAG_ID
		for v in self.var_list:
			if str(v['tag_id']) == str(TAG_ID):
				if len(v['parent_var']) > 0:
					return ""

		text += '\nvar ' + str(var['var_id']) + '=' + 'document.getElementById("' + str(var['tag_id']) + '");\n'
		self.var_list.append(var)
		return str(text)

	def garbage_collect(self):
		return "CollectGarbage();"

	def create_array(self,var):
		text = ""
		var['var_type'] = "array"
		text += '\nvar ' + str(var['var_id']) + ' = ' + '[' + ' ];'

		count = 0
		for arr in var['array']:
			text += str(var['var_id']) +'['+ str(count) + ']' + '=' + str(arr) + ';'  

		self.var_list.append(var)
		return str(text)


	def create_element(self,var,tag_name):
		text = ""

		var['var_type'] = "element"
		text += '\nvar ' + str(var['var_id']) + ' = ' + "document.createElement" + '("' + str(tag_name) + '");'
		self.var_list.append(var)
		return str(text)

	def create_child_insert(self,p_var,c_var):
		text = ""
		if p_var['var_type'] != "element" or c_var['var_type'] != "element":
			return ""
		if p_var['var_id'] == c_var['var_id']:
			return ""
		if p_var['tag_id'] == c_var['tag_id']:
			return ""

		p_var['child_var'].append(c_var['var_id'])
		c_var['parent_var'].append(p_var['var_id'])

		text += '\n' + str(p_var['var_id']) + '.' + 'appendChild(' + str(c_var['var_id']) + ');\n'
		return text

	def create_child_remove(self,p_var,c_var):
		text = ""
		if p_var['var_type'] != "element" or c_var['var_type'] != "element":
			return ""
		if p_var['var_id'] == c_var['var_id']:
			return ""
		if p_var['tag_id'] == c_var['tag_id']:
			return ""

		if not c_var['var_id'] in p_var['child_var']:
			return ""



		p_var['child_var'].remove(c_var["var_id"])

		text += '\n' + str(p_var['var_id']) + '.' + 'removeChild(' + str(c_var['var_id']) + ');\n'
		return text

	def create_treewalker(self,var,target_var):
		text = ""
		if target_var['var_type'] != "element":
			return ""
		var['var_type'] = "TreeWalker"
		text = '\n'+ str(var['var_id']) + "= document.createTreeWalker(" + str(target_var['var_id']) + ", NodeFilter.SHOW_ELEMENT, ElementChecker, false);\n"
		self.var_list.append(var)

		return text

	def create_nodeiterator(self,var,target_var):
		text = ""
		if target_var['var_type'] != "element":
			return ""

		var['var_type'] = "NodeIterator"
		text = '\n'+ str(var['var_id']) + "= document.createNodeIterator("+ str(target_var['var_id']) +", NodeFilter.SHOW_ELEMENT, ElementChecker, false);\n"
		self.var_list.append(var)

		return text

	def elementChecker(self):
		text = "function ElementChecker (node) {if (node.tagName.toLowerCase () == 'button') {return NodeFilter.FILTER_ACCEPT;}return NodeFilter.FILTER_SKIP;}"
		return str(text)







