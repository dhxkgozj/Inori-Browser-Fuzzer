import random

"""
@font-face {
    font-family: myFirstFont;
    src: url(sansation_light.woff);
}
@keyframes mymove {
    from {top: 0px;}
    to {top: 200px;}
}
@media screen and (max-width: 300px) {
    body {
        background-color: lightblue;
    }
}
"""
class css_control():
	css = {
		'align-content' : ['stretch','center','flex-start','flex-end','space-between','space-around','initial','inherit'],
		'align-items' : ['stretch','center','flex-start','flex-end','baseline','initial','inherit'],
		'align-self' : ['auto','stretch','flex-start','flex-end','baseline','initial','inherit'],
		'animation' : ['initial','inherit'],
		'animation-delay' : ['time','initial','inherit'],
		'animation-direction' : ['normal','reverse','alternate','alternate-reverse','initial','inherit'],
		'animation-duration' : ['time','initial','inherit'],
		'animation-fill-mode' : ['none','forwards','backwards','both','initial','inherit'],
		'animation-iteration-count' : ['number','infinite','initial','inherit'],
		'animation-name' : ['keyframename','none','initial','inherit'],
		'animation-play-state' : ['paused','running','initial','inherit'],
		'animation-timing-function' : ['linear','ease','ease-in','ease-in-out','cubic-bezier(33,44,3,44)','initial','inherit'],
		'backface-visibility' : ['visible','hidden','initial','inherit'],
		'background' : ['initial','inherit'],
		'background-attachment' : ['scroll','fixed','local','initial','inherit'],
		'background-clip' : ['border-box','padding-box','content-box','initial','inherit'],
		'background-color' : ['color','transparent','initial','inherit'],
		'background-image' : ['url','none','initial','inherit'],
		'background-origin' : ['padding-box','border-box','content-box','initial','inherit'],
		'background-position' : ['location','25%% 35%%','px','px','initial','inherit'],
		'background-repeat' : ['repeat','repeat-x','repeat-y','no-repeat','initial','inherit'],
		'background-size' : ['auto','length','cover','contain','initial','inherit'],
		'border' : ['initial','inherit'],
		'border-bottom' : ['initial','inherit'],
		'border-bottom-color' : ['color','transparent','initial','inherit'],
		'border-bottom-left-radius' : ['length','30%','initial','inherit'],
		'border-bottom-right-radius' : ['length','30%','initial','inherit'],
		'border-bottom-style' : ['none','hidden','dotted','dashed','double','groove','ridge','inset','outset','initial','inherit'],
		'border-bottom-width' : ['medium','thin','thick','single_length','initial','inherit'],
		'border-collapse' : ['separate','collapse','initial','inherit'],
		'border-color' : ['color','transparent','initial','inherit'],
		'border-image' : ['initial','inherit'],
		'border-image-outset' : ['length','number','initial','inherit'],
		'border-image-repeat' : ['stretch','repeat','round','space','initial','inherit'],
		'border-image-slice' : ['number','3%','fill','initial','inherit'],
		'border-image-source' : ['none','url','initial','inherit'],
		'border-image-width' : ['length','number','30%','auto','initial','inherit'],
		'border-left' : ['initial','inherit'],
		'border-left-color' : ['color','transparent','initial','inherit'],
		'border-left-style' : ['none','hidden','dotted','dashed','solid','double','groove','ridge','inset','outset','initial','inherit'],
		'border-left-width' : ['medium','thin','thick','single_length','initial','inherit'],
		'border-radius' : ['single_length','30%','initial','inherit'],
		'border-right' : ['initial','inherit'],
		'border-right-color' : ['color','transparent','initial','inherit'],
		'border-right-style' : ['none','hidden','dotted','dashed','solid','double','ridge','inset','outset','initial','inherit'],
		'border-right-width' : ['medium','thin','thick','single_length','initial','inherit'],
		'border-spacing' : ['length','initial','inherit'],
		'border-style' : ['none','hidden','dotted','dashed','solid','double','groove','ridge','inset','outset','initial','inherit'],
		'border-top' : ['initial','inherit'],
		'border-top-color' : ['color','transparent','initial','inherit'],
		'border-top-left-radius' : ['length','35%','initial','inherit'],
		'border-top-right-radius' : ['length','34%','initial','inherit'],
		'border-top-style' : ['none','hidden','dotted','dashed','solid','double','groove','ridge','inset','outset','initial','inherit'],
		'border-top-width' : ['medium','thin','thick','single_length','inherit'],
		'border-width' : ['medium','thin','thick','length','initial','inherit'],
		'bottom' : ['auto','single_length','34%','initial','inherit'],
		'box-shadow' : ['none','20px 20px 50px 20px pink','20px 20px 50px 20px pink inset','initial','inherit'],
		'box-sizing' : ['content-box','border-box','initial','inherit'],
		'caption-side' : ['top','bottom','initial','inherit'],
		'clear' : ['none','left','right','both','initial','inherit'],
		'clip' : ['auto','shape','initial','inherit'],
		'color' : ['color','initial','inherit'],
		'column-count' : ['number','auto','initial','inherit'],
		'column-fill' : ['balance','auto','initial','inherit'],
		'column-gap' : ['single_length','normal','initial','inherit'],
		'column-rule' : ['initial','inherit'],
		'column-rule-color' : ['color','initial','inherit'],
		'column-rule-style' : ['none','hidden','dotted','dashed','solid','double','groove','ridge','inset','outset','initial','inherit'],
		'column-rule-width' : ['medium','thin','thick','single_length','initial','inherit'],
		'column-span' : ['1','all','initial','inherit'],
		'column-width' : ['auto','single_length','initial','inherit'],
		'columns' : ['auto','initial','inherit'],
		'counter-increment' : ['subsection','none','1','initial','inherit'],
		'counter-reset' : ['section','none','initial','inherit'],
		'cursor' : ['alias','all-scroll','auto','cell','context-menu','col-resize','copy','crosshair','default','e-resize','ew-resize','grab','grabbing','help','move','n-resize','ne-resize','nesw-resize','ns-resize','none','not-allowed','progress','url','initial','inherit'],
		'direction' : ['ltr','rtl','initial','inherit'],
		'display' : ['inline','block','list-item','none','flex','inline-block','inline-flex','run-in','table-row-group','initial','inherit'],
		'empty-cells' : ['show','hide','initial','inherit'],
		'flex' : ['auto','initial','none','inherit'],
		'flex-basis' : ['number','auto','initial','inherit'],
		'flex-direction' : ['row','row-reverse','column','column-reverse','initial','inherit'],
		'flex-flow' : ['flex-direction','flex-wrap','initial','inherit'],
		'flex-grow' : ['number','initial','inherit'],
		'flex-shrink' : ['number','initial','inherit'],
		'flex-wrap' : ['nowrap','wrap','wrap-reverse','initial','inherit'],
		'float' : ['none','left','right','initial','inherit'],
		'font' : ['caption','icon','menu','message-box','small-caption','status-bar','initial','inherit'],
		'font-family' : ['Georgia','Book Antiqua','Arial','Impact','initial','inherit'],
		'font-size' : ['medium','xx-small','x-small','small','large','x-large','xx-large','smaller','larger','single_length','30%','initial','inherit'],
		'font-size-adjust' : ['number','none','initial','inherit'],
		'font-stretch' : ['ultra-condensed','extra-condensed','condensed','semi-condensed','normal','semi-expanded','expanded','extra-expanded','ultra-expanded','initial','inherit'],
		'font-style' : ['normal','italic','oblique','initial','inherit'],
		'font-variant' : ['normal','small-caps','initial','inherit'],
		'font-weight' : ['normal','bold','bolder','lighter','100','initial','inherit'],
		'hanging-punctuation' : ['none','first','last','allow-end','force-end','initial','inherit'],
		'height' : ['auto','single_length','30%','initial','inherit'],
		'justify-content' : ['flex-start','flex-end','center','space-between','space-around','initial','inherit'],
		'left' : ['auto','single_length','30%','initial','inherit'],
		'letter-spacing' : ['normal','single_length','initial','inherit'],
		'line-height' : ['normal','number','single_length','30%','initial','inherit'],
		'list-style' : ['initial','inherit'],
		'list-style-image' : ['none','url','initial','inherit'],
		'list-style-position' : ['inside','outside','initial','inherit'],
		'list-style-type' : ['disc','armenian','circle','cjk-ideographic','decimal','decimal-leading-zero','georgian','hebrew','none','initial','inherit'],
		'margin' : ['length','30%','auto','initial','inherit'],
		'margin-bottom' : ['single_length','30%','auto','initial','inherit'],
		'margin-left' : ['single_length','30%','auto','initial','inherit'],
		'margin-right' : ['single_length','30%','auto','initial','inherit'],
		'margin-top' : ['single_length','30%','auto','initial','inherit'],
		'max-height' : ['none','single_length','30%','initial','inherit'],
		'max-width' : ['none','single_length','34%','initial','inherit'],
		'min-height' : ['single_length','34%','initial','inherit'],
		'min-width' : ['single_length','44%','initial','inherit'],
		'opacity' : ['number','initial','inherit'],
		'order' : ['number','initial','inherit'],
		'outline' : ['initial','inherit'],
		'outline-color' : ['invert','color','initial','inherit'],
		'outline-offset' : ['single_length','initial','inherit'],
		'outline-style' : ['none','hidden','dotted','dashed','solid','double','groove','ridge','inset','outset','initial','inherit'],
		'outline-width' : ['medium','thin','thick','single_length','initial','inherit'],
		'overflow' : ['visible','hidden','scroll','auto','initial','inherit'],
		'overflow-x' : ['visible','hidden','scroll','auto','initial','inherit'],
		'overflow-y' : ['visible','hidden','scroll','auto','initial','inherit'],
		'padding' : ['single_length','33%','initial','inherit'],
		'padding-bottom' : ['single_length',"34%",'initial','inherit'],
		'padding-left' : ['single_length','44%','initial','inherit'],
		'padding-right' : ['single_length','45%','initial','inherit'],
		'padding-top' : ['single_length','55%','initial','inherit'],
		'page-break-after' : ['auto','always','avoid','left','right','initial','inherit'],
		'page-break-before' : ['auto','always','avoid','left','right','initial','inherit'],
		'page-break-inside' : ['auto','avoid','initial','inherit'],
		'perspective' : ['single_length','none','initial','inherit'],
		'perspective-origin' : ['44%% 33%%','initial','inherit'],
		'position' : ['static','absolute','fixed','relative','initial','inherit'],
		'quotes' : ['none',"'<' '>'",'initial','inherit'],
		'resize' : ['none','both','horizontal','vertical','initial','inherit'],
		'right' : ['auto','single_length','initial','inherit'],
		'tab-size' : ['number','single_length','initial','inherit'],
		'table-layout' : ['auto','fixed','initial','inherit'],
		'text-align' : ['left','right','center','justify','initial','inherit'],
		'text-align-last' : ['auto','left','right','center','justify','start','end','initial','inherit'],
		'text-decoration' : ['none','underline','overline','line-through','initial','inherit'],
		'text-decoration-color' : ['color','initial','inherit'],
		'text-decoration-line' : ['none','underline','overline','line-through','initial','inherit'],
		'text-decoration-style' : ['solid','double','dotted','dashed','wavy','initial','inherit'],
		'text-indent' : ['single_length','44%','initial','inherit'],
		'text-justify' : ['auto','inter-word','inter-ideograph','inter-cluster','distribute','kashida','trim','none','initial','inherit'],
		'text-overflow' : ['clip','ellipsis','visible','initial','inherit'],
		'text-shadow' : ['h-shadow','v-shadow','blur-radius','color','none','initial','inherit'],
		'text-transform' : ['none','capitalize','uppercase','lowercase','initial','inherit'],
		'top' : ['auto','single_length','44%','initial','inherit'],
		'transform' : ['none','matrix(0.866,0.5,-0.5,0.866,0,0)','translate(10px)','translate3d(30,-3,3)','scaleX(330)','perspective(33)','initial','inherit'],
		'transform-origin' : ['0 -1', '33 -3', '33 33', '0 0','initial','inherit'],
		'transform-style' : ['flat','preserve-3d','initial','inherit'],
		'transition' : ['initial','inherit'],
		'transition-delay' : ['3s','initial','inherit'],
		'transition-duration' : ['1s','-2s','initial','inherit'],
		'transition-property' : ['none','all','property','initial','inherit'],
		'transition-timing-function' : ['ease','linear','ease-in','ease-out','ease-in-out','cubic-bezier(3,4,5,6)','initial','inherit'],
		'unicode-bidi' : ['normal','embed','bidi-override','initial','inherit'],
		'vertical-align' : ['baseline','single_length','42%','sub','super','top','text-top','middle','bottom','text-bottom','initial','inherit'],
		'visibility' : ['visible','hidden','collapse','initial','inherit'],
		'white-space' : ['normal','nowrap','pre','pre-line','pre-wrap','initial','inherit'],
		'width' : ['auto','single_length','45%','initial','inherit'],
		'word-break' : ['normal','break-all','keep-all','initial','inherit'],
		'word-spacing' : ['normal','single_length','initial','inherit'],
		'word-wrap' : ['normal','break-word','initial','inherit'],
		'z-index' : ['auto','number','initial','inherit']
		
	}
	css_quota_type = {
		'content' : ['normal','none','counter','attr','"Read"','open-quote','close-quote','no-open-quote','no-close-quote','url','initial','inherit']
	}

	def __init__(self):
		pass

	def css_location(self):
		location = ['left top',
			'left center',
			'left bottom',
			'right top',
			'right center',
			'right bottom',
			'center top',
			'center center',
			'center bottom'
		]
		return random.choice(location)

	def css_color(self):
		color = ['red','blue','#000000','#ff9900','rgb(255,255,255)','rgb(3,255,1)']
		return random.choice(color)

	def css_url(self):
		return "url('/1.png')"

	def css_length(self):
		return "100px 100px"

	def css_single_length(self):
		return "100px"

	def css_attr(self):
		return "attr(random.choice(id))"


	def css_id(self):
		pass


	def type_css(self,css_property):
		for pro in css_property:
			if pro == "time":
				return "-1s"

			if pro == "number":
				return "1"

			if pro == "color":
				return self.css_color()

			if pro == "url":
				return self.css_url()

			if pro == "location":
				return self.css_location()

			if pro == "length":
				return self.css_length()

			if pro == "single_length":
				return self.css_single_length()

			if pro == "attr":
				return self.css_attr()

			if pro == "id":
				return self.css_id()

	def css_style_start(self):
		return "\n<style>\n"

	def css_style_end(self):
		return "\n</style>\n"

	def css_style_create(self,tag_name,css_name,css_property):
		style = str(tag_name) + "{" + str(css_name) + ":" + random.choice(css_property) + ";}"
		return style

