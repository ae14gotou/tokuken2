#-*- coding: utf-8 -*-
#確率的アルゴリズム:AntTree_STOCH
class Ant():
    def __init__(self, data, Id, pos, code=0):
        self.data = data
        self.a_plus = 0
        self.a_pos = pos
        self.Tsim = 1.0
        self.Tdsim = 0.0
        self.parent = []
        self.children = []
        self.Id = Id
        self.conect = False
        self.label = -1
        self.code = code

    def set_parent(self, P):
        self.parent.append(P)
        self.conect = True

    def set_children(self, Lmax, child):
        if len(self.children) < Lmax:
            self.children.append(child)

    def set_plus(self, Id):
        self.a_plus = Id

    def set_pos(self, pos):
        self.a_pos = pos

    def set_label(self, label):
        self.label = label

    def dec_Tsim(self, alpha1):
        self.Tsim = self.Tsim * alpha1

    def inc_Tdsim(self, alpha2):
        self.Tdsim = self.Tdsim + alpha2

#決定論的アルゴリズム:AntTree_NO-THRESHOLDS
class d_Ant(Ant):   #Antクラスの継承
    first = True #初回の試行かどうか
    def fin_first(self):
        self.first = False
        
    def set_Tdsim(self, Td):
        self.Tdsim = Td

    def change_conect(self):
        self.conect = not self.conect

    def disconect(self):
        self.parent.pop()
        self.set_pos(0)
        self.set_plus(0)
        self.change_conect()

    def rm_children(self, i):
        self.children.remove(i)
        
