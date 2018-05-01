import xlrd
from pygame import mixer as mx
from tkinter import *



class Teacher:
    def __init__(self, info):
        self.name = info[0].value
        self.course_num = info[1].value
        self.course_name = info[2].value
        self.grade = info[4].value
        self.rank = info[5].value
        self.avg = info[3].value



class Page:
    def __init__(self, course):
        self.name = course
        self.teachers = [0, 0, 0, 0, 0, 0]


class Buttons:
    def __init__(self):
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0




class my_gui(Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.pages = {}
        # self.upload_data()
        self.canvas = Canvas(self)
        self.my_images = []
        self.image_on_canvas = ""
        self.main_screen = True
        self.cur_screen = ""
        self.sound_x_1 = mx.Sound("40 BPM Metronome.ogg")
        self.sound_x_2 = mx.Sound("60 BPM Metronome.ogg")
        self.sound_x_3 = mx.Sound("80 BPM Metronome.ogg")
        self.sound_x_4 = mx.Sound("100 BPM Metronome.ogg")
        self.sound_x_5 = mx.Sound("120 BPM Metronome.ogg")
        self.sound_x_6 = mx.Sound("140 BPM Metronome.ogg")
        self.sound_y_1 = mx.Sound(
            "40 BPM - Simple Straight Beat - Drum Track.ogg")
        self.sound_y_2 = mx.Sound(
            "60 BPM - Simple Straight Beat - Drum Track.ogg")
        self.sound_y_3 = mx.Sound(
            "80 BPM - Simple Straight Beat - Drum Track.ogg")
        self.sound_y_4 = mx.Sound(
            "100 BPM Drum Track  Loop  Metronome.ogg")
        self.sound_y_5 = mx.Sound(
            "120 BPM Drum Track  Loop  Metronome.ogg")
        self.sound_y_6 = mx.Sound(
            "140 BPM - Simple Straight Beat - Drum Track.ogg")
        self.set_volumes()
        self.play_sounds()
        self.cur_sound_x = self.init_sound_x()
        self.cur_sound_y = self.init_sound_y()
        self.initUI()

    def initUI(self):
        self.master.title("The True Teacher's Rank")
        self.pack(fill=BOTH, expand=1)
        self.my_images.append(PhotoImage(file="graph eyal final.png"))
        self.my_images.append(PhotoImage(file="teachers algo.png"))
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor=NW,
                                                        image=self.my_images[
                                                            0])
        self.canvas.pack(fill=BOTH, expand=1)
        self.master.geometry("{0}x{1}+0+0".format(1229, 691))
        root.bind('<Motion>', self.motion)
        # root.bind("<Button-1>", self.readPos)
        self.master.mainloop()

    def motion(self, event):

        print(event.x, event.y)
        mx.init()
        a, b, c, d, e, f, g, h, i, j, k, l = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        rate = (event.y - 105)/ 475
        if (event.y > 105 and event.y < 580) and (
                event.x > 103 and event.x < 1090):
            if event.x < 267:
                a = rate
                b = 1-rate
            elif event.x < 431:
                c = rate
                d = 1 - rate
            elif event.x < 595:
                e = rate
                f = 1 - rate
            elif event.x < 759:
                g = rate
                h = 1 - rate
            elif event.x < 923:
                i = rate
                j = 1 - rate
            else:
                k = rate
                l = 1 - rate

        self.sound_x_1.set_volume(a)
        self.sound_x_2.set_volume(c)
        self.sound_x_3.set_volume(e)
        self.sound_x_4.set_volume(g)
        self.sound_x_5.set_volume(i)
        self.sound_x_6.set_volume(k)
        self.sound_y_1.set_volume(b)
        self.sound_y_2.set_volume(d)
        self.sound_y_3.set_volume(f)
        self.sound_y_4.set_volume(h)
        self.sound_y_5.set_volume(j)
        self.sound_y_6.set_volume(l)





    def upload_data(self):
        file = xlrd.open_workbook("Seker.xlsx")
        worksheet = file.sheet_by_index(0)
        num_of_teachers = int(worksheet.cell(0, 0).value)
        cur_course = Page(worksheet.cell(2, 2).value)

        for i in range(num_of_teachers):
            if worksheet.cell(i + 2, 2).value == cur_course.name:
                new_teacher = Teacher(worksheet.row(i + 2))
                cur_course.teachers[
                    int(worksheet.cell(i + 2, 6).value)] = new_teacher
            else:
                self.pages[cur_course.name] = cur_course
                cur_course = Page(worksheet.cell(i + 2, 2).value)
                new_teacher = Teacher(worksheet.row(i + 2))
                cur_course.teachers[int(
                    worksheet.cell(i + 2, 6).value)] = new_teacher
        self.pages[cur_course.name] = cur_course

    def init_sound_x(self):
        pass

    def init_sound_y(self):
        return mx.Sound("Hip Hop Drumless Backing Track Metronome Version.wav")

    def play_sounds(self):
        self.sound_x_1.play(loops=-1)
        self.sound_x_2.play(loops=-1)
        self.sound_x_3.play(loops=-1)
        self.sound_x_4.play(loops=-1)
        self.sound_x_5.play(loops=-1)
        self.sound_x_6.play(loops=-1)
        self.sound_y_1.play(loops=-1)
        self.sound_y_2.play(loops=-1)
        self.sound_y_3.play(loops=-1)
        self.sound_y_4.play(loops=-1)
        self.sound_y_5.play(loops=-1)
        self.sound_y_6.play(loops=-1)

    def set_volumes(self):
        self.sound_x_1.set_volume(0)
        self.sound_x_2.set_volume(0)
        self.sound_x_3.set_volume(0)
        self.sound_x_4.set_volume(0)
        self.sound_x_5.set_volume(0)
        self.sound_x_6.set_volume(0)
        self.sound_y_1.set_volume(0)
        self.sound_y_2.set_volume(0)
        self.sound_y_3.set_volume(0)
        self.sound_y_4.set_volume(0)
        self.sound_y_5.set_volume(0)
        self.sound_y_6.set_volume(0)


root = Tk()
mx.init()
mx.set_num_channels(12)
ex = my_gui(root)
