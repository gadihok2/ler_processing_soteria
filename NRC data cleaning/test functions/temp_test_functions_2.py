# coding: utf8
import os
import sys
import shutil
from shutil import copyfile
import re

'''
string = "My name is NALIN Limit tos 1400 spaces, i.e., approximately 15 single-spaced typewritten I nes ta ra rum pum"

def pp_1(string):
    list1 = ['single-spaced','SINGLE-SPACED','Single-spaced','single-space']
    for i in list1:
        if i in string:
            index = string.find(i)
            string = string[0:index-44] + string[index+30:]
            #print(string[index:index+30])
            #print(string)
        else:
            continue
    return string 

print(string,pp_1(string))
'''

'''
def main(folder_1,folder_2):
	i = 0
	for filename in os.listdir(folder_1):
		#if filename.startswith('2000', 3, 7) or filename.startswith('2001', 3, 7) or filename.startswith('2002', 3, 7) or filename.startswith('2003', 3, 7) or filename.startswith('2004', 3, 7) or filename.startswith('2005', 3, 7) or filename.startswith('2006', 3, 7) or filename.startswith('2007', 3, 7) or filename.startswith('2008', 3, 7) or filename.startswith('2009', 3, 7) or filename.startswith('2010', 3, 7) or filename.startswith('2011', 3, 7) or filename.startswith('2012', 3, 7) or filename.startswith('2013', 3, 7) or filename.startswith('2014', 3, 7) or filename.startswith('2015', 3, 7) or filename.startswith('2016', 3, 7) or filename.startswith('2017', 3, 7) or filename.startswith('2018', 3, 7):
		#if filename.startswith('1985', 3, 7) or filename.startswith('1986', 3, 7) or filename.startswith('1987', 3, 7) or filename.startswith('1988', 3, 7) or filename.startswith('1989', 3, 7):
		if filename.startswith('1990', 3, 7) or filename.startswith('1991', 3, 7) or filename.startswith('1992', 3, 7) or filename.startswith('1993', 3, 7) or filename.startswith('1994', 3, 7):
		#if filename.startswith('1995', 3, 7) or filename.startswith('1996', 3, 7) or filename.startswith('1997', 3, 7) or filename.startswith('1998', 3, 7) or filename.startswith('1999', 3, 7):
			if filename.startswith('ML', 0, 2) == False:
				i += 1
				old = folder_1 + "/" + filename
				new = folder_2 + "/" + filename
				os.rename(old,new)
				print i
			else:
				continue  
		else:
			continue 

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])
'''

'''
def refiner(string):
    list_1 = string.split()
    list_2 = []
    list_3 = []
    #print list_1[1].isupper()
    #print list_1
    for i in list_1:
        #if "(" or ")" not in i:
        if i.isupper() == True:
            list_3.append(i)
        elif i.isdigit() == False and i.isalpha() == False:
            if i[-1] == ',' or i[-1] == '.':
                if i[0].isalpha() == True:
                    list_2.append(i)
                else:
                    list_3.append(i)
        else:
            list_2.append(i)
        #else:
        #   continue
    #print list_3
    output = " ".join(list_2)
    return output
'''

#string = '''SYSTEM 11. THIS REPORT IS SUBMITTED PURSUANT TO THE REQUIREMENTS OF 10 CFR§: (Check all that apply) • 20.2201(b)0.2201(d)• 20.2203(a)(1) • 20.2203(a)(2)(i)• 20.2203(a)(2)(ii) • 20.2203(a)(2)(iii)• 20.2203(a)(3)(i) • 50.73(a)(2)(i)(C) • 50.73(a)(2)(vii) • 20.2203(a)(3)(ii) 0 50.73(a)(2)(ii)(A) • 50.73(a)(2)(viii)(A) • 20.2203(a)(4) • 50.73(a)(2)(ii)(B) • 50.73(a)(2)(viii)(B) • 50.36(c)(1)(i)(A) • 50.73(a)(2)(iii) • 50.73(a)(2)(ix)(A) • 50.36(c)(1)(ii)(A) • 50.73(a)(2)(iv)(A) • 50.73(a)(2)(x) • 50.36(c)(2) • 50.73(a)(2)(v)(A) • 73.71(a)(4) • 20.2203(a)(2)(iv) • 50.46(a)(3)(ii) • 50.73(a)(2)(v)(B) • 73.71(a)(5) • 20.2203(a)(2)(v) • 50.73(a)(2)(i)(A) • 50.73(a)(2)(v)(C) • OTHER • 20.2203(a)(2)(vi) • 50.73(a)(2)(i)(B) • 50.73(a)(2)(v)(D) Specify in Abstract below or in NRC Form 366A 12.LICENSEE CONTACT FOR THIS LER TELEPHONE NUMBER (Include Area Code) 920/755-7793 13.COMPLETE ONE LINE FOR EACH COMPONENT FAILURE DESCRIBED IN THIS REPORT MANU REPORTABLE MANU REPORTABLECOMPONENT CAUSE SYSTEM COMPONENTFACTURER TO EPIX FACTURER TO EPIX 14.SUPPLEMENTAL REPORT EXPECTED 15. EXPECTED MONTH DAY YEAR SUBMISSION • YES (If yes, complete 15. EXPECTED SUBMISSION DATE) J NO DATE ABSTRACT (Limit   On October 25, 2007, at 1930 CDT Point Beach Nuclear Plant (PBNP) Unit 1 and Unit 2 low temperature overpressure protection (LTOP) systems were declared inoperable as a result of the determination that the current LTOP actuation setpoint was non-conservative based on new calculation information. Changes were made to operating procedures to delineate operation of reactor coolant pumps and charging pumps during low temperature conditions. These changes provided the guidance required to ensure that the current LTOP setpoints remain conservative. Operability of LTOP was restored for both Unit 1 and Unit 2 on October 26, 2007, at 1751 CDT upon issuance of the revised procedures. This issue was discovered as part of the ongoing '''


'''
def anchor_optimizer_checker(string):
	if string.count('(')>10 or string.count(')')>10 or string.count('5')>10 or string.count('•') >1:
		return True
	else:
		return False

'''
test = "1,AANUFACTuRER  To  , P!,  FACTuR ER EP1X N/A N/A N/A N/A N/A -4 '74, N/A N/A N/A N/A N/A 14.    0 YES (if yes. complete 15.   ) CE) NO 15,       ABSTRACT (Ltrrut  On February 19, 2014, it was determined that the Braidwood Generating Station has not complied with Technical Specifications (TS) 3.4.3, RCS Pressure and Temperature (P/T) s, between March 2011 and October 2013, during start-up of the plant following plant refueling outages. Braidwood TS 3.4.3 ing Condition for Operation (LCO) states that RCS pressure, RCS temperature, and RCS heatup and cooldown rates shall be maintained within the limits specified in the PTLR. During previous Reactor Coolant System (RCS) vacuum fill operations at Braidwood Station Unit 1 and Unit 2, RCS pressure exceeded the Pressure and Temperature s Report (PTLR) P/T curve lower bound in that the PfT curve does not indicate a limit below 0 psig. This TS non-compliance is reportable in accordance with 10 CFR 50.73(a)(2)(i)(B), Any operation or condition prohibited by the plants Technical Specifications. The cause of operation outside of the P/T curve limits is the application of an inadequate operating procedure that allowed the P/T lower pressure bound to be exceeded during RCS fill operations. RCS fill pressures below the PfT curve lower bound did not affect the integrity of the RCS system."

test2 = '''      N/A N/A N/A N/A N/A N/A N/A N/A N/A N/A 14.    q YES (If yes, complete 15.   ) 1 NO 15.       N/A N/A N/A ABSTRACT (   This report is submitted pursuant to the 30 day Special Report requirement of 10 CFR 50.46(a)(3)(ii). The guidance provided in NURGEG 1022, Revision 3, allows the reporting under 10 CFR 50.73 and 10 CFR 50.46 to be combined. On November 25, 2014, AREVA NP Inc. notified Entergy Operations, Inc. of a deficiency in the Arkansas Nuclear One, Unit 1 (ANO-1) Emergency Core Cooling System evaluation model.'''

test3 = '''  , 1     B BN ISV A415 Y 1 14.    • YES (If yes, complete 15.   ) 0 NO 15.  SUBM SSION     N/A ABSTRACT (   On February 9, 2011, LaSalle Unit 1 was in Mode 2 (Startup) following a forced outage. During a walkdown of the drywell, a steam leak was observed coming from the Reactor Core Isolation Cooling Steam Supply Inboard Isolation Bypass/Warm up Valve (1E51-F076), a normally-closed, one inch, motor operated valve. The leak was determined to be on the valve bonnet extension-to-bonnet upper seal weld. At 1804 hours, the leak was classified as Pressure Boundary Leakage, and Technical Specification (TS) 3.4.5 Condition C was entered. TS 3.4.5 Required Action C.1 and C.2 require that the unit be in Mode 3 within 12 hours and Mode 4 within 36 hours. On February 9, 2011, at 1830 hours, a plant shutdown of Unit 1 commenced. The unit entered Mode 3 at 2258 hours on February 9, and reached Mode 4 at 0353 hours on February 10, 2011. The seal weld was repaired, and the unit was restarted on February 10, 2011. The equipment apparent cause evaluation determined that the cause was due to a weld defect or discontinuity from the original weld construction (i.e., manufacturing, installation/construction errors, etc.) of the upper seal weld that propagated through wall as a result of system loading and conditions (i.e., high pressure steam) during normal plant operations.'''

test4 = '''     B AB ISV A391 Y 14.    q YES (If yes, complete 15.   ) x NO 15.      ABSTRACT (   On February 2, 2011, at 0533, the Unit 2 reactor automatically tripped from 98.3% power as a result of low flow in the "C" loop of the reactor coolant system (RCS). The plant responded to the reactor trip as designed. All three auxiliary feed water (AFW) pumps automatically initiated on low-low steam generator (SG) water level providing flow to the SGs. The AFW pumps were secured by 0613. At 1222, the reactor coolant pump for "C" loop was stopped. With no flow, compliance with Technical Specification (TS) 3.17.1 was not maintained and a 30 hour action statement to place the unit in a cold shutdown condition was entered in accordance with TS 3.0.1. A preliminary root cause evaluation (RCE) determined that the low flow condition in the "C" RCS loop resulted from a separation of a loop stop valve's disc assembly from the stem, which allowed the disc assembly to drop into the flow stream.'''

test5 = ''' .TO      B BQ PSP N/A Y N/A N/A N/A N/A N/A 14.    0 YES (If yes, complete 15.   ) 0 NO 15.  SUBM SSION     N/A N/A N/A ABSTRACT (   On February 25, 2011, dried boric acid was identified on a 1A safety injection (SI) pump discharge line. At 1830 hours, upon receipt of the non-destructive examination results indicating a potential pressure boundary leak, the lA SI train was declared inoperable, and Technical Specification ing Condition for Operation (LCO) 3.5.2, "Emergency Core Cooling Systems - Operating," Condition A was entered for one train inoperable. Following pipe replacement, on March 3, 2011, at 2028 hours, the system was returned to service and LCO 3.5.2 Condition A was exited. The apparent cause of the through wall crack is outside diameter (transgranular) stress corrosion cracking that initiated from the external surface of the pipe caused by chloride exposure. '''

test6 = ''' 1,AANUFACTuRER  To  , P!,  FACTuR ER EP1X N/A N/A N/A N/A N/A -4 '74, N/A N/A N/A N/A N/A 14.    0 YES (if yes. complete 15.   ) CE) NO 15,       ABSTRACT (Ltrrut  On February 19, 2014, it was determined that the Braidwood Generating Station has not complied with Technical Specifications (TS) 3.4.3, "RCS Pressure and Temperature (P/T) s," between March 2011 and October 2013, during start-up of the plant following plant refueling outages. Braidwood TS 3.4.3 ing Condition for Operation (LCO) states that "RCS pressure, RCS temperature, and RCS heatup and cooldown rates shall be maintained within the limits specified in the PTLR." During previous Reactor Coolant System (RCS) vacuum fill operations at Braidwood Station Unit 1 and Unit 2, RCS pressure exceeded the Pressure and Temperature s Report (PTLR) P/T curve lower bound in that the PfT curve does not indicate a limit below 0 psig. This TS non-compliance is reportable in accordance with 10 CFR 50.73(a)(2)(i)(B), "Any operation or condition prohibited by the plants Technical Specifications". The cause of operation outside of the P/T curve limits is the application of an inadequate operating procedure that allowed the P/T lower pressure bound to be exceeded during RCS fill operations. RCS fill pressures below the PfT curve lower bound did not affect the integrity of the RCS system.'''

test7 = '''       N/A N/A N/A N/A N/A D FK RLY27 GE Y 14.    q YES (If yes, complete 15.   ) 4 NO 15.  IONMISS SUB    ABSTRACT (   On January 17, 2014, while operating at 100% power, Standby Transformer 1X4 Under voltage Relay 127/SB2 failed to meet requirements of Surveillance Test Procedure (STP) 3.3.8.1-05B, 1A4 4KV Emergency Transformer Supply Under voltage Calibration. Two relay trip circuit contacts were found to be incorrectly configured such that the relay could not perform the intended function to actuate on loss-of-voltage to trip the Standby Transformer supply breaker. A past operability review determined that the relay had been inoperable for 120 days, 8 hours and 5 minutes. The relay is required to be operable in Modes 1, 2, and 3, and when the associated "B" Emergency Diesel Generator is required to be operable by ing Condition for Operation (LCO) 3.8.2, AC Sources-Shutdown. The event resulted in a condition prohibited by Technical Specifications and is reportable pursuant to 10CFR50.73(a)(2)(i)(B). The safety significance is minimized due to the fact that degraded voltage relays perform a similar function and would trip the Standby Transformer supply breaker to allow the "B" Emergency Diesel Generator to carry essential loads during a Loss-of-Offsite-Power. The root cause of this event was inadequate procedural guidance for both preplanned maintenance and post maintenance testing. This event did not result in a safety system functional failure. There were no radiological releases associated with this event.'''
'''
def reg_ex(extracted,list):
	extracted = re.search( r'.* (.*?) N/A', extracted)
	list.append(extracted.group())
	return list

list1 = []
list1 = reg_ex(test,list1)
list1 = reg_ex(test2,list1)
'''

def reg_ex(extracted):
	#extracted = re.sub( r'.* (.*?) N/A', "", extracted)
	extracted = re.sub( r'.* (.*?) ABSTRACT ', "", extracted)
	return extracted
print(reg_ex(test7))
