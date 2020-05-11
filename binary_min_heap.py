from time import sleep

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_min_heap:
    def __init__(self):
        self.root = None


    def get_li(self):
        hl = []
        if self.root == None:
            return hl

        cur_node = self.root
        q = []
        q.append(cur_node)
        while len(q) != 0:
            temp = q.pop(0)
            hl.append(temp.data)
            if temp.left != None:
                q.append(temp.left)

            if temp.right != None:
                q.append(temp.right)

        return hl

    #recursive version of get_node()
    # def get_node(self, data, cur_node):
    #     if cur_node.data == data:
    #         return cur_node
    #     elif cur_node.left != None:
    #         return self.get_node(data, cur_node.left)
    #     elif cur_node.right != None:
    #         return self.get_node(data, cur_node.right)

    def get_node(self, data):
        cur_node = self.root
        q = []
        q.append(cur_node)
        while len(q) != 0:
            temp = q.pop(0)
            if temp.data == data:
                return temp

            if temp.left != None:
                q.append(temp.left)

            if temp.right != None:
                q.append(temp.right)


    def heapify_up(self, data):
        cur_node = self.get_node(data)
        while True:
            li = self.get_li()
            i = li.index(cur_node.data)
            parent = li[int((i-1)/2)]
            parent_node = self.get_node(parent)
            if cur_node.data < parent_node.data:
                temp = cur_node.data
                cur_node.data = parent_node.data
                parent_node.data = temp
            else:
                return

            cur_node = parent_node


    def _insert(self, data):
        validation_staus = False
        new_node = Node(data)
        cur_node = self.root
        q = []
        q.append(cur_node)
        while len(q) != 0:
            temp = q.pop(0)

            if temp.left == None:
                temp.left = new_node
                if new_node.data < temp.data:
                    validation_staus = True

                return validation_staus
            else:
                q.append(temp.left)

            if temp.right == None:
                temp.right = new_node
                if new_node.data < temp.data:
                    validation_staus = True

                return validation_staus
            else:
                q.append(temp.right)


    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            print(f'{bcolors.SUCCESS}Data added.{bcolors.ENDC}')
        else:
            hl = self.get_li()
            if data in hl:
                print(f'{bcolors.FAIL}Data {data} already present.{bcolors.ENDC}')
                return
            else:
                need_validation = self._insert(data)
                print(f'{bcolors.SUCCESS}Data added.{bcolors.ENDC}')
                if need_validation:
                    print(f'{bcolors.WARNING}Validating...{bcolors.ENDC}')
                    self.heapify_up(data)
                    sleep(1)


    def heapify_down(self, key_node):
        cur_node = key_node
        while True:
            if cur_node.left == None and cur_node.right == None:
                return
            elif cur_node.left == None:
                right_node = cur_node.right
                if cur_node.data > right_node.data:
                    temp = cur_node.data
                    cur_node.data = right_node.data
                    right_node.data = temp
                    cur_node = right_node
                else:
                    return
            elif cur_node.right == None:
                left_node = cur_node.left
                if cur_node.data > left_node.data:
                    temp = cur_node.data
                    cur_node.data = left_node.data
                    left_node.data = temp
                    cur_node = left_node
                else:
                    return
            else:
                left_node = cur_node.left
                right_node = cur_node.right

                min_child = min(left_node.data, right_node.data)
                if cur_node.data > min_child:
                    if min_child == left_node.data:
                        temp = cur_node.data
                        cur_node.data = left_node.data
                        left_node.data = temp
                        cur_node = left_node
                    elif min_child == right_node.data:
                        temp = cur_node.data
                        cur_node.data = right_node.data
                        right_node.data = temp
                        cur_node = right_node
                else:
                    return


    def del_last(self):
        li = self.get_li()
        key = li[-1]
        i = len(li) - 1
        parent = li[int((i - 1) / 2)]
        parent_node = self.get_node(parent)
        if parent_node.left.data == key:
            parent_node.left = None
            return

        if parent_node.right.data == key:
            parent_node.right = None
            return


    def delete(self, key):
        del_status = False
        if self.root == None:
            return

        li = self.get_li()
        if key in li:
            key_node = self.get_node(key)
            if key_node.left == None and key_node.right == None:
                if key_node == self.root:
                    self.root = key_node = None
                else:
                    self.del_last()
            else:
                key_node.data = li[-1]
                self.del_last()
                self.heapify_down(key_node)

            del_status = True

        return del_status


    def display(self):
        if self.root == None:
            print(f'{bcolors.WARNING}Heap has no nodes.{bcolors.ENDC}')
            return

        li = self.get_li()
        print(li)


    def count(self):
        if self.root == None:
            return 0

        li = self.get_li()
        count = len(li)
        return count


    def _height(self, cur_node, ht):
        if cur_node == None:
            return ht

        left_ht = self._height(cur_node.left, ht + 1)
        right_ht = self._height(cur_node.right, ht + 1)

        return max(left_ht, right_ht)


    def height(self):
        if self.root == None:
            return 0

        return self._height(self.root, 0)


if __name__ == "__main__":
    bcolors = bcolors()
    bh = Binary_min_heap()
    while True:
        try:
            choice = int(input('''1. Insert
2. Delete
3. Display
4. Count and height
5. Exit
Enter your choice: '''))
        except ValueError:
            print(f'{bcolors.WARNING}\nEnter only number.\n{bcolors.ENDC}')
        else:
            if choice == 1:
                print('\n----------------------------------------')
                try:
                    data = int(input('Enter data to be inserted: '))
                except ValueError:
                    print(f'{bcolors.WARNING}Enter only number.{bcolors.ENDC}')
                else:
                    bh.insert(data)
                    bh.display()

                print('----------------------------------------\n')
            elif choice == 2:
                print('\n----------------------------------------')
                bh.display()
                try:
                    data = int(input('Enter data to be deleted: '))
                except ValueError:
                    print(f'{bcolors.WARNING}Enter only number.{bcolors.ENDC}')
                else:
                    data_deleted = bh.delete(data)
                    if data_deleted:
                        print(f'{bcolors.SUCCESS}Data deleted.{bcolors.ENDC}')
                        bh.display()
                    else:
                        print(f'{bcolors.FAIL}Data {data} not found.{bcolors.ENDC}')

                print('----------------------------------------\n')
            elif choice == 3:
                print('\n----------------------------------------')
                bh.display()
                print('----------------------------------------\n')
            elif choice == 4:
                print('\n----------------------------------------')
                print(f'Nodes in heap: {bh.count()}')
                print(f'Height of heap: {bh.height()}')
                print('----------------------------------------\n')
            elif choice == 5:
                print(f'{bcolors.FAIL}\nClosing...{bcolors.ENDC}')
                sleep(1)
                break
            else:
                print(f'{bcolors.WARNING}\nWrong choice.\n{bcolors.ENDC}')