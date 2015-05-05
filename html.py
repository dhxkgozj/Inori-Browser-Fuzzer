#-*- coding: utf-8 -*-
import random
import json
import sys



class html_control():
	tag = {
		"a" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"addr" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"acronym" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"address" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"applet" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"area" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"b" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"base" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"baseFont" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"bdo" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"bgSound" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"big" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"blink" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"blockQuote" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"body" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"br" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"button" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"caption" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"center" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"cite" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"code" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"col" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"colGroup" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"comment" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"dd" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"del" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"dfn" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"dir" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"div" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"dl" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"dt" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"ern" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"embed" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"fieldSet" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"font" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"form" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"frame" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"frameSet" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"H1" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"H2" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"H3" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"H4" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"H5" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"H6" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"head" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"hr" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"html" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"i" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"iframe" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"img" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"input" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"ins" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"isIndex" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"kbd" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"keygen" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"label" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"legend" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"li" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"link" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"listing" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"map" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"marquee" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"menu" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"meta" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"nobr" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"noFrames" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"noScript" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"object" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"ol" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"optGroup" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"option" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"p" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"param" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"plain Text" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"pre" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"q" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"rt" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"ruby" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"s" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"samp" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"script" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"select" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"small" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"span" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"strike" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"strong" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"style" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"sub" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"sup" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"table" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"tBody" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"td" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"textArea" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"tFoot" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"th" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"tHead" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"title" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"tr" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"tt" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"u" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"ul" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"var" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"wbr" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"xml" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		},
		"xmp" : {
			"attributes" : {"accessKey" : ["char"],"cite" : ["href","String"],"class" : ["String"],"contentEditable" : ["inherit","Bool"],"dataFld" : ["String"], "dataFormatAs" : ["html","localized-text","text"],"dataSrc" : ["String"],"DateTime" : ["time"],"dir" : ["ltr","rtl"],"DISABLED" : ["disabled"],"draggable" : ["Bool"],"HIDEFOCUS" : ["hidefocus"] , "id" : ["String"],"lang" : ["String"] , "style" : ["css"],"tabIndex" : ["0","1"],"title" : ["String"]},
			"event" : []
		}
	}





	html_sp = []
	tag_status_use_dic = []
	def __init__(self):
		self.tag_count = 0


	def html_special_find(self,tag):
		if tag == "form":
			return True
		if tag == "iframe":
			return True

		return False

	def html_start(self):
		return "<!DOCTYPE html>\n<html>"

	def html_end(self):
		return "\n</html>"

	"""
	tag : 생성 할 태그 종류 [string]
	properties : 들어갈 옵션 [list]
	perent : 부모 tag
	tag_id : tag_id
	"""

	def html_body_start(self):
		return "\n<body>\n"
	def html_body_end(self):
		return "\n</body>\n"

	def html_head_start(self):
		return "\n<head>\n"
	def html_head_end(self):
		return "\n</head>\n"

	def html_tag_start(self,tag_id,tag_name,attributes,event,attributes_value_ptr,inner_text_value,tag_status_dic):
		if tag_id == None or tag_name == None:
			return {}

		text = "\n<"

		text = text + str(tag_name) # tag name insert

		text = text + " " + "id=" + '"'+str(tag_id) + '"'

		if attributes == {}:
			return {}
		for x in range(1,5):
			property_name = ""
			property_name = self.tag_attribute_name(attributes.keys())
			proper_value = self.tag_attribute_type(attributes[property_name])
			tag_status_dic['used_attributes'].append(property_name)
			text += " " + property_name + '="' + str(proper_value) + '"'

		text += ">\n"
		text += inner_text_value

		text += "\n</" + str(tag_name) + ">\n"

		dic = {}
		dic = {
			"text" : str(text),
			"tag_status_dic" : tag_status_dic
		}
		return dic


	def tag_attribute_name(self,properties):
		while 1:
			 name = random.choice(properties)
			 if "id" in name:
			 	continue
			 if "DateTime" in name:
			 	continue
			 if "style" in name:
			 	continue
			 if "DISABLED" in name:
			 	continue
			 if "title" in name:
			 	continue
			 return name

	def tag_attribute_type(self,attribute_type):
		for attr in attribute_type:
			if "char" in attr:
				return "a"
			elif "href" in attr:
				return "http://naver.com"
			elif "String" in attr:
				return "0xFF"
			elif "Bool" in attr:
				return "false"
			elif "time" in attr: # http://help.dottoro.com/lhrqjhwi.php
				return ""
			elif "css" in attr:
				return ""
			else:
				return str(attr)
