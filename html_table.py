#-*- coding: utf-8 -*-
class html_table_control():
	tag = {
		"table" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"], "unSelectable" : ["on","off"]},
			"event" : []
		},
		"tBody" : {
					"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"], "unSelectable" : ["on","off"]},
					"event" : []
				},
		"td" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"], "unSelectable" : ["on","off"]},
			"event" : []
		},
		"tFoot" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"], "unSelectable" : ["on","off"]},
			"event" : []
		},
		"th" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"], "unSelectable" : ["on","off"]},
			"event" : []
		},
		"tHead" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"], "unSelectable" : ["on","off"]},
			"event" : []
		},
		"tr" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"], "unSelectable" : ["on","off"]},
			"event" : []
		},
		"caption" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"], "unSelectable" : ["on","off"]},
			"event" : []
		},
		"col" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"], "unSelectable" : ["on","off"]},
			"event" : []
		},
		"colGroup" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"], "unSelectable" : ["on","off"]},
			"event" : []
		}
	}

	def __init__(self):
		pass
	def table_tag_start(self):
		return self.tag['table']
	def table_tag_end(self):
		return "</table>"

	def table_head_start(self):
		return self.tag['tHead']
	def table_head_end(self):
		return "</tHead>"

	def table_caption_start(self):
		return self.tag['caption']
	def table_caption_end(self):
		return "</caption>"

	def table_body_start(self):
		return self.tag['tBody']
	def table_body_end(self):
		return "</tBody>"

	def table_tfoot_start(self):
		return self.tag['tFoot']
	def table_tfoot_end(self):
		return "</tFoot>"

