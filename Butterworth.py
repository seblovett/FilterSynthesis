#!/usr/bin/python
# @file Butterworth.py
# Date Created: Thu 17 Jul 2014 10:44:20 BST by seblovett on seblovett-Ubuntu
# <+Last Edited: Sat 19 Jul 2014 12:11:38 BST by seblovett on seblovett-Ubuntu +>
# @author seblovett
# @brief A brief description of this code

import math
import RC_Match

def TF_ToString(TF):
	#print("To String Fn")
	TFS = "H(s)="
	for t in TF:
		#print t
		f="("
		for i in range(len(t)-1,-1,-1):
			#print i
			if i == 0:
				f+=" %f )" % t[len(t) - 1 - i]
			elif i == 1:
				f+= " %fs +"% t[len(t) - 1 - i]
			else:
				s = "s^%d " % i
				f += "%f%s + " % (t[len(t) - 1 - i],s)
		
		#print f
		TFS += f
	return TFS
## @brief Documentation for a function.
#  @param - None
#  @retval - None
#  More details.
def MakeTF(order=1):
	n = order #save for later
	# is the order odd?
	TF = list()
	if (order % 2):
		#print "Odd"
		TF.append([1,1])
		order -= 1
	order /= 2
	for k in range(1,order+1):
		#print k
		coeff = -2.0 * math.cos( math.pi*((2.0*float(k) + float(n) - 1.0 ) / (2.0*float(n))) )
		#print coeff
		TF.append([1,coeff,1])
		#TF+= "(s^2 + %fs + 1)" % coeff
	#print TF
	print TF_ToString(TF)
	return TF

## @brief Converts a 1st / 2nd order transfer function to the component values needed
def TF_to_Value(tf, w0, outfile):
	if (len(tf) == 2):
		print("First order")
		outfile.write("First Order:\n")
		#easy - just need to make RC constant correct.
		(R, C, er) = RC_Match.RC_Mult(1.0/w0)
		outfile.write("R=%e\nC=%e\n" % (R,C))
	elif (len(tf)==3):
		print("Second order")
		outfile.write("Second Order:\n")
		(R, C, er) = RC_Match.RC_Mult(1.0/w0)
		outfile.write("R=%e\nC=%e\n" % (R,C))
		#check that the TF is in standard form
		#@todo attempt to normalise a tf if possible
		if tf[0] != 1.0:
			raise Exception("TF is not normalised")
			
		if tf[2] != 1.0:
			raise Exception("TF is not normalised")
		
		Q = 1.0 / tf[1] 
		A = 3.0 - 1.0/Q
		RfRg = A - 1
		print("Q=%e\nA=%e\n" % (Q, A))
		if (A > 3.0) or (A < 1.0):
			raise Exception("Filter will be unstable")
		(Rf, Rg, err) = RC_Match.RR_Div(RfRg)
		
		outfile.write("Rf=%e\nRg=%e\nQ=%e,A=%e\n" % (Rf,Rg,Q,A))
	else:
		raise Exception("Can only realise 1st / 2nd order functions")
	pass

if "__main__" == __name__:
	''' Code to be run if this is main '''
	print("Will generate a Butterworth transfer function")
#	for i in range(1,9):
#		print "Order: %d" % i
#		MakeTF(i)
	f = open("Filter.txt", 'w')
	w0 = 2000*math.pi
	Order = 4
	
	f.write("Butterworth Filter\nw0=%e\nOrder=%d\n" % (w0, Order))
	tf = MakeTF(Order)
	i = 0
	for t in tf:
		i += 1	
		f.write("Stage %d\n" % i)
		TF_to_Value(t, w0, f)
	f.close()
	pass

