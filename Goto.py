#!/usr/bin/python3

###The following code is considered harmful.

class Goto(BaseException):
	'''my_label = Goto(); try: raise my_label; except my_label:'''
	def __new__(cls, *args, **kwargs):
		#This is the goto label. `except label:'
		return type('label', (Exception, BaseException, object,), {});
		#__new__() returns an instance, not a class.
		#return BaseException.__new__(cls, args, kwargs);

GOTO = Goto;

#Don't raise this.
initial_label=Goto();
initial_label.__doc__ = \
	"All labels need to be set to this initially. Don't raise this.";

##Example:
if __name__ == '__main__':
	from sys import argv;
	#We need to define the labels to prevent a NameError.
	#Also, label1 will be checked before label2.
	#Therefore, label1 needs to inherit from BaseException
	#in a way that doesn't overlap with label2.
	#It may be tempting to define these labels as BaseException,
	#but `except BaseException' will always trigger before any other label.
	label1 = initial_label;
	label2 = initial_label;

	try:
		if len(argv) == 1:
			label1 = Goto();
			raise label1;
		else:
			label2 = Goto();
			raise label2;
	except label1:
		print('foo');
	except label2:
		print('bar');
