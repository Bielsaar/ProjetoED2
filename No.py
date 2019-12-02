
from Filme import Filme
class Node:
    def __init__(self, filme=None, left=None, right=None):
        self._filme = filme
        self._left = left
        self._right = right
        self.balance = 0
    def set_filme(self, filme):
        self._filme = filme

    def get_filme(self):
        return self._filme

    def set_left(self, left):
        self._left = left

    def get_left(self):
        return self._left

    def set_right(self, right):
        self._right = right

    def get_right(self):
        return self._right

    

    def insert(self, filme):
        if self.get_filme() == None:
            self.set_filme(filme)
            return self
        else:
            p = self
            while True:
                if p.get_filme().get_nome() > filme.get_nome():
                    if p.get_left() == None:
                        node = Node(filme)
                        p.set_left(node)
                        break
                    else:
                        p = p.get_left()
                elif p.get_filme().get_nome() < filme.get_nome():
                    if p.get_right() == None:
                        node = Node(filme)
                        p.set_right(node)
                        break
                    else:
                        p = p.get_right()
                elif p.get_filme().get_nome() == filme.get_nome():
                    print(filme.get_nome())
                    return None
            if self.is_balanced(self) == False:
            	self = self.do_balance(self, filme.get_nome())
            	#pass
            return self
    def left_rotation(self, root):
        y = root.get_right()
        z = y.get_left()

        # Rotaciona
        y.set_left(root)
        root.set_right(z)

        # Muda os pesos
        lh = root.height(root.get_left()) - 1
        rh = root.height(root.get_right()) - 1
        root.balance = lh - rh

        lh = root.height(y.get_left()) - 1
        rh = root.height(y.get_right()) - 1
        y.balance = lh - rh

        # Retorna a raiz
        return y


    def right_rotation(self, root):
        y = root.get_left()
        z = y.get_right()

        # Rotaciona
        y.set_right(root)
        root.set_left(z)

        # Muda os pesos
        lh = root.height(root.get_left()) - 1
        rh = root.height(root.get_right()) - 1
        root.balance = lh - rh

        lh = root.height(y.get_left()) - 1
        rh = root.height(y.get_right()) - 1
        y.balance = lh - rh

        # Retorna a raiz
        return y

    def do_balance(self, root, key):
        balance = root.balance
        # Esquerda - Esquerda
        if balance > 1 and key < root.get_left().get_filme().get_nome():
            return self.right_rotation(root)

        # Direita - Direita
        if balance < -1 and key > root.get_right().get_filme().get_nome():
            y = self.left_rotation(root)
            return y
        #Rotacao dupla Esquerda - Direta
        if balance > 1 and key > root.get_left().get_filme().get_nome():
            root.set_left(root.left_rotation(root.get_left()))
            return self.right_rotation(root)

        # Rotacao dupla Direita - Esquerda
        if balance < -1 and key < root.get_right().get_filme().get_nome():
            root.set_right(root.right_rotation(root.get_right()))
            return self.left_rotation(root)

        return root
    def list_items(self):
        right = self.get_right()
        left = self.get_left()
        if self is not None and self.get_filme() is not None:
            if left != None:
                left.list_items()
            print(self.get_filme().get_nome())
            if right != None:
                right.list_items()



    def search_by_name(self, name):
        #Busca pelo nome
        p = self
        while True:
            #caso nao ache um filme, eventualmente o p sera None
            if p is None or p.get_filme() is None:
                return None
            if p.get_filme().get_nome() == name:
                return p.get_filme()
            else:
                #move o p de acordo com a possivel posição (esquerda/direita) do filme(node)
                if p.get_filme().get_nome() > name:
                    p = p.get_left()
                elif p.get_filme().get_nome() < name:
                    p = p.get_right()

    def search(self, name):
        #usando recursividade
        left = self.get_left()
        right = self.get_right()
        if self is not None:
            if self.get_filme().get_nome() > name:
                if left is not None:
                    return left.search(name)
            elif self.get_filme().get_nome() < name:
                if right is not None:
                    return right.search(name)
            else:
                return self
    def in_order_successor(self, root):
       	    
       	    p = root.get_right()
       	    while p.get_left() is not None:
       	    	p  = p.get_left()
       	    return p

    def search_by_id(self, aid):
    
        left = self.get_left()
        right = self.get_right()
        if self is not None:
            if left is not None:
                left.search_by_id(aid)
            if self.get_filme().get_aid() == aid:
                print("Nome: ", self.get_filme().get_nome())
                print("Ano: ", self.get_filme().get_ano())
                print("id: ", self.get_filme().get_aid())
                print("-" * 20)
            if right is not None:
                right.search_by_id(aid)

    def height(self, root):
    #Altura da arvore
        if root is None:
            return 0
        return max(self.height(root.get_right()), self.height(root.get_left())) + 1

    def is_balanced(self, root):
    #Se balanceada, = a true
        if root is None:
            return True

        lh = root.height(root.get_left()) - 1
        rh = root.height(root.get_right()) - 1
        root.balance = lh - rh

        if ((abs(lh - rh) <= 1) and self.is_balanced(root.get_left()) is True and self.is_balanced(root.get_right()) is True):
            return True

        return False

    def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self._right != None:
            ret += self._right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self._filme._aid)

        # Print left branch
        if self._left != None:
            ret += self._left.__str__(depth + 1)

        return ret
