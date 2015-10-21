
###############################################################
# 
#              AUTORS
#
#       Moscato Giuseppe aka peppeska <moscatog@yahoo.it>
# 
#       Altamore Giovanni <zzuncu@hotmail.com>
# 
# 
# 
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
# 
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
# 
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
# 
###############################################################

import serial,array,time
import string
import pango

class xbee_lib():

	def __initi__(self,port,baudrate,bytesize,parity,stopbits):
		self.ser=serial.Serial(port,baudrate,bytesize,parity,stopbits)

	# questa funzione legge tutti gli ingressi della porta A e restituisce un array (la dimensione dell'array e' specificata nel user manual della MuIn)
	# esempio array = [@,A,ch1,ch1,space,space,ch2,ch2,space,space,ch3,ch3,space,space,ch4,ch4,space,space,ch5,ch5,#]
	def read_ADC(self):
                ######### ADC ##########

		# stringa per lettura da canali ADC della porta A
                com_str_tosend="@A00000#"
                
                self.ser.write(com_str_tosend)
                   
                print "ADC: "
                time.sleep(2)
                output = []
                while self.ser.inWaiting():
                    output.append(self.ser.read())
                print output

		return output


        # funzione per la trasmissione dei comandi AT via seriale
        def send_AT(self,com_str_tosend):

		#com_str_tosend=self.entry_at.get_text()

		if com_str_tosend == '+++':
			self.ser.write(com_str_tosend)
	        else:
        		self.ser.write('%s\r' % com_str_tosend)

		print "AT: "
		time.sleep(2)
		output = []
		while self.ser.inWaiting():
			output.append(self.ser.read())
		print output

		return output



