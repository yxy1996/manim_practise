from manimlib.imports import *
import os
import pyclbr
import random
import math
from manimlib.scene.zoomed_scene import *

# load a picture
class whatisfingerpris2(Scene):
    CONFIG={
        "plane_kwargs" : {
        "color" : RED
        },
        "camera_config":{"background_color":WHITE},
        # rotating to update points' states, and it is not neccessary that their states correspond to the rotation.
        "point_rotation_angle_axis_pairs": [
            (35 * DEGREES, rotate_vector(RIGHT, 30 * DEGREES)),
        ]
    }
    def construct(self):
        img = ImageMobject('wifi signal.png')
        img.scale(4)  
        img.shift(3.2* LEFT) 

        tex_qitashuoming = Paragraph(
        "MAC1             \t1",
        "MAC2             \t2",
        "B0:F9:63:91:FB:F1\t3",
        "48:8A:D2:C4:D6:10\t4",
        "B0:D5:9D:FE:4D:D6\t5",
        )
        
        # consistant with one of the elements' color in wifi signal.png.  (red)
        tex_qitashuoming.set_color("#C00000")
        tex_qitashuoming.set_all_lines_alignments("right")
        tex_qitashuoming.scale(0.8)
        tex_qitashuoming.to_edge(RIGHT)
        tex_qitashuoming.shift(1.5*UP)
        
       
        rect = SurroundingRectangle(tex_qitashuoming)
        rect.set_color("#C00000")
        
        # moving rect generated from the position of the 5th row of paragraph, and is moved to the 3th row of paragraph
        rec_paragraph = SurroundingRectangle(tex_qitashuoming[4])
        rec_paragraph.set_color("#C00000")
        rec_paragraph.shift((tex_qitashuoming[2].get_center()[1]-tex_qitashuoming[4].get_center()[1])*UP)

        shuoming_tex = TextMobject("\\che{MAC Mappings}")
        shuoming_tex.scale(0.9)
        shuoming_tex.next_to(rect,0.8*UP)
        shuoming_tex.set_color("#C00000")
        
        # consistant with one of the elements' color in wifi signal.png. (blue)
        # normalization wifi fingerprints.
        decimals = VGroup(*[
            DecimalNumber(
                0.085,
                num_decimal_places=3,
                color="#0070C0",
                include_sign=False,
                edge_to_fix=RIGHT,
            ),
             DecimalNumber(
                0.071,
                num_decimal_places=3,
                color="#0070C0",
                include_sign=False,
                edge_to_fix=RIGHT,
            ),
            DecimalNumber(
                0.563,
                num_decimal_places=3,
                color="#0070C0",
                include_sign=False,
                edge_to_fix=RIGHT,
            ),
            DecimalNumber(
                0.4,
                num_decimal_places=3,
                color="#0070C0",
                include_sign=False,
                edge_to_fix=RIGHT,
            ),
            DecimalNumber(
                0.413,
                num_decimal_places=3,
                color="#0070C0",
                include_sign=False,
                edge_to_fix=RIGHT,
            )
        ])

        number_label = VGroup(
            decimals[0],
            decimals[1],
            decimals[2],
            decimals[3],
            decimals[4],
        )
        number_label.scale(0.6)
        number_label.arrange(RIGHT)
        number_label.move_to(rect,DOWN)
        number_label.shift(2.5*DOWN)

        tex_pre = Paragraph("New WiFi sensory data received")
        tex_pre.set_color("#C00000")
        tex_pre.scale(0.8)
        tex_pre.to_edge(LEFT)
        
        rect1 = SurroundingRectangle(number_label[2])
        rect2 = SurroundingRectangle(number_label[3])
        rect3 = SurroundingRectangle(number_label[4])
        rect4 = SurroundingRectangle(number_label[1])
        rect5 = SurroundingRectangle(number_label[0])

        rect1.set_color("#0070C0")
        rect2.set_color("#0070C0")
        rect3.set_color("#0070C0")
        rect4.set_color("#0070C0")
        rect5.set_color("#0070C0")
       
        tex_above_rect = TextMobject("\\che{WiFi Fingerprint}")
        tex_above_rect.scale(0.9)
        tex_above_rect.next_to(rect1,0.8*UP)
        tex_above_rect.set_color("#0070C0")

        dicimal_rects = VGroup(rect1,rect2,rect3,rect4,rect5)

        point = VectorizedPoint(OUT)

        def generate_decimal_updater(decimal, index):
            #shifted_i = (index - 1) % 3
            decimal.add_updater(lambda d: d.set_value(
                abs(random.randint(0,1000))/1000
            ))
            return decimal
   
        self.add(rect,shuoming_tex,tex_qitashuoming[:2],tex_above_rect)  # Display the image
        #self.play(FadeOut(img))
        self.play(FadeIn(tex_pre))
        self.wait(0.5)
        self.play(FadeOut(tex_pre))
        self.play(FadeIn(img))
        self.wait(0.5)
        self.play(Write(tex_qitashuoming[2:]))

        rect_copy = rect.copy()
        self.wait(0.5)
        self.play(Transform(rect_copy,dicimal_rects))   
        
        # raw wifi fingerprint
        decimals_fake = VGroup(*[
            DecimalNumber(
                -45,
                num_decimal_places=0,
                color="#0070C0",
                include_sign=False,
                edge_to_fix=RIGHT,
            ),
            DecimalNumber(
                -58,
                num_decimal_places=0,
                color="#0070C0",
                include_sign=False,
                edge_to_fix=RIGHT,
            ),
            DecimalNumber(
                -57,
                num_decimal_places=0,
                color="#0070C0",
                include_sign=False,
                edge_to_fix=RIGHT,
            )
        ])
        number_label_fake = VGroup(
            decimals_fake[0],
            decimals_fake[1],
            decimals_fake[2],
        )
        number_label_fake.scale(0.6)
        number_label_fake.arrange(RIGHT,buff=(rect2.get_center()[0] - rect1.get_center()[0])/2)
        number_label_fake.move_to(number_label[2:])


        rectangle = Rectangle(height=2.66, width=8.5)
        rectangle.set_color("#C00000")
        rectangle.to_edge(UP+LEFT)
        rectangle.shift(0.5*LEFT + 0.5*UP)

        more_aps = TexMobject("\\cdots")
        more_aps.next_to(number_label,1.2*DOWN)
        more_aps.scale(0.8)
        more_aps.set_color("#0070C0")

        self.play(ShowCreation(rectangle),ShowCreation(rec_paragraph))
        self.play(Write(number_label_fake[0]))
        self.play(ApplyMethod(rectangle.shift,2.66*DOWN),ApplyMethod(rec_paragraph.shift,(tex_qitashuoming[3].get_center()[1]-tex_qitashuoming[2].get_center()[1])*UP))
        self.play(Write(number_label_fake[1]))
        self.play(ApplyMethod(rectangle.shift,2.66*DOWN),ApplyMethod(rec_paragraph.shift,(tex_qitashuoming[4].get_center()[1]-tex_qitashuoming[3].get_center()[1])*UP))
        self.play(Write(number_label_fake[2]))
        self.play(FadeOut(rectangle),FadeOut(rec_paragraph))

        self.play(Transform(number_label_fake,number_label[2:]))
        self.wait(0.5)
        self.play(Write(number_label[:2]),ShowCreation(more_aps))

        self.add(number_label[2:])
        self.remove(number_label_fake)
        self.wait(1.5)
        for i, decimal in enumerate(decimals):
            self.add(generate_decimal_updater(decimal, i))

        pairs = self.point_rotation_angle_axis_pairs
        
        # each time the angle changes, the 3 dimensions of points change randomly in range of [0.000,1.000]
        for angle, axis in pairs:
            self.play(
                Rotate(point, angle, axis=axis, about_point=ORIGIN),
                run_time=2
            )
            self.wait()



class EFieldInThreeD(ThreeDScene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)

    def construct(self):
        # 2d part
        plane = NumberPlane(**self.plane_kwargs) #Create axes and grid
        plane.add(plane.get_axis_labels())  #add x and y label
        self.add(plane)  #Place grid on screen
        vec_field = []  #Empty list to use in for loop
        draw_field = VGroup(*vec_field)   #Pass list of vectors to create a VGroup

        square=Square(side_length=1,fill_color=YELLOW, fill_opacity=1)
        square.move_to(0.5*(LEFT+UP))
        squarelist = []

        forlist = [-1,1]
        for i in forlist:
            square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.5)
            square.move_to((i+0.5)*(LEFT+UP))
            squarelist.append(square)
        for i in forlist:
            square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.5)
            square.move_to((i-0.5)*(RIGHT+UP)+UP)
            squarelist.append(square)
        for i in forlist:
            square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.5)
            square.move_to((0.5+i)*UP+0.5*LEFT)
            squarelist.append(square)
        for i in forlist:
            square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.5)
            square.move_to((i)*RIGHT+0.5*(LEFT+UP))
            squarelist.append(square)
        square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.8)
        square.move_to(0.5*(LEFT+UP))
        squarelist.append(square)
        field = 0.5*RIGHT + 0.5*UP   #Constant field up and to right
   
        result = Circle(fill_color=YELLOW, fill_opacity=1, color=YELLOW)
        result.scale(0.1)
        result.move_to(0.5*(LEFT+UP))
        self.add(result)

        draw_field = VGroup(*squarelist)
     
        eq0 = TextMobject("$\\mathbf{(\\mu^*_1,\\sigma^*_1)}$")
        eq0.scale(2)
        eq0.to_edge(UP)
        eq0.shift(1*DOWN)
        eq0.set_color(BLUE)

        eq1 = TextMobject("$\\mathbf{(\\mu^*_1,\\sigma^*_1),(\\mu^*_2,\\sigma^*_2),\\cdots,(\\mu^*_9,\\sigma^*_9)}$")
        eq1.scale(2)
        eq1.to_edge(UP)
        eq1.shift(1*DOWN)
        eq1.set_color(BLUE)

        eq2 = TextMobject("$\\mathbf{(\\mu^*_s,\\sigma^*_s)}$")
        eq2.scale(2)
        eq2.shift(1.5*DOWN)
        eq2.set_color(YELLOW)
        self.add_foreground_mobjects(result ) 

        self.play(GrowFromCenter(draw_field),rate = 5)
        self.play(ApplyMethod(draw_field.shift,UP),ApplyMethod(result.shift,UP+0.1*RIGHT))
        self.play(ApplyMethod(draw_field.shift,RIGHT),ApplyMethod(result.shift,RIGHT+0.1*DOWN))
        self.play(ApplyMethod(draw_field.shift,2*DOWN),ApplyMethod(result.shift,2*DOWN+0.1*DOWN))
        self.play(ApplyMethod(draw_field.shift,RIGHT),ApplyMethod(result.shift,RIGHT+0.1*LEFT))
        self.play(ApplyMethod(draw_field.shift,DOWN),ApplyMethod(result.shift,DOWN+0.05*LEFT))
        self.play(ApplyMethod(draw_field.shift,2*RIGHT),ApplyMethod(result.shift,2*RIGHT+0.1*UP))
        self.play(FadeOut(plane))
        self.play(Transform(squarelist[1],eq0))
        self.wait(1)
        self.play(Transform(squarelist[1],eq1))
        self.wait(1)
        self.play(Transform(squarelist[1],eq2)) 
        self.wait(1)

        # 3d part
        self.remove(squarelist[1],draw_field,result)
        axes = ThreeDAxes()

        plane = NumberPlane(**self.plane_kwargs)
        self.add(plane)
        #plane.main_lines.fade(.9)   #Doesn't work in most recent commit
        a = plane.get_axis_labels()[0]
        a.next_to([5,0,0],DOWN)
        b = plane.get_axis_labels()[1]
        b.next_to([0,5,0],LEFT)
        c = TexMobject("Probability")
        c.next_to([0,0,3],LEFT)
        c.rotate(TAU/4,[1,0,0])
        self.add(a)
        self.add(b)
        self.add(c)

        axes.get_axis_labels()
        squarelist = []
        forlist = [-1,1]

        square3=Square(side_length=1,fill_color=YELLOW, fill_opacity=1)
        square3.move_to(0.5*(LEFT+UP))

        for i in forlist:
            square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.5)
            square.move_to((i+0.5)*(LEFT+UP))
            squarelist.append(square)
        for i in forlist:
            square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.5)
            square.move_to((i-0.5)*(RIGHT+UP)+UP)
            squarelist.append(square)
        for i in forlist:
            square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.5)
            square.move_to((0.5+i)*UP+0.5*LEFT)
            squarelist.append(square)
        for i in forlist:
            square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.5)
            square.move_to((i)*RIGHT+0.5*(LEFT+UP))
            squarelist.append(square)
        square=Square(side_length=1,fill_color=BLUE, fill_opacity=0.8)
        square.move_to(0.5*(LEFT+UP))
        squarelist.append(square)
        square_12  = VGroup(*squarelist)

        self.add(square_12)

        plateau = ParametricSurface(
            lambda u, v: np.array([
                v,
                u,
                0
            ]),v_max=2,u_max=2,v_min=-1,u_min=-1,fill_opacity=0.1,
            checkerboard_colors=[RED_D, RED_E],
            resolution=(5, 5)).scale(2)

        plateau2 = ParametricSurface(
            lambda u, v: np.array([
                v,
                u,
                0
            ]),v_max=2,u_max=2,v_min=-1,u_min=-1,fill_opacity=0.1,
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(5, 5)).scale(2)

        plateau3 = ParametricSurface(
            lambda u, v: np.array([
                v,
                u,
                0
            ]),v_max=2,u_max=2,v_min=-1,u_min=-1,fill_opacity=2.,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(5, 5)).scale(2)

        
        paraboloid_12 = ParametricSurface(
            lambda u, v: np.array([
                v ,
                u,
                0.8*13/(2*3.14)*np.exp(-((v-17/26)**2*13+(u-11/13)**2*13) )
            ]),v_max=2,u_max=2,v_min=-1,u_min=-1,fill_opacity=2.,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(40, 40 )).scale(2)
        dis = paraboloid_12.get_center()[2]
        paraboloid_12.shift([0.,0.,dis])



        paraboloid_1 = ParametricSurface(
            lambda u, v: np.array([
                v,
                u,
                0.8*3/3.14*np.exp(-((v-1)**2*4+(u-1)**2*9))
            ]),v_max=2,u_max=2,v_min=-1,u_min=-1,fill_opacity=2.,
            checkerboard_colors=[RED_D, RED_E],
            resolution=(23, 23 )).scale(2)

        dis = paraboloid_1.get_center()[2]
        paraboloid_1.shift([0.,0.,dis])

        paraboloid_2 = ParametricSurface(
            lambda u, v: np.array([
                v ,
                u,
                0.8*3/3.14*np.exp(-((v-0.5)**2*9+(u-0.5)**2*4))
            ]),v_max=2,u_max=2,v_min=-1,u_min=-1,fill_opacity=2.,
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(23, 23 )).scale(2)

        dis = paraboloid_2.get_center()[2]
        paraboloid_2.shift([0.,0.,dis])

        para_list = []
        para_list.append(plateau)
        para_list.append(plateau2)
        para = VGroup(*para_list)

        self.set_camera_orientation(phi=60* DEGREES, theta= -90*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.add(axes)

        self.wait(1)
        #self.play(Write(plateau))
        #self.play(Transform(plateau,paraboloid),rate=5)
        self.play((ApplyMethod(square_12.shift,[0.,0.,-3.5])),FadeOut(plane))
        self.play(Transform(squarelist[0],plateau))
        self.add(plateau)
        self.remove(squarelist[0])
        self.play(Transform(plateau,paraboloid_1))
        self.play(Transform(squarelist[1],plateau2))
        self.add(plateau2)
        self.remove(squarelist[1])
        self.play(Transform(plateau2,paraboloid_2))
        self.wait(1)
        self.play(Transform(plateau2,paraboloid_12),Transform(plateau,paraboloid_12))
        self.wait(1)
       


HEAD_INDEX   = 0
BODY_INDEX   = 1
ARMS_INDEX   = 2
LEGS_INDEX   = 3

if __name__ == "__main__":
    # Call this file at command line to make sure all scenes work with version of manim
    # type "python manim_tutorial_P37.py" at command line to run all scenes in this file
    #Must have "import os" and  "import pyclbr" at start of file to use this
    ###Using Python class browser to determine which classes are defined in this file
    module_name = 'manim_tutorial_P37'   #Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module==module_name:
            print(item.name)
            os.system("python -m manim manim_tutorial_P37.py %s -l" % item.name)  #Does not play files

