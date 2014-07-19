#!/usr/bin/python
# @file RC_Match.py
# Date Created: Thu 17 Jul 2014 11:45:32 BST by seblovett on seblovett-Ubuntu
# <+Last Edited: Thu 17 Jul 2014 16:06:45 BST by seblovett on seblovett-Ubuntu +>
# @author seblovett
# @brief A brief description of this code


## @brief calculates approximations for the E series.
#  @param - E - the number of series (e.g. 3,6,12,24...)
#  @retval - Series, list of the numbers in the series to one decimal place
def E_series(E):
	Series = []
	for i in range(E):
		Series.append(round(10.0 ** (float(i) / float(E)),1))
	print Series
	return Series

## @brief Calculates the best combination of R and C from E series values to minimise error of the product.
#  @param - target - the value to make from R*C. R_e, C_e - Resistor / Capacitor series to use (def. 12, 6), tol - acceptable error, in per cent
#  @retval - (R_value, C_value, error) - the best suited R and C values and the error
#  More details.
def RC_Mult(target,R_e=12,C_e=6,tol=None):
	if target < 0.0:
		target = -target #can not deal with negative numbers
	factor = 1
	target_init = target
	while ( target > 10.0 ):
		factor *= 10.0 #store the factor
		target /= 10.0
	while ( target < 1.0 ):
		factor /= 10.0
		target *= 10.0
	print "Normalised Target = %f, factor = %f" % (target, factor)
	
	#make the e series values. 
	R_series = E_series(R_e)
	C_series = E_series(C_e)
	R_best = None
	C_best = None
	Error = tol #needs to be better than this to qualify
	#itterate over the two series
	for r in R_series:
		for c in C_series:
			#calculate error
			err = 100 * (( target - r*c) / target )
			if err < 0:
				err = -err
			#keep tabs on the best solution
			if (err < Error) or (Error == None):
				R_best = r
				C_best = c
				Error = err
				print "Found new best: R=%f, C=%f, Err=%f" % (R_best, C_best, Error)
	if R_best == None:
		print("Cannot find a good enough solution")
	else:
		if factor > 1: #make R bigger
			R_best *= factor
		elif factor < 1:
			#make C smaller
			C_best *= factor
		while (C_best > 10e-9) and ( R_best < 1e5):
			#limit C to nF and R to MOhm
			C_best *= 0.1 #shift both values
			R_best *= 10 
		err = 100 * (( target_init - R_best*C_best) / target_init )

		print "R = %e, C = %e, R*C=%e Error = %f%%" % (R_best, C_best, R_best * C_best, err)
	return (R_best, C_best, err)


## @brief Calculates the best combination of R1 and R2 from E series values to minimise error of the division of R1/R2.
#  @param - target - the value to make from R1/R2. R_e Resistor series to use (def. 12), tol - acceptable error, in per cent
#  @retval - (R1_value, R2_value, error) - the best suited R values and the error
#  More details.
def RR_Div(target,R_e=12,tol=None):
	if target < 0.0:
		target = -target #can not deal with negative numbers
	factor = 1
	target_init = target
	while ( target > 10.0 ):
		factor *= 10.0 #store the factor
		target /= 10.0
	while ( target < 1.0 ):
		factor /= 10.0
		target *= 10.0
	print "Normalised Target = %f, factor = %f" % (target, factor)
	
	#make the e series values. 
	R1_series = E_series(R_e)
	R2_series = E_series(R_e)
	R1_best = None
	R2_best = None
	Error = tol #needs to be better than this to qualify
	#itterate over the two series
	for r1 in R1_series:
		for r2 in R2_series:
			#calculate error
			err = 100 * (( target - r1/r2) / target )
			if err < 0:
				err = -err
			#keep tabs on the best solution
			if (err < Error) or (Error == None):
				R1_best = r1
				R2_best = r2
				Error = err
				print "Found new best: R1=%f, R2=%f, Err=%f" % (R1_best, R2_best, Error)
	if R1_best == None:
		print("Cannot find a good enough solution")
	else:
		if factor > 1: #make R bigger
			R1_best *= factor
		elif factor < 1:
			#make C smaller
			R2_best /= factor
#		while (R_best > 10e-9) and ( R_best < 1e5):
#			#limit C to nF and R to MOhm
#			C_best *= 0.1 #shift both values
#			R_best *= 10 
		err = 100 * (( target_init - R1_best*R2_best) / target_init )

		print "R1 = %e, R2 = %e, R1/R2=%e Error = %f%%" % (R1_best, R2_best, R1_best / R2_best, err)
	return (R1_best, R2_best, err)

if "__main__" == __name__:
	print "RC Matcher"
	#E_series(12)
	RC_Mult(0.1200)
	RR_Div(0.2)
	
	
	pass

