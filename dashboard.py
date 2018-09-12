'''
project : electric dashboard for a car ( mechanical department graduation project for rally competition )
by : abdullah abunar
requirements : tkinter
'''

from tkinter import *

class dashboard:

	def __init__(self, master):
		
		self.master = master
		self._create_GUI()
		
		# speed pointer related variables
		self.counter = 0
		self.speed_pointer_center = (223, 250)
		self.speed_pixels = [105, 314, 103, 312, 101, 309, 99, 307, 98, 304, 96, 300, 95, 297, 94, 295, 94, 291, 93, 288, 93, 285, 93, 282,
							 93, 280, 93, 278, 93, 276, 92, 274, 92, 269, 92, 267, 91, 264, 91, 262, 92, 258, 93, 255, 93, 253, 94, 248,
							 93, 246, 93, 243, 93, 240, 93, 237, 94, 233, 94, 231, 95, 228, 95, 226, 95, 225, 96, 223, 96, 219, 96, 217,
							 97, 215, 97, 213, 98, 211, 98, 209, 99, 206, 101, 204, 101, 201, 102, 200, 102, 199, 104, 196, 105, 192,
							 106, 192, 107, 191, 107, 189, 109, 187, 109, 185, 110, 182, 111, 181, 112, 179, 114, 176, 116, 174, 117, 172,
							 120, 166, 122, 164, 123, 161, 125, 160, 127, 155, 131, 153, 132, 152, 133, 151, 135, 150, 137, 148, 139, 146,
							 140, 146, 144, 144, 143, 145, 145, 143, 146, 142, 148, 140, 151, 139, 154, 138, 155, 137, 156, 136, 159, 134,
							 161, 133, 163, 132, 167, 130, 170, 127, 171, 127, 173, 126, 175, 124, 178, 122, 181, 122, 183, 122, 186, 120,
							 187, 120, 188, 119, 192, 118, 195, 118, 199, 118, 200, 118, 202, 118, 204, 118, 208, 118, 209, 118, 210, 118,
							 211, 118, 213, 118, 216, 117, 222, 117, 223, 117, 224, 117, 227, 118, 229, 118, 232, 119, 235, 119, 237, 119,
							 240, 117, 242, 118, 245, 120, 249, 120, 251, 121, 252, 121, 255, 121, 256, 121, 259, 122, 260, 123, 261, 123,
							 263, 123, 266, 126, 268, 126, 269, 126, 270, 127, 272, 127, 274, 129, 276, 130, 280, 132, 282, 134, 283, 136,
							 287, 137, 289, 139, 289, 141, 292, 144, 295, 145, 296, 145, 297, 147, 299, 149, 301, 149, 303, 152, 306, 153,
							 310, 155, 311, 158, 313, 160, 313, 163, 316, 164, 319, 166, 320, 167, 323, 168, 324, 171, 326, 174, 327, 175,
							 328, 178, 329, 183, 330, 186, 330, 189, 331, 192, 332, 194, 333, 196, 333, 198, 334, 200, 335, 203, 336, 204,
							 336, 206, 338, 207, 338, 208, 340, 212, 340, 217, 341, 221, 341, 224, 342, 228, 342, 232, 342, 235, 340, 241,
							 340, 244, 340, 248, 338, 251, 338, 252, 338, 255, 337, 261, 336, 264, 336, 267, 336, 270, 335, 272, 335, 275,
							 334, 277, 332, 281, 331, 286, 329, 290, 327, 296, 326, 299, 324, 305, 322, 310, 321, 310, 320, 311, 320, 313,
							 316, 318, 315, 322, 313, 324, 310, 327, 308, 331, 305, 335, 300, 338]
		self.max_speed = len(self.speed_pixels)
							 
		# RPM pointer related variables
		self.counter2 = 0
		self.rpm_pointer_center = (661, 249)
		self.rpm_pixels = [570, 336, 568, 334, 566, 332, 564, 330, 564, 329, 563, 328, 562, 327, 561, 326, 560, 323, 559, 321, 557, 319, 556,
						   317, 554, 315, 554, 314, 553, 312, 552, 310, 551, 308, 550, 306, 549, 305, 549, 303, 547, 302, 546, 300, 546, 298,
						   545, 297, 544, 296, 544, 294, 544, 293, 544, 292, 542, 289, 542, 285, 542, 282, 541, 281, 539, 278, 539, 277, 539,
						   273, 539, 272, 539, 269, 539, 266, 539, 264, 537, 262, 537, 259, 538, 257, 538, 254, 539, 250, 539, 248, 539, 245,
						   539, 241, 539, 238, 539, 233, 539, 229, 539, 224, 542, 220, 542, 216, 542, 211, 544, 207, 546, 203, 548, 198, 550,
						   196, 551, 195, 551, 194, 551, 191, 553, 188, 555, 185, 556, 183, 558, 180, 560, 177, 562, 173, 565, 169, 568, 167,
						   570, 165, 572, 161, 574, 159, 578, 155, 580, 154, 583, 152, 586, 150, 588, 148, 590, 146, 592, 144, 596, 142, 598,
						   141, 602, 138, 605, 137, 609, 135, 612, 135, 613, 134, 617, 132, 620, 130, 621, 130, 625, 129, 627, 128, 629, 128,
						   632, 127, 634, 126, 636, 126, 639, 126, 641, 126, 642, 125, 643, 125, 645, 125, 647, 124, 649, 124, 651, 124, 653,
						   124, 654, 124, 656, 124, 658, 124, 662, 125, 666, 124, 667, 124, 668, 124, 670, 124, 672, 124, 674, 125, 676, 125,
						   679, 126, 682, 127, 686, 127, 688, 128, 692, 129, 696, 131, 699, 131, 704, 133, 709, 135, 712, 137, 715, 140, 720,
						   142, 723, 143, 727, 143, 730, 145, 734, 148, 739, 151, 742, 154, 744, 156, 746, 158, 748, 160, 752, 162, 754, 165,
						   756, 169, 757, 171, 760, 173, 761, 175, 762, 177, 764, 179, 765, 180, 766, 182, 768, 185, 771, 188, 771, 192, 772,
						   194, 774, 201, 775, 202, 776, 205, 777, 209, 780, 210, 781, 212, 781, 214 ]
		self.max_rpm = len(self.rpm_pixels)
		
	def _create_GUI(self):
		'''
			creates the canvas, the background photo, pointer and gas tank indicator.
		'''
		
		self.master.title('Dashboard')
		self.master.resizable(False, False)
		
		# canvas configurations
		self.canvas = Canvas(self.master)
		self.canvas.config(width = 892, height = 502)
		self.canvas.config(background = 'black')
		self.canvas.pack()
		
		# dashboard ready image
		self.photo = PhotoImage(file = "dashboard.png")
		self.image = self.canvas.create_image(446, 251, image = self.photo)
		
		# speed pointer
		self.pointer = self.canvas.create_line(107, 314, 223, 250, fill = 'white', width = 2)
		
		# RPM pointer
		self.rpm_pointer = self.canvas.create_line(570, 336, 661, 249, fill = 'white', width = 2)
				
		# temperory buttons instead of the motor feedback
		Button(self.master, text = 'Speed up', command = self._speed_up).pack()
		Button(self.master, text = 'Speed down', command = self._speed_down).pack()
		Button(self.master, text = 'RPM up', command = self._speed_up2).pack()
		Button(self.master, text = 'RPM down', command = self._speed_down2).pack()
		
	def _speed_up(self):
		'''
			simulates the pushing on gas pedal
		'''
		
		pix1 = self.speed_pixels[self.counter]
		pix2 = self.speed_pixels[self.counter + 1]
		
		if (self.counter > self.max_speed): pass			# end point
		else:
			print(pix1, pix2)
			self.canvas.coords(self.pointer, pix1, pix2 , self.speed_pointer_center[0], self.speed_pointer_center[1])
			self.counter += 2
			
	def _speed_up2(self):
		'''
			simulates the pushing on gas pedal
		'''
		
		pix1 = self.rpm_pixels[self.counter2]
		pix2 = self.rpm_pixels[self.counter2 + 1]
		
		if (self.counter2 > self.max_rpm): pass			# end point
		else:
			print(pix1, pix2)
			self.canvas.coords(self.rpm_pointer, pix1, pix2 , self.rpm_pointer_center[0], self.rpm_pointer_center[1])
			self.counter2 += 2
			
	def _speed_down(self):
		'''
			simulates the letting go of the gas pedal
		'''
		
		pix1 = self.speed_pixels[self.counter]
		pix2 = self.speed_pixels[self.counter + 1]
		
		if (self.counter == 0): pass			# start point
		else:
			print(pix1, pix2)
			self.canvas.coords(self.pointer, pix1, pix2 , self.speed_pointer_center[0], self.speed_pointer_center[1])
			self.counter -= 2
		
	def _speed_down2(self):
		'''
			simulates the letting go of the gas pedal
		'''
		
		pix1 = self.rpm_pixels[self.counter2]
		pix2 = self.rpm_pixels[self.counter2 + 1]
		
		if (self.counter2 == 0): pass			# start point
		else:
			print(pix1, pix2)
			self.canvas.coords(self.rpm_pointer, pix1, pix2, self.rpm_pointer_center[0], self.rpm_pointer_center[1])
			self.counter2 -= 2
		
def main():
	
	root = Tk()
	App = dashboard(root)
	root.mainloop()
	
if __name__ == '__main__': main()
